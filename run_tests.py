#!/usr/bin/env python3
"""
Main test runner script for the lab tests framework.
"""
import sys
import os
import subprocess


def run_pytest_tests():
    """Run tests using pytest."""
    print("\n" + "="*60)
    print("Running pytest tests...")
    print("="*60 + "\n")
    
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__)) + ":" + env.get("PYTHONPATH", "")
    
    result = subprocess.run(
        ["pytest", "tests/", "-v"],
        capture_output=False,
        env=env
    )
    
    return result.returncode


def run_custom_tests():
    """Run tests using custom framework."""
    print("\n" + "="*60)
    print("Running custom framework tests...")
    print("="*60 + "\n")
    
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__)) + ":" + env.get("PYTHONPATH", "")
    
    result = subprocess.run(
        ["python", "tests/demo_custom_framework.py"],
        capture_output=False,
        env=env
    )
    
    return result.returncode


def main():
    """Main entry point."""
    print("\n" + "="*60)
    print("Lab Tests Framework - Test Runner")
    print("="*60)
    
    # Run pytest tests
    pytest_result = run_pytest_tests()
    
    # Run custom framework tests
    custom_result = run_custom_tests()
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"Pytest tests: {'PASSED' if pytest_result == 0 else 'FAILED'}")
    print(f"Custom tests: {'PASSED' if custom_result == 0 else 'FAILED'}")
    print("="*60 + "\n")
    
    # Return non-zero if any tests failed
    return max(pytest_result, custom_result)


if __name__ == "__main__":
    sys.exit(main())
