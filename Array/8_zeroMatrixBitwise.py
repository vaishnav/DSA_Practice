# Write an algorithm such that if an element is an MxN matrix is 0, its entire row and column are set to 0
from tester import DSATest


class ZeroMatrix(DSATest):
    def solution(self, arr: list):
        rows = 0
        columns = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    # we use OR if we want to set the bit as 1 irrespective of previous value, we use XOR to flip the bit
                    rows |= (1<<j)
                    columns |= (1<<i)
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                # We move the the jth or ith bit to start position and & with 1 ( basically 00001) to check if the jth or ith bit is 1 or 0
                if ((rows >> j) & 1) or ((columns >> i) & 1):
                    arr[i][j] = 0
        return arr


if __name__ == "__main__":
    test_cases = [
        # 1. 1x1 with no zero
        ([[1]], [[1]]),
        # 2. 1x1 with zero
        ([[0]], [[0]]),
        # 3. 2x2 no zero
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
        # 4. 2x2 with one zero
        ([[0, 2], [3, 4]], [[0, 0], [0, 4]]),
        # 5. 2x2 with two zeros in separate rows/cols
        ([[0, 2], [3, 0]], [[0, 0], [0, 0]]),
        # 6. 2x2 all zeros
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        # 7. 3x3 single zero center
        ([[1, 2, 3], [4, 0, 6], [7, 8, 9]], [[1, 0, 3], [0, 0, 0], [7, 0, 9]]),
        # 8. 3x3 multiple zeros
        ([[1, 0, 3], [0, 5, 6], [7, 8, 9]], [[0, 0, 0], [0, 0, 0], [0, 0, 9]]),
        # 9. 3x3 no zeros
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        # 10. 3x3 all zeros
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        # 11. 3x4 with zero at first row, last column
        (
            [[1, 2, 3, 0], [5, 6, 7, 8], [9, 10, 11, 12]],
            [[0, 0, 0, 0], [5, 6, 7, 0], [9, 10, 11, 0]],
        ),
        # 12. 3x4 with multiple zeros
        (
            [[1, 2, 0, 4], [5, 0, 7, 8], [9, 10, 11, 12]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [9, 0, 0, 12]],
        ),
        # 13. 4x1 with zero in second row
        ([[1], [0], [3], [4]], [[0], [0], [0], [0]]),
        # 14. 4x1 no zero
        ([[1], [2], [3], [4]], [[1], [2], [3], [4]]),
        # 15. 1x4 with zero at end
        ([[1, 2, 3, 0]], [[0, 0, 0, 0]]),
        # 16. 1x4 no zero
        ([[1, 2, 3, 4]], [[1, 2, 3, 4]]),
        # 17. 4x4 single zero top-left
        (
            [[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[0, 0, 0, 0], [0, 6, 7, 8], [0, 10, 11, 12], [0, 14, 15, 16]],
        ),
        # 18. 4x4 single zero bottom-right
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
            [[1, 2, 3, 0], [5, 6, 7, 0], [9, 10, 11, 0], [0, 0, 0, 0]],
        ),
        # 19. 4x4 zeros in one row
        (
            [[1, 2, 3, 4], [0, 0, 0, 0], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        ),
        # 20. 4x4 zeros in one column
        (
            [[1, 0, 3, 4], [5, 0, 7, 8], [9, 0, 11, 12], [13, 0, 15, 16]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        ),
        # 21. 5x5 diagonal zeros
        (
            [
                [0, 2, 3, 4, 5],
                [6, 0, 8, 9, 10],
                [11, 12, 0, 14, 15],
                [16, 17, 18, 0, 20],
                [21, 22, 23, 24, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        ),
        # 22. 5x3 zeros in first column
        (
            [[0, 2, 3], [0, 5, 6], [0, 8, 9], [0, 11, 12], [0, 14, 15]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        ),
        # 23. 6x6 no zero
        (
            [[i for i in range(j, j + 6)] for j in range(1, 37, 6)],
            [[i for i in range(j, j + 6)] for j in range(1, 37, 6)],
        ),
        # 24. 6x6 one zero in middle
        (
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 0, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
                [31, 32, 33, 34, 35, 36],
            ],
            [
                [1, 2, 0, 4, 5, 6],
                [7, 8, 0, 10, 11, 12],
                [13, 14, 0, 16, 17, 18],
                [0, 0, 0, 0, 0, 0],
                [25, 26, 0, 28, 29, 30],
                [31, 32, 0, 34, 35, 36],
            ],
        ),
        # 25. 3x3, zero at (0, 0)
        ([[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 0, 0], [0, 4, 5], [0, 7, 8]]),
        # 26. 3x3, zero at (2, 2)
        ([[1, 2, 3], [4, 5, 6], [7, 8, 0]], [[1, 2, 0], [4, 5, 0], [0, 0, 0]]),
        # 27. 2x4 zero in last column
        ([[1, 2, 3, 0], [5, 6, 7, 8]], [[0, 0, 0, 0], [5, 6, 7, 0]]),
        # 28. 4x2 zero in first row
        ([[0, 2], [3, 4], [5, 6], [7, 8]], [[0, 0], [0, 4], [0, 6], [0, 8]]),
        # 29. Edge: zeros on entire border
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        # 30. Edge: only one row, all zeros
        ([[0, 0, 0]], [[0, 0, 0]]),
        # 31. Edge: only one column, all zeros
        ([[0], [0], [0]], [[0], [0], [0]]),
        # 32. Large 10x10 all ones
        ([[1] * 10 for _ in range(10)], [[1] * 10 for _ in range(10)]),
        # 33. Large 10x10 one zero at (9,9)
        (
            [[1] * 10 for _ in range(9)] + [[1] * 9 + [0]],
            [[1] * 9 + [0] for _ in range(9)] + [[0] * 10],
        ),
        # 34. Large 10x10 one zero at (0,5)
        (
            [[1] * 5 + [0] + [1] * 4] + [[1] * 10 for _ in range(9)],
            [[0] * 10] + [[1] * 5 + [0] + [1] * 4 for _ in range(9)],
        ),
        # 35. Large 10x10 diagonal zeros
        (
            [[0 if i == j else 1 for j in range(10)] for i in range(10)],
            [[0] * 10 for _ in range(10)],
        ),
    ]

    # Create an instance of the problem subclass
    tester = ZeroMatrix()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    # report = tester.generate_report()
    # print("\nDetailed Test Report:\n")
    # print(report)
