# Assume you have a method isSubstring which checks if one word is a substring of another. Given two string s1 and s2 write code to check if if s2 is rotation of s1,
# using only one call to isSubstring. 
from tester import DSATest

class StringRotation(DSATest):
    def isSubstring(self, s1: str, s2: str):
        return s1 in s2

    def solution(self, s1: str, s2: str):
        # When we rotate the string we do it around a point and lets say we divide the string in 2 parts one is x and other is y
        # if the string is xy then its rotation would be yx, so if we join xy and xy we will get xyxy which also contains yx as its substring
        if len(s1) != len(s2):
            return False
        return self.isSubstring(s2, s1+s1)


if __name__ == "__main__":
    test_cases = [
        (("", ""), True),  # Both strings empty
        (("", "a"), False),  # One empty, one non-empty
        (("abcde", "deabc"), True),  # Standard rotation
        (("abcde", "eabcd"), True),  # Last char rotated to front
        (("abcde", "cdeab"), True),  # Rotated by 2
        (("aa", "aa"), True),  # Same repeated char
        (("abcdef", "abcdef"), True),  # No rotation, same string
        (("abcd", "dabc"), True),  # Rotated by 1
        (("waterbottle", "erbottlewat"), True),  # Example in books
        (("rotation", "tionrota"), True),  # Rotated by 4
        (("abc", "cab"), True),  # Rotated by 2
        (("abc", "bca"), True),  # Rotated by 1
        (("abc", "abc"), True),  # Same string
        (("abc", "bac"), False),  # Not a rotation
        (("abcde", "edabc"), False),  # Wrong order
        (("a", "a"), True),  # Single char same
        (("a", "b"), False),  # Single char different
        (("abcde", "abcdf"), False),  # Same length, totally different
        (("abcde", ""), False),  # s2 empty
        (("", "abcde"), False),  # s1 empty
        (("abcde", "abcd"), False),  # s2 shorter
        (("abcd", "abcde"), False),  # s2 longer
        (("ab", "ba"), True),  # Rotated by 1
        (("ab", "ab"), True),  # Same string
        (("ab", "bb"), False),  # Wrong content
        (("aaba", "abaa"), True),  # Palindrome rotation
        (("aaaa", "aaaa"), True),  # All chars same
        (("abcdabcd", "cdabcdab"), True),  # Larger rotation
        (("abcd", "bcda"), True),  # Rotated by 2
        (("abcd", "acbd"), False),  # Not a rotation
        (("ba", "ab"), True),  # Rotated by 1 reverse
        (("rotation", "onrotati"), True),  # Rotated by 6
        (("rotation", "otationr"), True),  # Rotated by 1
        (("rotation", "noitatior"), False),  # Reverse and more chars - not rotation
        (("rotation", "rotatino"), False),  # Typo string
    ]


    # Create an instance of the problem subclass
    tester = StringRotation()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)