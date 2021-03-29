import os


def create_file(file_path):
    with open(file_path, "w") as file:
        file.write()


def add_content_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content + "\n")


def replace_content_file(file_path, content, replece_with):
    with open(file_path, "r+") as file:
        text = ''.join(file.readlines())
        replece_content = text.replace(content, replece_with)
        file.seek(0)
        file.writelines(replece_content)


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")


actioner = {
    "Create": create_file,
    "Add": add_content_to_file,
    "Replace": replace_content_file,
    "Delete": delete_file
        }


def strat_engen():
    command_data = input().split("-")
    while not command_data == "End":
        command, command_data = command_data[0], command_data[1:]
        actioner[command](*command_data)
        command_data = input()
# create_file("my_text.txt")
# add_content_to_file("my_text.txt", "there")
# replace_content_file("my_text.txt", "command", "@@@@@@@@@@@@@@@")


strat_engen()