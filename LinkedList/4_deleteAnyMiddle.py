# Implement an algorithm to delete a node in the middle (ie. any node but the first and last node, not necessarily the exact middle) of a singly liked list,
# given only access to that node
# Example [1,2,3,4,5,6] will turn to [1,2,4,5,6]
from tester import DSATest
from LinkedList.linkedList import *


class DeleteMiddle(DSATest):
    def solution(self, link_list: SingleNode, delete_node: SingleNode):
        # will not be touching link_list as it will violate the condition of problem statement
        # Intereviewer will expect you to point out that if we've given the last node then the solution won't work
        curr = delete_node
        if curr == None or curr.next == None:
            return False
        
        # Just copy the data of subequent node and delete last node
        curr.data = curr.next.data
        curr.next = curr.next.next
        
        return link_list


def get_test_cases(cases: list):
    final_cases = []
    for case in cases:
        input_case = SinglyLinkedList()
        input_case.appendList(case[0][0])
        input_case_head = input_case.getList()
        node_to_remove = input_case.getNode(case[0][1])

        if case[1] == False:
            expected_output_case_head = False
        else:
            expected_output_case = SinglyLinkedList()
            expected_output_case.appendList(case[1])
            expected_output_case_head = expected_output_case.getList()

        final_cases.append([(input_case_head, node_to_remove), expected_output_case_head])

    return final_cases


if __name__ == "__main__":
    base_test_cases = [
        [[[1, 2, 3, 4, 5, 6], 2], [1, 2, 4, 5, 6]],
        [[[1, 2, 3, 4, 5, 6], 3], [1, 2, 3, 5, 6]],
        [[[1, 2, 3, 4, 5, 6], 1], [1, 3, 4, 5, 6]],
        [[[1, 2, 3, 4], 1], [1, 3, 4]],
        [[[1, 2, 3, 4], 2], [1, 2, 4]],
        [[[1, 2, 3], 1], [1, 3]],
        [[[0, 0, 0, 0], 2], [0, 0, 0]],
        [[[-1, -2, -3, -4, -5], 2], [-1, -2, -4, -5]],
        [[[5], 0], False],
        [[[1, 2], 1], False],
        [[[1, 2], 0], [2]],
        [[[10, 20, 30, 40, 50], 0], [20, 30, 40, 50]],
        [[[10, 20, 30, 40, 50], 4], False],
        [[[7, 7, 7, 7, 7], 2], [7, 7, 7, 7]],
        [[[1, 2, 2, 2, 3], 2], [1, 2, 2, 3]],
        [[[1, 2, 3, 2, 4], 3], [1, 2, 3, 4]],
        [[[9, 8, 7, 6, 5, 4, 3, 2, 1], 4], [9, 8, 7, 6, 4, 3, 2, 1]],
        [[[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 8], [1, 3, 5, 7, 9, 11, 13, 15, 19]],
        [
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 25], 
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        ],
        [
            [[100, 90, 80, 70, 60, 50, 40, 30, 20, 10], 5],
            [100, 90, 80, 70, 60, 40, 30, 20, 10],
        ],
        [[[1, 1, 2, 2, 3, 3, 4, 4], 6], [1, 1, 2, 2, 3, 3, 4]],
        [[[2, 4, 6, 8, 10], 2], [2, 4, 8, 10]],
        [[[2, 4, 6, 8, 10], 1], [2, 6, 8, 10]],
        [[[2, 4, 6, 8, 10], 3], [2, 4, 6, 10]],
        [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8], [0, 1, 2, 3, 4, 5, 6, 7, 9]],
        [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1], [0, 2, 3, 4, 5, 6, 7, 8, 9]],
        [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
        [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9], False],
        [[[1000000, 2000000, 3000000], 1], [1000000, 3000000]],
        [[[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 5], [3, 1, 4, 1, 5, 2, 6, 5, 3, 5]],
        [[[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 6], [3, 1, 4, 1, 5, 9, 6, 5, 3, 5]],
        [[[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 1], [3, 4, 1, 5, 9, 2, 6, 5, 3, 5]],
        [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8], [1, 2, 3, 4, 5, 6, 7, 8, 10]],
        [[[-5, -4, -3, -2, -1], 3], [-5, -4, -3, -1]],
        [[[42, 42, 42], 1], [42, 42]],
        [[[0, 0, 1, 1, 2, 2, 3, 3], 0], [0, 1, 1, 2, 2, 3, 3]],
        [[[0, 0, 1, 1, 2, 2, 3, 3], 7], False],
    ]

    test_cases = get_test_cases(base_test_cases)

    # Create an instance of the problem subclass
    tester = DeleteMiddle()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
