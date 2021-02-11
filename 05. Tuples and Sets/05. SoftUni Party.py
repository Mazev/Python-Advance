def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)


guest_count = int(input())
arrived = input()
reservations = input_to_list(guest_count)
guest_arrived = input_to_list_until_command(arrived)
guest_not_arrived = set(reservations).difference(guest_arrived)

# print(len(reservation))
# sorted_list_guest = sorted(reservation)
# for i in sorted_list_guest:
#     print(i)
