
from abc import ABC, abstractmethod
import time
import traceback
import sys
from typing import Any, List, Tuple, Optional, Dict, Callable
from functools import wraps
import json
import copy

class DSATest(ABC):
    def __init__(self):
        self.test_results: List[Dict] = []
        self.performance_data: Dict[str, Any] = {}

    @abstractmethod
    def solution(self, *args, **kwargs):
        """To be implemented in problem file"""
        pass

    def _measure_performance(func: Callable) -> Callable:
        """Decorator to measure execution time and memory usage"""
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # Get memory before (simplified approach)
            import psutil
            import os
            process = psutil.Process(os.getpid())
            memory_before = process.memory_info().rss

            start_time = time.perf_counter()
            result = func(self, *args, **kwargs)
            end_time = time.perf_counter()

            memory_after = process.memory_info().rss
            execution_time = end_time - start_time
            memory_used = memory_after - memory_before

            return result, {
                'execution_time': execution_time,
                'memory_used': memory_used
            }
        return wrapper

    def run_tests(self, test_cases: List[Tuple], 
                  show_performance: bool = True,
                  timeout: Optional[float] = None,
                  verbose: bool = True) -> Dict[str, Any]:
        """
        Run test cases with enhanced reporting and performance metrics

        Args:
            test_cases: List of (input, expected_output) tuples
            show_performance: Whether to show performance metrics
            timeout: Maximum execution time per test in seconds
            verbose: Whether to show detailed output

        Returns:
            Dictionary containing test results and statistics
        """
        passed = 0
        failed = 0
        exceptions = 0
        total = len(test_cases)
        total_time = 0
        total_memory = 0

        self.test_results = []

        if verbose:
            print(f"Running {total} test cases...")
            print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            test_input, expected = test_case

            # Normalize input to tuple
            if not isinstance(test_input, tuple):
                test_input = (test_input,)

            test_result = {
                'test_number': i,
                'input': test_input,
                'expected': expected,
                'status': 'unknown',
                'execution_time': 0,
                'memory_used': 0,
                'output': None,
                'error': None
            }

            try:
                # Measure performance
                start_time = time.perf_counter()

                # Simple timeout implementation
                if timeout:
                    import signal
                    def timeout_handler(signum, frame):
                        raise TimeoutError(f"Test timed out after {timeout} seconds")
                    signal.signal(signal.SIGALRM, timeout_handler)
                    signal.alarm(int(timeout))

                # Run the solution
                test_input_pass = copy.deepcopy(test_input)
                result = self.solution(*test_input_pass)

                if timeout:
                    signal.alarm(0)  # Cancel timeout

                end_time = time.perf_counter()
                execution_time = end_time - start_time

                test_result['output'] = result
                test_result['execution_time'] = execution_time
                total_time += execution_time

                # Check result
                if result == expected:
                    test_result['status'] = 'passed'
                    passed += 1
                    if verbose:
                        time_str = f" ({execution_time*1000:.2f}ms)" if show_performance else ""
                        print(f"Test {i}: ✅ Passed{time_str}")
                else:
                    test_result['status'] = 'failed'
                    failed += 1
                    if verbose:
                        print(f"Test {i}: ❌ Failed | Input: {test_input} | Expected: {expected} | Got: {result}")

            except TimeoutError as e:
                test_result['status'] = 'timeout'
                test_result['error'] = str(e)
                exceptions += 1
                if verbose:
                    print(f"Test {i}: ⏱️ Timeout | Input: {test_input} | {e}")

            except Exception as e:
                test_result['status'] = 'exception'
                test_result['error'] = str(e)
                test_result['traceback'] = traceback.format_exc()
                exceptions += 1
                if verbose:
                    print(f"Test {i}: ⚠️ Exception | Input: {test_input} | {e}")

            self.test_results.append(test_result)

        # Calculate statistics
        percentage = (passed / total) * 100 if total > 0 else 0
        avg_time = total_time / total if total > 0 else 0

        results_summary = {
            'total_tests': total,
            'passed': passed,
            'failed': failed,
            'exceptions': exceptions,
            'success_rate': percentage,
            'total_time': total_time,
            'average_time': avg_time,
            'test_results': self.test_results
        }

        if verbose:
            print("-" * 50)
            print(f"Results: {passed}/{total} tests passed ({percentage:.2f}%)")
            if show_performance:
                print(f"Total execution time: {total_time*1000:.2f}ms")
                print(f"Average time per test: {avg_time*1000:.2f}ms")

            if failed > 0:
                print(f"Failed tests: {failed}")
            if exceptions > 0:
                print(f"Exceptions: {exceptions}")

        return results_summary

    def run_single_test(self, test_input: Any, expected: Any, verbose: bool = True) -> Dict[str, Any]:
        """Run a single test case"""
        return self.run_tests([(test_input, expected)], verbose=verbose)

    def generate_report(self, filename: Optional[str] = None) -> str:
        """Generate a detailed test report"""
        if not self.test_results:
            return "No test results available. Run tests first."

        report = []
        report.append("=== DSA Test Report ===\n")

        # Summary
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r['status'] == 'passed')
        failed = sum(1 for r in self.test_results if r['status'] == 'failed')
        exceptions = sum(1 for r in self.test_results if r['status'] in ['exception', 'timeout'])

        report.append(f"Total Tests: {total}")
        report.append(f"Passed: {passed} ({passed/total*100:.1f}%)")
        report.append(f"Failed: {failed} ({failed/total*100:.1f}%)")
        report.append(f"Exceptions: {exceptions} ({exceptions/total*100:.1f}%)")
        report.append("")

        # Performance summary
        execution_times = [r['execution_time'] for r in self.test_results if r['execution_time'] > 0]
        if execution_times:
            report.append("Performance Summary:")
            report.append(f"Total time: {sum(execution_times)*1000:.2f}ms")
            report.append(f"Average time: {sum(execution_times)/len(execution_times)*1000:.2f}ms")
            report.append(f"Min time: {min(execution_times)*1000:.2f}ms")
            report.append(f"Max time: {max(execution_times)*1000:.2f}ms")
            report.append("")

        # Failed tests details
        failed_tests = [r for r in self.test_results if r['status'] in ['failed', 'exception', 'timeout']]
        if failed_tests:
            report.append("Failed Test Details:")
            for test in failed_tests:
                report.append(f"Test {test['test_number']}: {test['status'].upper()}")
                report.append(f"  Input: {test['input']}")
                report.append(f"  Expected: {test['expected']}")
                if test['output'] is not None:
                    report.append(f"  Got: {test['output']}")
                if test['error']:
                    report.append(f"  Error: {test['error']}")
                report.append("")

        report_text = "\n".join(report)

        if filename:
            with open(filename, 'w') as f:
                f.write(report_text)
            print(f"Report saved to {filename}")

        return report_text

    def export_results(self, filename: str, format: str = 'json'):
        """Export test results to file"""
        if format.lower() == 'json':
            with open(filename, 'w') as f:
                json.dump(self.test_results, f, indent=2, default=str)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def compare_solutions(self, other_solution: Callable, test_cases: List[Tuple]) -> Dict[str, Any]:
        """Compare this solution with another solution"""
        print("Comparing solutions...")

        # Run tests on current solution
        current_results = self.run_tests(test_cases, verbose=False)

        # Create temporary test class for other solution
        class TempTest(DSATest):
            def __init__(self, solution_func):
                super().__init__()
                self.solution_func = solution_func

            def solution(self, *args, **kwargs):
                return self.solution_func(*args, **kwargs)

        other_tester = TempTest(other_solution)
        other_results = other_tester.run_tests(test_cases, verbose=False)

        comparison = {
            'current_solution': {
                'success_rate': current_results['success_rate'],
                'total_time': current_results['total_time'],
                'average_time': current_results['average_time']
            },
            'other_solution': {
                'success_rate': other_results['success_rate'],
                'total_time': other_results['total_time'],
                'average_time': other_results['average_time']
            }
        }

        # Determine winner
        if current_results['success_rate'] > other_results['success_rate']:
            comparison['winner'] = 'current (better correctness)'
        elif current_results['success_rate'] < other_results['success_rate']:
            comparison['winner'] = 'other (better correctness)'
        elif current_results['average_time'] < other_results['average_time']:
            comparison['winner'] = 'current (faster)'
        elif current_results['average_time'] > other_results['average_time']:
            comparison['winner'] = 'other (faster)'
        else:
            comparison['winner'] = 'tie'

        print(f"Winner: {comparison['winner']}")
        return comparison
