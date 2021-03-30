#  търсим файл
# try:
#     file = open('text.txt', 'r')
#     print("File found")
# except FileNotFoundError:
#     print('File not Found')

try:
    file = open('numbers.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('File not Found')