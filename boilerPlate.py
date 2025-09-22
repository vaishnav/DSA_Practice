# Question Description
from tester import DSATest

class FirstSolution(DSATest):
    def solution(self, s: str):
        pass
    
class SecondSolution(DSATest):
    def solution(self, s: str):
        pass
        

if __name__ == "__main__":
    test_cases = [
    ]


    # Create an instance of the problem subclass
    tester = FirstSolution()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
    print("\nDetailed Test Report:\n")
    print(report)

    # sol = FirstSolution()
    # comparison = sol.compare_solutions(SecondSolution().solution, test_cases=test_cases)

    # print("\nComparison Summary:")
    # print(comparison)