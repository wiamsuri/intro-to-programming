# Functions


def square(number):
    # TODO: Write a function that returns the square of a number
    # Code goes here
    return number

print('1. )')
print('square of 1 is 1     Result: {}'.format(square(1)))
print('square of 4 is 16    Result: {}'.format(square(4)))
print('square of 10 is 100  Result: {}'.format(square(10)))
print('square of 9 is 81    Result: {}'.format(square(9)))


def average(number_list):
    # TODO: Write a function that returns the average of the number list input
    # Code goes here
    return number_list[0]

print('2. )')
print('average 2, 3    is 2.5      Result: {}'.format(average([2.0, 3.0])))
print('average 4, 5, 7 is 5.333333 Result: {}'.format(average([4.0, 5.0, 7.0])))
print('average 0, 2, 5 is 2.333333 Result: {}'.format(average([0.0, 2.0, 5.0])))


# TODO: Write a function that find the largest number in the input list
# Code goes here

print('3. )')
try:
    print('max of 2, 3, 8    is 8     Result: {}'.format(find_max([2, 3, 8])))
    print('max of 10, 42, 2  is 42    Result: {}'.format(find_max([10, 42, 2])))
    print('max of 31, 4, 5   is 31    Result: {}'.format(find_max([31, 4, 5])))
except NameError:
    print('The function "find_max" is not defined')
