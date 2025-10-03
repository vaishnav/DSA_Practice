# Write code to remove duplicates from an unsorted linked list. FOLLOW UP How would you solve this problem if a temporary buffer is not allowed ?
from tester import DSATest
from LinkedList.linkedList import *


class RemoveDups(DSATest):
    def solution(self, s: SingleNode):
        dups = {}

        curr = s
        index = 0
        while curr:
            value = curr.data
            if value not in dups:
                dups[value] = set()
            else:
                dups[value].add(index)

            index += 1
            curr = curr.next

        curr = s
        for i in range(1, index):
            value = curr.next.data
            if index in dups[value]:
                if curr == s:
                    s = curr.next.next
                else:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return s
    
class RemoveDupsNoBuffer(DSATest):
    def solution(self, s: SingleNode):
        start = s
        while start:
            prev = start
            curr = start.next
            value = start.data
            while curr:
                if value == curr.data and type(value) == type(curr.data):
                    prev.next = curr.next
                else:
                    prev = prev.next
                curr = curr.next
            start = start.next
        return s


def get_test_cases(cases: list):
    final_cases = []
    for case in cases:
        input_case = SinglyLinkedList()
        input_case.appendList(case[0])
        input_case_head = input_case.getList()

        expected_output_case = SinglyLinkedList()
        expected_output_case.appendList(case[1])
        expected_output_case_head = expected_output_case.getList()

        final_cases.append([input_case_head, expected_output_case_head])

    return final_cases

if __name__ == "__main__":
    base_test_cases = [
        # Empty list
        ([], []),
        # Single element list
        ([1], [1]),
        # No duplicates, sorted order
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        # No duplicates, unsorted order
        ([5, 3, 1, 4, 2], [5, 3, 1, 4, 2]),
        # All duplicates
        ([1, 1, 1, 1, 1], [1]),
        # Multiple duplicates, unsorted
        ([4, 5, 4, 2, 2, 3, 1, 5], [4, 5, 2, 3, 1]),
        # Duplicates at beginning
        ([7, 7, 8, 9, 10], [7, 8, 9, 10]),
        # Duplicates at end
        ([11, 12, 13, 13, 13], [11, 12, 13]),
        # Duplicates in middle
        ([20, 21, 22, 22, 23, 24], [20, 21, 22, 23, 24]),
        # Large list with no duplicates
        (list(range(100)), list(range(100))),
        # Large list with duplicates
        (list(range(50)) + list(range(25, 75)), list(range(75))),
        # List with negative numbers and duplicates
        ([-1, -2, -3, -1, -2, 0], [-1, -2, -3, 0]),
        # List with zeros and duplicates
        ([0, 0, 0, 0, 0], [0]),
        # List with one element repeated many times
        ([9] * 20, [9]),
        # List with alternating duplicates
        ([1, 2, 1, 2, 1, 2], [1, 2]),
        # List with characters instead of integers
        (["a", "b", "a", "c", "b"], ["a", "b", "c"]),
        # List with mixed types (int and str) - assuming allowed
        ([1, "1", 2, "2", 1, 2], [1, "1", 2, "2"]),
        # Very large list with random duplicates
        ([i // 2 for i in range(70)], list(set([i // 2 for i in range(70)]))),
        # List with None values and duplicates
        ([None, 1, None, 2, 2, None], [None, 1, 2]),
        # List with special characters
        (["!", "@", "!", "#", "@", "$"], ["!", "@", "#", "$"]),
        # List with floats and duplicates
        ([1.1, 2.2, 1.1, 3.3, 2.2], [1.1, 2.2, 3.3]),
        # List with mixed int and float duplicates
        ([1, 1.0, 2, 2.0], [1, 1.0, 2, 2.0]),
        # List with single element repeated with spaces
        (["a", "a", "a", " "], ["a", " "]),
        # Reversed list with duplicates
        ([5, 4, 3, 2, 1, 5, 4, 3], [5, 4, 3, 2, 1]),
        # List with max int values and duplicates
        ([2**31 - 1, 2**31 - 1, 0], [2**31 - 1, 0]),
        # List with min int values and duplicates
        ([-(2**31), -(2**31), 1], [-(2**31), 1]),
        # List with alternating single and duplicates
        ([1, 2, 2, 3, 4, 4, 5], [1, 2, 3, 4, 5]),
        # List with prime numbers and duplicates
        ([2, 3, 5, 7, 11, 13, 2, 7, 11], [2, 3, 5, 7, 11, 13]),
        # List with alphabet letters repeated
        (
            [chr(65 + i // 2) for i in range(50)],
            [chr(65 + i) for i in range(25)],
        ),
        # Large random list with repeated pattern
        ([1, 2, 3, 4, 5] * 7, [1, 2, 3, 4, 5]),
        # Single element None repeated
        ([None] * 10, [None]),
        # List with boolean values and duplicates
        ([True, False, True, False], [True, False]),
        # List of empty strings and duplicates
        (["", "", "a", ""], ["", "a"]),
        # List with unicode characters with duplicates
        (["ñ", "ö", "ñ", "ü", "ö"], ["ñ", "ö", "ü"]),
    ]
    test_cases = get_test_cases(base_test_cases)

    # Create an instance of the problem subclass
    # tester = RemoveDups()
    tester = RemoveDupsNoBuffer()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
