"""
Demo of using the custom LabTest framework.
"""
from lab_tests import LabTest, LabTestRunner
from lab_tests.calculator import add, subtract, multiply, is_even


class AdditionTest(LabTest):
    """Test addition functionality."""
    
    def run(self):
        self.assert_equal(add(2, 3), 5, "2 + 3 should equal 5")
        self.assert_equal(add(-1, 1), 0, "-1 + 1 should equal 0")
        self.assert_equal(add(0, 0), 0, "0 + 0 should equal 0")


class SubtractionTest(LabTest):
    """Test subtraction functionality."""
    
    def run(self):
        self.assert_equal(subtract(5, 3), 2, "5 - 3 should equal 2")
        self.assert_equal(subtract(10, 10), 0, "10 - 10 should equal 0")


class MultiplicationTest(LabTest):
    """Test multiplication functionality."""
    
    def run(self):
        self.assert_equal(multiply(3, 4), 12, "3 * 4 should equal 12")
        self.assert_equal(multiply(0, 5), 0, "0 * 5 should equal 0")


class EvenNumberTest(LabTest):
    """Test even number checker."""
    
    def run(self):
        self.assert_true(is_even(2), "2 should be even")
        self.assert_true(is_even(4), "4 should be even")
        self.assert_false(is_even(3), "3 should not be even")


def main():
    """Run all custom lab tests."""
    runner = LabTestRunner()
    
    runner.add_test(AdditionTest("Addition Test", "Test basic addition operations"))
    runner.add_test(SubtractionTest("Subtraction Test", "Test basic subtraction operations"))
    runner.add_test(MultiplicationTest("Multiplication Test", "Test basic multiplication operations"))
    runner.add_test(EvenNumberTest("Even Number Test", "Test even number detection"))
    
    passed, failed = runner.run_all()
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    exit(main())
