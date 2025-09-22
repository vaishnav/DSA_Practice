# Write a method to replace all spaces in a string with "%20" You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string. Use character array so that you can perform this operation in place. 

from tester import DSATest
from array import array

class Urifly(DSATest):
    def solution(self, s: array, lth: int):
        curr = lth-1
        full_length = len(s)-1
        while curr >= 0:
            if s[curr] == " ":
                s[full_length] = '0'
                s[full_length-1] = '2'
                s[full_length-2] = '%'
                full_length -= 3
            else:
                s[full_length] = s[curr]
                full_length -= 1
            curr -= 1
        return s
    
def prepare_char_array(input, result):
    # Count spaces in the true length part
    space_count = 0
    true_length = input[1]
    input_string = input[0]
    for i in range(true_length):
        if input_string[i] == ' ':
            space_count += 1

    # Create a char array from input string trimmed to true length
    char_array = array('u',[])
    char_array.extend(input_string)

    # Extend array with empty spaces to simulate buffer for in-place replacement
    char_array.extend([' '] * (space_count * 2))

    result_array = array('u',[])
    result_array.extend(result)

    return ((char_array, true_length), result_array)

if __name__ == "__main__":
    base_test_cases = [
        (("", 0), ""),
        ((" ", 1), "%20"),
        (("A", 1), "A"),
        (("  ", 2), "%20%20"),
        (("A B", 3), "A%20B"),
        (("Hello World", 11), "Hello%20World"),
        ((" a b ", 5), "%20a%20b%20"),
        ((" a  b ", 6), "%20a%20%20b%20"),
        (("a b c", 5), "a%20b%20c"),
        (("abc   ", 6), "abc%20%20%20"),
        (("  abc", 5), "%20%20abc"),
        (("abc def", 7), "abc%20def"),
        (("abc def ghi", 11), "abc%20def%20ghi"),
        (("a b c d e", 9), "a%20b%20c%20d%20e"),
        (("A  B  C", 7), "A%20%20B%20%20C"),
        (("  A  B  ", 8), "%20%20A%20%20B%20%20"),
        (("A B C D", 7), "A%20B%20C%20D"),
        (("A", 1), "A"),
        (("    ", 4), "%20%20%20%20"),
        (("TestCase", 8), "TestCase"),
        (("Test Case", 9), "Test%20Case"),
        (("Test Case ", 10), "Test%20Case%20"),
        (("Test  Case", 10), "Test%20%20Case"),
        ((" Test Case", 10), "%20Test%20Case"),
        (("  Leading", 9), "%20%20Leading"),
        (("TestCaseNoSpace", 15), "TestCaseNoSpace"),
        (("   ", 3), "%20%20%20"),
        (("A B  C D", 8), "A%20B%20%20C%20D"),
        (("  ", 2), "%20%20"),
        (("A    B", 6), "A%20%20%20%20B"),
        (("Space  Middle", 13), "Space%20%20Middle"),
        (("Middle Space", 12), "Middle%20Space"),
        (("M S", 3), "M%20S"),
        (("Multiple   Spaces", 17), "Multiple%20%20%20Spaces"),
        (("EndsWithSpace ", 14), "EndsWithSpace%20"),
        ((" ", 1), "%20"),
    ]

    test_cases = []
    for case in base_test_cases:
        test_cases.append(prepare_char_array(*case))

    # Create an instance of the problem subclass
    tester = Urifly()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    report = tester.generate_report()
    # print("\nDetailed Test Report:\n")
    # print(report)