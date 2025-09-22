# Implement an algorithm to determine if a string has all unique characters, What if you cannot use additional data structures ?
from tester import DSATest

class UniqueCharsBitwise(DSATest):
    # The suggested solution uses a bit vector (an integer as a bitmask) to track the presence of characters, 
    # assuming the string consists of only lowercase letters 'a' through 'z'. 
    # Each bit in the integer corresponds to a letter. This allows checking and setting flags in constant time and uses minimal extra space.
    def solution(self, s: str):
        checker = 0  # Integer used as bit vector to track characters
        for char in s:
            val = ord(char) - ord('a')  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25
            if (checker & (1 << val)) > 0:
                # Bit already set, character repeated
                return False
            checker |= (1 << val)  # Set the bit for this character
        return True
    


if __name__ == "__main__":
    test_cases = [
        ("", True),                       # Empty string
        ("a", True),                      # Single character
        ("abcdefg", True),                # All unique
        ("hello", False),                 # Duplicate 'l'
        ("aa", False),                     
        ("abcdefghijklmnopaqrstuvwxyza", False),  # Duplicate 'A'
        ("hithere", False),              # Duplicate 'h' and space
        # ("1234567890", True),             # All unique digits
    ]


    # Create an instance of the problem subclass
    tester = UniqueCharsBitwise()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)
