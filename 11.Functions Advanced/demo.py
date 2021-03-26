# def convert_iterable_to_absolute(num_list):
#     result = [abs(el) for el in num_list]
#     return result
#
#
# num = [float(el) for el in input().split()]
#
# print(convert_iterable_to_absolute(num))

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{value}, {key}')
#
#
# greet_me(Peter='Hello', Ivan='Bye')


# def some_func(arg1, *rest_arg):
#     print(arg1 + sum(rest_arg))
#
#
# some_func(5 , 5 , 10)


# staks

# def say_hello_n_time(times):
#     if times == 0:
#         return
#     print('Hello')
#     say_hello_n_time(times - 1)
#
#
# say_hello_n_time(5)