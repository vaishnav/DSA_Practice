# Given a string, write a function to check if if its is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

from tester import DSATest

class PalinPerm(DSATest):
    def solution(self, s: str):
        s = s.lower()
        char_count = {}
        for i in s:
            if i == " ":
                continue
            if i in char_count:
                if char_count[i] == 0:
                    char_count[i] += 1
                    continue
                char_count[i] -= 1
            else:
                char_count[i] = 1
        
        char_sum = 0
        for j in char_count:
            char_sum += char_count[j]
        
        if char_sum <= 1:
            return True
        
        return False
            

if __name__ == "__main__":
    test_cases = [
        ('', True),
        ('a', True),
        (' ', True),
        ('  ', True),
        ('Tact Coa', True),                   # Case insensitivity, phrase
        ('Able was I ere I saw Elba', True),  # Famous palindrome
        ('ab', False),
        ('aa', True),
        ('abc', False),
        ('aabb', True),
        ('aabbc', True),
        ('aabbcc', True),
        ('aabbccd', True),
        ('aabbccdd', True),
        ('aabbccdde', True),
        ('aabbccddee', True),
        ('abcd', False),
        ('abcde', False),
        ('A man, a plan, a canal: Panama', False),   # Punctuation
        ('Was it a car or a cat I saw?', False),
        ('!!!', True),                        # Only punctuation
        ('   ', True),                        # Only spaces
        ('1221', True),                       # Digits, even count
        ('12321', True),                      # Digits, odd count
        ('1234', False),
        ('RaceCar', True),
        ('No lemon, no melon', True),
        ('aabbccddeef', True),               # Two odd counts
        ('aabbccddeeffg', True),              # One odd count
        ('あいいあ', True),                    # Unicode palindrome
        ('あいえお', False),                   # Unicode, not a palindrome
        ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', True),            # All alphabet twice
        ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzx', True),           # All alphabet twice plus one
        ('abcdefg', False)                    # All unique, odd count
    ]


    # Create an instance of the problem subclass
    tester = PalinPerm()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
    print("\nDetailed Test Report:\n")
    print(report)