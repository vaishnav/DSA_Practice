# Implement an algorithm to determine if a string has all unique characters, What if you cannot use additional data structures ?
from tester import DSATest

class UniqueChars(DSATest):
    def solution(self, s: str):
        return len(set(s)) == len(s)
    
if __name__ == "__main__":
    test_cases = [
        ("", True),                       # Empty string
        ("a", True),                      # Single character
        ("abcdefg", True),                # All unique
        ("hello", False),                 # Duplicate 'l'
        ("Aa", True),                     # Case-sensitive unique
        ("abcdefghijklmnopaqrstuvwxyzA", False),  # Duplicate 'A'
        ("hi there", False),              # Duplicate 'h' and space
        ("1234567890", True),             # All unique digits
    ]


    # Create an instance of the problem subclass
    tester = UniqueChars()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
    print("\nDetailed Test Report:\n")
    print(report)

    # sol = UniqueChars()
    # comparison = sol.compare_solutions(UniqueCharsBitwise().solution, test_cases=test_cases)

    # print("\nComparison Summary:")
    # print(comparison)