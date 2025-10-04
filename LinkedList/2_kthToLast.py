# Implement an algorith to find the kth to last element of a singly linked list
from tester import DSATest
from LinkedList.linkedList import *


class KthToLast(DSATest):
    def solution(self, llist: SingleNode, kth: int):
        last_pointer = llist
        for i in range(kth):
            if last_pointer:
                last_pointer = last_pointer.next
            else:
                return None
            
        curr = llist
        while last_pointer:
            last_pointer = last_pointer.next
            curr = curr.next

        if curr:
            return curr.data
        return None


def get_test_cases(cases: list):
    final_cases = []
    for case in cases:
        input_case = SinglyLinkedList()
        input_case.appendList(case[0])
        input_case_head = input_case.getList()

        final_cases.append([(input_case_head, case[1]), case[2]])

    return final_cases

if __name__ == "__main__":
    base_test_cases = [
        # Basic cases
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 2, 4),
        ([1, 2, 3, 4, 5], 3, 3),
        ([1, 2, 3, 4, 5], 4, 2),
        ([1, 2, 3, 4, 5], 5, 1),
        # Single element
        ([10], 1, 10),
        ([10], 0, None),
        ([10], 2, None),
        # Two elements
        ([1, 2], 1, 2),
        ([1, 2], 2, 1),
        # Empty list
        ([], 1, None),
        ([], 0, None),
        ([], 5, None),
        # k greater than length
        ([1, 2, 3], 4, None),
        ([1, 2, 3], 10, None),
        ([5, 10], 5, None),
        # k = 0 (invalid)
        ([1, 2, 3, 4], 0, None),
        ([10, 20], 0, None),
        # Negative k (invalid)
        ([1, 2, 3], -1, None),
        ([5, 10, 15], -5, None),
        # Lists with duplicates
        ([1, 1, 1, 1], 1, 1),
        ([1, 1, 1, 1], 2, 1),
        ([5, 3, 5, 3, 5], 3, 5),
        ([2, 2, 2, 2, 2], 5, 2),
        # Lists with negative numbers
        ([-1, -2, -3, -4], 1, -4),
        ([-1, -2, -3, -4], 4, -1),
        ([5, -3, 0, 7, -9], 2, 7),
        ([-10, -20, -30], 3, -10),
        # Large lists
        (list(range(1, 101)), 1, 100),
        (list(range(1, 101)), 50, 51),
        (list(range(1, 101)), 100, 1),
        (list(range(1, 101)), 101, None),
        # Lists with zeros
        ([0, 0, 0], 1, 0),
        ([0, 0, 0], 2, 0),
        ([1, 0, 2, 0, 3], 3, 2),
        # Mixed positive and negative
        ([10, -5, 20, -15, 30], 1, 30),
        ([10, -5, 20, -15, 30], 3, 20),
        ([100, -200, 300, -400], 4, 100),
        # Three elements
        ([7, 8, 9], 1, 9),
        ([7, 8, 9], 2, 8),
        ([7, 8, 9], 3, 7),
        # Large k boundary
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, None),
        # Sorted vs unsorted
        ([9, 1, 5, 3, 7], 1, 7),
        ([9, 1, 5, 3, 7], 5, 9),
        # Large values
        ([1000000, 2000000, 3000000], 2, 2000000),
        ([999999, 888888, 777777, 666666], 1, 666666),
    ]

    test_cases = get_test_cases(base_test_cases)

    # Create an instance of the problem subclass
    tester = KthToLast()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
