# Given an image represented by NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees, can you do this in place ?
from tester import DSATest


class RotateMatrix(DSATest):
    def solution(self, arr: list):
        # Initialize pointers to represent the current layer (outermost to innermost)
        left = 0
        right = len(arr) - 1
        
        # Process each layer of the matrix, moving inwards
        while left < right:
            # For each position in the current layer, cycle the values of four corresponding cells
            for i in range(right - left):
                top, bottom = left, right
                
                # Store the top-left position value temporarily
                temp = arr[left][top + i]

                # Move value from bottom-left to top-left
                arr[left][top + i] = arr[bottom - i][left]

                # Move value from bottom-right to bottom-left
                arr[bottom - i][left] = arr[bottom][right - i]

                # Move value from top-right to bottom-right
                arr[bottom][right - i] = arr[top + i][right]

                # Assign temp (top-left original) to top-right
                arr[top + i][right] = temp
            
            # Move pointers inwards to the next inner layer
            left += 1
            right -= 1

        # Matrix has been rotated in-place; return the result
        return arr




if __name__ == "__main__":
    test_cases = [
        # 1x1: smallest case
        ([[1]], [[1]]),
        # 2x2: basic rotation
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        # 3x3: odd size
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        # 4x4: unique numbers
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]],
        ),
        # 5x5: all zero
        (
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        ),
        # 5x5: increasing by row
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
        # 6x6: identical elements
        ([[1] * 6 for _ in range(6)], [[1] * 6 for _ in range(6)]),
        # 6x6: diagonal different
        (
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
                [31, 32, 33, 34, 35, 36],
            ],
            [
                [31, 25, 19, 13, 7, 1],
                [32, 26, 20, 14, 8, 2],
                [33, 27, 21, 15, 9, 3],
                [34, 28, 22, 16, 10, 4],
                [35, 29, 23, 17, 11, 5],
                [36, 30, 24, 18, 12, 6],
            ],
        ),
        # Non-sequential, 3x3
        ([[5, 9, 2], [8, 0, 15], [22, 8, 3]], [[22, 8, 5], [8, 0, 9], [3, 15, 2]]),
        # Negative numbers, 3x3
        (
            [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
            [[-7, -4, -1], [-8, -5, -2], [-9, -6, -3]],
        ),
        # Large negative values, 2x2
        ([[-1000, 2000], [1500, -2500]], [[1500, -1000], [-2500, 2000]]),
        # Mixed types, 2x2
        ([[1.5, 2], [3, 4.0]], [[3, 1.5], [4.0, 2]]),
        # All ones, 7x7
        ([[1] * 7 for _ in range(7)], [[1] * 7 for _ in range(7)]),
        # Custom pattern, 4x4
        (
            [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0], [1, 0, 0, 1]],
            [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]],
        ),
        # 2x2: Single change
        ([[9, 2], [4, 7]], [[4, 9], [7, 2]]),
        # All max int, 3x3
        ([[2147483647] * 3 for _ in range(3)], [[2147483647] * 3 for _ in range(3)]),
        # All min int, 3x3
        ([[-2147483648] * 3 for _ in range(3)], [[-2147483648] * 3 for _ in range(3)]),
        # 1x1: Large number
        ([[99999999]], [[99999999]]),
        # Even and odd edge, 8x8
        (
            [
                [1, 2, 3, 4, 5, 6, 7, 8],
                [9, 10, 11, 12, 13, 14, 15, 16],
                [17, 18, 19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30, 31, 32],
                [33, 34, 35, 36, 37, 38, 39, 40],
                [41, 42, 43, 44, 45, 46, 47, 48],
                [49, 50, 51, 52, 53, 54, 55, 56],
                [57, 58, 59, 60, 61, 62, 63, 64],
            ],
            [
                [57, 49, 41, 33, 25, 17, 9, 1],
                [58, 50, 42, 34, 26, 18, 10, 2],
                [59, 51, 43, 35, 27, 19, 11, 3],
                [60, 52, 44, 36, 28, 20, 12, 4],
                [61, 53, 45, 37, 29, 21, 13, 5],
                [62, 54, 46, 38, 30, 22, 14, 6],
                [63, 55, 47, 39, 31, 23, 15, 7],
                [64, 56, 48, 40, 32, 24, 16, 8],
            ],
        ),
        # 1x1: String pixel
        ([["pixel"]], [["pixel"]]),
        # All same but one, 3x3
        ([[2, 2, 2], [2, 0, 2], [2, 2, 2]], [[2, 2, 2], [2, 0, 2], [2, 2, 2]]),
        # Middle non-zero, 3x3
        ([[0, 0, 0], [0, 5, 0], [0, 0, 0]], [[0, 0, 0], [0, 5, 0], [0, 0, 0]]),
        # Checkerboard pattern, 4x4
        (
            [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]],
            [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]],
        ),
        # 3x3: Center fixed
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        # Repeated rotations: after 4 should be same
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        # 2x2: Float values
        ([[1.1, 2.2], [3.3, 4.4]], [[3.3, 1.1], [4.4, 2.2]]),
        # 3x3: All negatives
        (
            [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
            [[-7, -4, -1], [-8, -5, -2], [-9, -6, -3]],
        ),
        # 1x1: Zero
        ([[0]], [[0]]),
        # 8x8: All zeroes
        ([[0] * 8 for _ in range(8)], [[0] * 8 for _ in range(8)]),
        # 5x5: First row all one, others zero
        (
            [
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
            ],
        ),
        # Identity matrix 3x3
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[0, 0, 1], [0, 1, 0], [1, 0, 0]]),
        # Reverse sequential, 4x4
        (
            [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]],
            [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]],
        ),
        # Alternating pattern 3x3
        ([[1, 2, 1], [2, 1, 2], [1, 2, 1]], [[1, 2, 1], [2, 1, 2], [1, 2, 1]]),
        # 2x2: All float zeros
        ([[0.0, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0]]),
        # 3x3: Mix int and float
        (
            [[1, 2.5, 3], [4, 5, 6.7], [7.2, 8, 9]],
            [[7.2, 4, 1], [8, 5, 2.5], [9, 6.7, 3]],
        ),
    ]

    # Create an instance of the problem subclass
    tester = RotateMatrix()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)
