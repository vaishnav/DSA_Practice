# There are three thypes of edits that can be performed on string: 
# insert a character. remove a character, or replace a character. Given two string, write a function to check if they are one edit (or zero edits) away
from tester import DSATest

class OneAway(DSATest):
    def solution(self, str1: str, str2):
        # If lenght difference is greate than 1 then more than edits would be needed
        if abs(len(str1)-len(str2)) > 1:
            return False
        
        # Find longer string
        min_string = str1
        max_string = str2
        
        if len(max_string) < len(min_string):
            max_string = str2
            min_string = str1
        
        # parse thorough both the strings at same time
        length = len(max_string)
        i = 0
        j = 0
        diff_found = False
        while i < length:
            # if we've  reached the end of smaller string without any difference than we can return true anyway
            if length - j == 1:
                return True
            # check if elements in two strings are same of not, if not then we can register one edit required
            # and in case two strings have different lengths, then we will move one step extra on longer string.
            if min_string[j] != max_string[i]:
                if diff_found:
                    return False
                diff_found = True
                if len(min_string) < length:
                    i += 1
                    continue
                
            i += 1
            j += 1
            
        return True
        

if __name__ == "__main__":
    test_cases = [
        (('abc', 'abc'), True),
        (('a', 'a'), True),
        (('', ''), True),
        (('abc', 'abdc'), True),
        (('abc', 'abcd'), True),
        (('', 'a'), True),
        (('a', ''), True),
        (('abcd', 'abc'), True),
        (('a', ''), True),
        (('abc', 'abx'), True),
        (('abc', 'xbc'), True),
        (('abc', 'axc'), True),
        (('abc', 'axyd'), False),
        (('abc', 'ab'), True),
        (('abc', 'axcdef'), False),
        (('', 'abc'), False),
        (('abc', ''), False),
        (('a', 'b'), True),
        (('a', ''), True),
        (('', 'a'), True),
        (('abc', 'Abc'), True),
        (('abc', 'ABC'), False),
        (('kitten', 'sitten'), True),
        (('kitten', 'kittne'), True),
        (('kitten', 'kittens'), True),
        (('kitten', 'kiten'), True),
        (('kitten', 'sittin'), False),
        (('kitten', 'kittenss'), False),
        (('kitten', 'kitt'), False),
        (('', 'a'), True),
        (('a', ''), True),
        (('', 'ab'), False),
        (('ab', ''), False)
    ]


    # Create an instance of the problem subclass
    tester = OneAway()

    # Run the tests with performance reporting enabled
    results = tester.run_tests(test_cases, show_performance=True)

    # Print a detailed report
    # report = tester.generate_report()
    # print("\nDetailed Test Report:\n")
    # print(report)
