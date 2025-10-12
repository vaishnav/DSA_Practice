# Implement an algorithm to delete a node in the middle (ie. any node but the first and last node, not necessarily the exact middle) of a singly liked list,
# given only access to that node
# Example [1,2,3,4,5,6] will turn to [1,2,4,5,6]
from tester import DSATest
from LinkedList.linkedList import *


class DeleteMiddle(DSATest):
    def solution(self, link_list: SingleNode):
        if not link_list:
            return link_list

        slow_pointer = link_list
        fast_pointer = link_list.next
        previous = None
        while fast_pointer:
            fast_pointer = fast_pointer.next
            if not fast_pointer:
                break

            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
            if not previous:
                previous = link_list
            else:
                previous = previous.next
        
        # First element is the middle element
        if not previous:
            link_list = link_list.next
            return link_list

        previous.next = slow_pointer.next
        return link_list


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
        [[1], []],
        [[], []],
        [[1, 2], [2]],
        [[1, 2, 3], [1, 3]],
        [[1, 2, 3, 4], [1, 3, 4]],
        [[1, 2, 3, 4, 5], [1, 2, 4, 5]],
        [[1, 2, 3, 4, 5, 6], [1, 2, 4, 5, 6]],
        [[0, 0, 0], [0, 0]],
        [[-1, -2, -3, -4, -5], [-1, -2, -4, -5]],
        [[5, 5], [5]],
        [[7, 7, 7, 7], [7, 7, 7]],
        [[10, 20, 30, 40, 50, 60, 70], [10, 20, 30, 50, 60, 70]],
        [[9, 8, 7, 6, 5, 4], [9, 8, 6, 5, 4]],
        [[2, 4, 6, 8, 10], [2, 4, 8, 10]],
        [[1000000, 2000000, 3000000], [1000000, 3000000]],
        [[1, 1, 2, 2, 3, 3, 4, 4], [1, 1, 2, 3, 3, 4, 4]],
        [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9]],
        [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 5, 6, 7, 8]],
        [[42], []],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]],
        [[5, 4, 3, 2, 1], [5, 4, 2, 1]],
        [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 5, 6, 7, 8]],
        [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]],
        [[100], []],
        [[1, 2, 2, 2, 2, 3], [1, 2, 2, 2, 3]],
        [[1, 3, 3, 3, 5], [1, 3, 3, 5]],
        [[11, 22], [22]],
        [[0], []],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 6, 7, 8, 9, 10]],
        [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
        [[0, -1, -2, -3, -4], [0, -1, -3, -4]],
        [[9, 7, 5, 3, 1], [9, 7, 3, 1]],
        [[1, 2, 2, 3, 3, 3, 4, 4, 4, 4], [1, 2, 2, 3, 3, 4, 4, 4, 4]],
        [[100, -100, 200, -200, 300, -300], [100, -100, -200, 300, -300]],
        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
        [
            [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],
            [1, 3, 5, 7, 9, 13, 15, 17, 19, 21, 23],
        ],
        [[4, 3, 2, 1, 0, -1, -2, -3, -4], [4, 3, 2, 1, -1, -2, -3, -4]],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13],
        ],
        [[9, 9], [9]],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]],
        [[2, 4], [4]],
        [[0, 1], [1]],
        [[1, 0, -1, 0, 1], [1, 0, 0, 1]],
        [[5, 4, 4, 4, 4, 5, 6], [5, 4, 4, 4, 5, 6]],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        ],
        [[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], [3, 1, 4, 1, 5, 2, 6, 5, 3, 5]],
    ]

    test_cases = get_test_cases(base_test_cases)

    # Create an instance of the problem subclass
    tester = DeleteMiddle()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
