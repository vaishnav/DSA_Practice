# Implement a method to perform basic string compression using the counts of repeadted character. For example, the string aabcccccaaa would become a2b1c5a3, 
# if the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only
# upper and lowercase letters (a-z)

from tester import DSATest

class StringCompression(DSATest):
    def solution(self, s: str):
        result = []
        if s == "":
            return ""
        
        curr_count = 1
        curr_char = s[0]
        for i in range(1, len(s)):
            if len(result) > len(s):
                return s
            if s[i] == curr_char:
                curr_count += 1
            else:
                result.append(curr_char)
                result.append(str(curr_count))
                curr_char = s[i]
                curr_count = 1

        result.append(curr_char)
        result.append(str(curr_count))

        if len(result) > len(s):
                return s
        return "".join(result)

        

if __name__ == "__main__":
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),          # example case
        ("abcdef", "abcdef"),                  # no repeated chars, returns original
        ("aaaaaa", "a6"),                      # all same chars
        ("aabbcc", "a2b2c2"),                  # each char appears twice
        ("a", "a"),                           # single character
        ("", ""),                            # empty string
        ("AaAaAa", "AaAaAa"),            # case sensitive
        ("bbbbbbbbb", "b9"),                  # long repetition
        ("abcdddeeefffggg", "a1b1c1d3e3f3g3"), # multiple repeats
        ("xyz", "xyz"),                       # all unique chars, no compression
        ("ppppqqqrrrssstt", "p4q3r3s3t2"),    # multiple chars with repeats
        ("zzzzzzzzzzzzzzzzzzzz", "z20"),     # very long single char
        ("aaaaaabbbbcccddde", "a6b4c3d3e1"), # mixed counts
        ("abcabcabc", "abcabcabc"),           # repeating patterns but not consecutive
        ("QwErTy", "QwErTy"),                 # mixed case no repeats
        ("TTTTTTTT", "T8"),                   # all uppercase, repeated
        ("aAaAaAaA", "aAaAaAaA"),     # alternating cases
        ("cccc", "c4"),                       # all same char
        ("abbcccddddeeeee", "a1b2c3d4e5"),    # increasing counts
        ("a"*50, "a50"),                      # very long repetitive string
        ("aabbaa", "a2b2a2"),                  # repetitive groups
        ("abababab", "abababab"),             # alternating chars no compression
        ("cccccbbbbaaa", "c5b4a3"),            # multiple large groups
        ("aabbccddeeff", "a2b2c2d2e2f2"),     # all pairs
        ("aabbccddeeffg", "aabbccddeeffg"),  # pairs with tail char
        ("a"*100 + "b"*100, "a100b100"),       # large counts two chars
        ("abcddcba", "abcddcba"),              # palindrome no compression
        ("mmmmnnnnooopppp", "m4n4o3p4"),       # mixed counts
        ("x"*3 + "y"*2 + "z"*4, "x3y2z4"),     # small groups
        ("AaBbCc", "AaBbCc"),                  # no repeats, mixed case
        ("eeeffffgggh", "e3f4g3h1"),           # mixed counts with tail char
        ("rrrsssuuuvvv", "r3s3u3v3"),          # groups of 3
        ("qqqwww", "q3w3"),                    # two groups of 3
        ("zzzyyyxxxwwwvvv", "z3y3x3w3v3"),     # multiple groups of 3
        ("abcdefghijklmnop", "abcdefghijklmnop") # long unique string
    ]


    # Create an instance of the problem subclass
    tester = StringCompression()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    # report = tester.generate_report()
    # print("\nDetailed Test Report:\n")
    # print(report)