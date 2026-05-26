#!/usr/bin/env python3
"""
mutation_runner.py — Automates mutation testing for the Calculator class.

This script:
1. Runs the test suite against the original (unmutated) code to confirm
   all tests pass.
2. For each mutant file, imports it in place of the original calculator
   and runs the test suite.
3. Records which mutants are killed (tests fail → mutant detected) and
   which survive (tests still pass → mutant undetected).
4. Computes the Mutation Score = (Killed / Total) * 100.

Usage:
    python mutation_runner.py
"""

import importlib
import importlib.util
import sys
import os
import types
from typing import Dict, List, Tuple


# Mutant registry: id -> (filename, mutation_type, description)
MUTANTS: Dict[str, Tuple[str, str, str]] = {
    "mutant_1": (
        "mutants/mutant_1.py",
        "Arithmetic Operator Change",
        "Changed add (+) to subtract (-)",
    ),
    "mutant_2": (
        "mutants/mutant_2.py",
        "Operator Swap",
        "Changed multiply (*) to divide (/)",
    ),
    "mutant_3": (
        "mutants/mutant_3.py",
        "Off-by-One / Boundary",
        "Changed exponent b to b + 1 in power()",
    ),
    "mutant_4": (
        "mutants/mutant_4.py",
        "Relational Operator Change",
        "Changed b == 0 to b <= 0 in divide()",
    ),
    "mutant_5": (
        "mutants/mutant_5.py",
        "Condition Negation",
        "Changed b == 0 to b != 0 in modulo()",
    ),
}


def import_module_from_file(module_name: str, filepath: str) -> types.ModuleType:
    """Import a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {filepath}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_tests(calculator_module: types.ModuleType) -> Tuple[int, int, List[str]]:
    """Run pytest tests against a given calculator module.

    We temporarily replace the 'calculator' module in sys.modules with
    the mutant version, then run pytest tests against our test file.

    Returns:
        Tuple of (passed, total, failure_messages).
    """
    import pytest

    # Save original module
    orig_module = sys.modules.get("calculator")

    # Install mutant as calculator module
    sys.modules["calculator"] = calculator_module

    try:
        # Run pytest programmatically
        test_file = os.path.join(os.path.dirname(__file__), "test_mutation.py")
        exit_code = pytest.main(
            [
                test_file,
                "-v",
                "--tb=short",
                "--no-header",
            ],
        )
    finally:
        # Restore original module
        if orig_module:
            sys.modules["calculator"] = orig_module
        else:
            del sys.modules["calculator"]

    # pytest exit codes: 0 = all passed, 1 = some failed, 2 = error
    total = 0
    passed = 0
    failures: List[str] = []

    # We'll parse the exit code — 0 means killed (tests failed = mutant detected)
    # Actually: exit 0 = all passed = mutant NOT killed (alive)
    # exit 1 = some failed = mutant KILLED
    return exit_code, failures


def run_tests_via_subprocess(mutant_path: str) -> Tuple[bool, str]:
    """Run tests using a modified PYTHONPATH to load the mutant.

    Returns:
        Tuple of (killed, output_string).
    """
    import subprocess

    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(script_dir, "test_mutation.py")
    mutant_abs = os.path.abspath(os.path.join(script_dir, mutant_path))

    # Create a loader script that patches sys.modules before running tests
    loader_script = f"""
import sys
import importlib.util

# Load the mutant module
spec = importlib.util.spec_from_file_location("calculator", "{mutant_abs}")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sys.modules["calculator"] = module

# Now run pytest
import pytest
test_file = "{test_file}"
exit_code = pytest.main([test_file, "-v", "--tb=short", "--no-header"])
sys.exit(exit_code)
"""

    result = subprocess.run(
        [sys.executable, "-c", loader_script],
        capture_output=True,
        text=True,
        timeout=30,
    )

    # Exit code 0 = all tests passed → mutant ALIVE (not killed)
    # Exit code 1 = some tests failed → mutant KILLED
    killed = result.returncode != 0
    output = result.stdout + result.stderr
    return killed, output


def test_original_passes() -> bool:
    """Verify that all tests pass against the original calculator."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(script_dir, "test_mutation.py")

    import subprocess
    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_file, "-v", "--tb=short", "--no-header"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.returncode == 0


def run_mutation_testing() -> Dict[str, Tuple[bool, str]]:
    """Run all mutants and return results.

    Returns:
        Dict mapping mutant_id -> (killed, output).
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 70)
    print("MUTATION TESTING RUNNER")
    print("=" * 70)
    print()

    # Step 1: Verify original passes
    print(">>> Verifying original calculator passes all tests...")
    if test_original_passes():
        print("    ✅ All tests pass on original code.\n")
    else:
        print("    ❌ Tests FAIL on original code! Fix tests before proceeding.\n")
        return {}

    # Step 2: Test each mutant
    results: Dict[str, Tuple[bool, str]] = {}

    for mutant_id, (mutant_path, mut_type, desc) in MUTANTS.items():
        print(f">>> Testing {mutant_id} ({mut_type})...")
        print(f"    {desc}")
        killed, output = run_tests_via_subprocess(mutant_path)
        status = "KILLED" if killed else "SURVIVED"
        results[mutant_id] = (killed, output)

        if killed:
            print(f"    ❌ Mutant {mutant_id}: KILLED (tests detected the mutation)")
        else:
            print(f"    ⚠️  Mutant {mutant_id}: SURVIVED (tests did not detect)")
        print()

    # Step 3: Report
    print("=" * 70)
    print("MUTATION TESTING RESULTS")
    print("=" * 70)
    print()

    total = len(results)
    killed_count = sum(1 for k, _ in results.values() if k)
    survived = total - killed_count
    score = (killed_count / total) * 100 if total > 0 else 0

    print(f"{'Mutant':<12} {'Type':<30} {'Killed?':<10} {'Test Evidence'}")
    print("-" * 70)

    for mutant_id, (mutant_path, mut_type, desc) in MUTANTS.items():
        if mutant_id in results:
            killed, output = results[mutant_id]
            killed_str = "✅ YES" if killed else "❌ NO"
            # Extract which test killed it from output
            evidence = ""
            if killed:
                # Parse output for FAILED test names
                for line in output.split("\n"):
                    if "FAILED" in line:
                        evidence = line.strip()
                        break
                # Also look for assertion errors
                if not evidence:
                    for line in output.split("\n"):
                        if "AssertionError" in line or "assert" in line:
                            evidence = line.strip()
                            break
            if not evidence:
                evidence = "See full output"
            print(f"{mutant_id:<12} {mut_type:<30} {killed_str:<10} {evidence[:60]}")

    print()
    print("-" * 70)
    print(f"Total Mutants:     {total}")
    print(f"Killed:            {killed_count}")
    print(f"Survived:          {survived}")
    print(f"Mutation Score:    {score:.1f}%")
    print("-" * 70)

    return results


def main() -> None:
    """Entry point for mutation testing."""
    run_mutation_testing()


if __name__ == "__main__":
    main()
