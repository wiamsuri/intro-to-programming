# 3-Practice

def factorial(num):
    # TODO: Find factorial of num input
    # Code goes here
    return num

print('0! equals 1     Result: {}'.format(factorial(0)))
print('4! equals 24    Result: {}'.format(factorial(4)))
print('8! equals 40320 Result: {}'.format(factorial(8)))


input_word_list = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
def find_longest_word(word_list):
    # TODO: Find the longest word in the list
    # Code goes here
    return word_list[0]

print('Expected result "consectetur". Result: "{}"'.format(find_longest_word(input_word_list)))


def e():
    # TODO: Find the value of e (Euler's number)
    # hint: Sum of 1/n! from 0 to infinity
    # Code goes here
    return 2.7

print('Expected result 2.71828182846. Result: {}'.format(e()))
