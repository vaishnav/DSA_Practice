# Given a string, write a function to check if if its is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

from tester import DSATest

# This solution ignores spaces, and assumes that all the input are a lower case alphabets, and won't work in other cases
class PalinPerm(DSATest):
    def solution(self, s: str):
        # Initialize bitmask checker to track character counts using bits.
        # Each bit represents whether a character ('a' to 'z') currently appears an odd or even number of times.
        checker = 0
        for char in s:
            # Map 'a' to 0, 'b' to 1, ..., 'z' to 25.
            if char != " ":
                val = ord(char) - ord('a')
                # Toggle the bit at position 'val'.
                # This means we flip the bit each time the character appears:
                # - Even count: bit resets to 0
                # - Odd count: bit ends up as 1
                checker ^= (1 << val)
        
        # After processing all characters, checker’s bits:
        # - 0 means all characters appeared an even number of times.
        # For a valid palindrome permutation, at most one character can have an odd count.    
        # If only one character has odd count that means only one bit is flipped eg 00001000
        # if we subtract one from that we would get 00000111 but that won't be true if multiple bits are flipped 
        # so we first subtract by 1 then we do "and" with original value, that would give us 0 in case of only 1 bit is flipped
        return (checker & (checker - 1)) == 0

if __name__ == "__main__":
    test_cases = [
        ("", True),
        ("a", True),
        ("tact coa", True),
        ("able was i ere i saw elba", True),
        ("ab", False),
        ("aa", True),
        ("abc", False),
        ("aabb", True),
        ("aabbc", True),
        ("aabbcc", True),
        ("aabbccd", True),
        ("aabbccdd", True),
        ("aabbccdde", True),
        ("aabbccddee", True),
        ("abcd", False),
        ("abcde", False),
        ("no lemon no melon", True),
        ("aabbccddeef", True),
        ("aabbccddeeffg", True),
        ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzx", True),
        ("abcdefg", False),
    ]

    test_cases = [(case[0].lower(), case[1]) for case in test_cases]
    print(test_cases)

    # Create an instance of the problem subclass
    tester = PalinPerm()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
    # print("\nDetailed Test Report:\n")
    # print(report)
