# търсим файл
# try:
#     file = open('text.txt', 'r')
#     print("File found")
# except FileNotFoundError:
#     print('File not Found')

try:
    with open('text2.txt', 'x') as file:
        print('file open')
except FileNotFoundError:
    print('File not Found')
        