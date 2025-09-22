# Given two strings, write a method to decide if one is a permutation of the other
from tester import DSATest

class CheckPermutations(DSATest):
    def solution(self, s1: str, s2: str):
        if len(s1) != len(s2):
            return False
        
        s1_chars = {}
        for i in s1:
            if i not in s1_chars:
                s1_chars[i] = 1
            else:
                s1_chars[i] += 1

        for j in s2:
            if j not in s1_chars:
                return False
            else:
                s1_chars[j] -= 1
                if s1_chars[j] < 0:
                    return False
        return True
    

if __name__ == "__main__":
    test_cases = [
        (("abc", "cba"), True),
        (("abcd", "dcba"), True),
        (("aabbcc", "baccab"), True),
        (("hello", "olleh"), True),
        (("test", "tset"), True),
        (("python", "typhon"), True),
        (("silent", "listen"), True),
        (("aaa", "aaa"), True),
        (("racecar", "carrace"), True),
        (("abc", "def"), False),
        (("abcd", "abcde"), False),
        (("abc", "abb"), False),
        (("abcd", "abce"), False),
        (("Hello", "hello"), False),  # case-sensitive
        (("123", "321"), True),
        (("112233", "332211"), True),
        (("!@#", "#@!"), True),
        (("abc ", "cab"), False),     # extra space
        (("spaces", "spcaes"), True),
        (("longerstring", "gnirtsregnol"), True),
        # Edge cases
        (("", ""), True),             # both empty
        (("a", "a"), True),           # single identical char
        (("a", "b"), False),          # single different char
        (("", "a"), False),           # one empty, one not
        ((" ", " "), True),           # whitespace vs whitespace
        (("  ", " "), False),         # double space vs single space
        (("Aa", "aA"), True),         # case-sensitive but still permutation
        (("aaa ", " aaaa"), False),   # different lengths with space
        (("permutation", "mutationper"), True),
        (("repeatedletters", "lettersrepeated"), True)
    ]


    # Create an instance of the problem subclass
    tester = CheckPermutations()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
    print("\nDetailed Test Report:\n")
    print(report)
