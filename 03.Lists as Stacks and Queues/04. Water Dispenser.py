from collections import deque

quantity = int(input())

names_queues = deque()
REFILL_COMMAND = 'refill'
while True:
    command = input()
    if command == 'Start':
        break
    names_queues.append(command)

while True:
    command = input()
    if command == 'End':
        print(f'{quantity} liters left')
        break
    if command.startswith(REFILL_COMMAND):
        command_tokens = command.split()
        refill_liters = int(command_tokens[1])
        quantity += refill_liters
    else:
        person = names_queues.popleft()
        person_liters = int(command)
        if person_liters <= quantity:
            quantity -= person_liters
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
