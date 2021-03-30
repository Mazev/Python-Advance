# def even_num(iter):
#     return (filter(lambda x: x % 2 == 0, iter))
#
#
# num = map(int, input().split())
# print(list(even_num(num)))


# def sortet_num(iter):
#     return list(sorted(iter , key= lambda x: x))
#
#
# num = map(int, input().split())
# print(sortet_num(num))


# def min_max_sum_num(iter):
#     min_num = min(iter)
#     max_num = max(iter)
#     sum_num = sum(iter)
#     return min_num, max_num, sum_num
#
#
# def print_result(min_num, max_num, sum_num):
#     print(f'The minimum number is {min_num}')
#     print(f'The maximum number is {max_num}')
#     print(f'The sum number is: {sum_num}')
#
#
# num = list(map(int, input().split()))
# min_num, max_num, sum_num = min_max_sum_num(num)
# print_result(min_num, max_num, sum_num)


# def print_stronger_sum_num(nums):
#     positive_sum = sum(filter(lambda x: x > 0, nums))
#     negative_sum = sum(filter(lambda x: x < 0, nums))
#     print(negative_sum, positive_sum, sep='\n')
#     if positive_sum > abs(negative_sum):
#         print(f'The positives are stronger than the negatives')
#     else:
#         print(f'The negatives are stronger than the positives')
#
#
# num = list(map(int, input().split()))
# print_stronger_sum_num(num)

#
# def concatenate(*text):
#     concatenate_text = ''
#     for el in text:
#         concatenate_text += el
#     return concatenate_text
#
#
#
# print(concatenate("Soft", "Uni", "Is", "Great", "!"))


# def get_command_nums(command, args):
#     if command == 'Odd':
#         return [s for s in args if s % 2 != 0]
#     else:
#         return [s for s in args if s % 2 == 0]
#
#
# def print_result(filtret_nums, numbers):
#     print(sum(filtret_nums) * len(numbers))
#
#
# command = input()
# numbers = list(map(int, input().split()))
# filtret_nums = get_command_nums(command, numbers)
# print_result(filtret_nums, numbers)

# def args_length(*args):
#     return len(args)
#
#
# print(args_length(1, 32, 5))
# print(args_length("john", "peter"))
# print(args_length([1, 2, 3]))


# def even_odd(*args):
#     inputs = [el for el in args]
#     command = inputs.pop()
#     result = []
#     if command == 'even':
#         for el in inputs:
#             if el % 2 == 0:
#                 result.append(el)
#     else:
#         for el in inputs:
#             if el % 2 == 1:
#                 result.append(el)
#     return result
#
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# def func_executor(*args):
#     result = []
#     for func_name, data in args:
#         res = func_name(*data)
#         result.append(res)
#     return result
#
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
# dictionary = {'name': 'Peter', 'age': 25}
#
# print(kwargs_length(**dictionary))


# def age_assignment(*names, **kwargs):
#     assignment = {}
#     for name in names:
#         for letter, age in kwargs.items():
#             if name.startswith(letter):
#                 assignment[name] = age
#     return assignment
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# def recursive_power(*args):
#     number = int(args[0])
#     power = int(args[1])
#     if power == 1:
#         return number
#     return number * recursive_power(number, power - 1)
#
#
# print(recursive_power(2, 10))
# print(recursive_power(10, 100))


def palindrome(word, index=0, left_index=-1):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] == word[left_index]:
        return palindrome(word, index + 1, left_index - 1)

    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))