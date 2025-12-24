"""
Lab Tests Framework
A simple testing framework for laboratory experiments and tests.
"""

__version__ = "0.1.0"


class LabTest:
    """Base class for lab tests."""
    
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.passed = None
        self.result = None
    
    def run(self):
        """Run the test. Override this method in subclasses."""
        raise NotImplementedError("Subclasses must implement run()")
    
    def assert_equal(self, actual, expected, message=""):
        """Assert that two values are equal."""
        if actual != expected:
            self.passed = False
            self.result = f"AssertionError: {actual} != {expected}. {message}"
            raise AssertionError(self.result)
        return True
    
    def assert_true(self, condition, message=""):
        """Assert that a condition is true."""
        if not condition:
            self.passed = False
            self.result = f"AssertionError: Condition is False. {message}"
            raise AssertionError(self.result)
        return True
    
    def assert_false(self, condition, message=""):
        """Assert that a condition is false."""
        if condition:
            self.passed = False
            self.result = f"AssertionError: Condition is True. {message}"
            raise AssertionError(self.result)
        return True


class LabTestRunner:
    """Test runner for lab tests."""
    
    def __init__(self):
        self.tests = []
        self.results = []
    
    def add_test(self, test):
        """Add a test to the runner."""
        self.tests.append(test)
    
    def run_all(self):
        """Run all tests and collect results."""
        self.results = []
        passed = 0
        failed = 0
        
        print(f"\nRunning {len(self.tests)} tests...\n")
        
        for test in self.tests:
            try:
                test.run()
                test.passed = True
                test.result = "PASSED"
                passed += 1
                print(f"✓ {test.name}: PASSED")
            except Exception as e:
                test.passed = False
                test.result = str(e)
                failed += 1
                print(f"✗ {test.name}: FAILED - {e}")
            
            self.results.append({
                'name': test.name,
                'description': test.description,
                'passed': test.passed,
                'result': test.result
            })
        
        print(f"\n{'='*50}")
        print(f"Total: {len(self.tests)} | Passed: {passed} | Failed: {failed}")
        print(f"{'='*50}\n")
        
        return passed, failed
