# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character of the final pair
# with an underscore ('_').

def solution(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i:i+2] for i in range(0, len(s), 2)]





# The goal of this exercise is to convert a string to a new string where each character in the new string
# is "(" if that character appears only once in the original string, or ")"
# if that character appears more than once in the original string. Ignore capitalization when determining
# if a character is a duplicate.
# Examples
#
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def duplicate_encode(word):
    word_lower = word.lower()
    char_count = {}
    for char in word_lower:
        char_count[char] = char_count.get(char, 0) + 1
    result = ''.join('(' if char_count[char] == 1 else ')' for char in word_lower)

    return result
