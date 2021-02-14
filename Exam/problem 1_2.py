from collections import deque


def while_is_valid(firework_effects, explosive_power):
    if len(firework_effects) > 0 and len(explosive_power) == 0:
        return False
    elif len(firework_effects) == 0 and len(explosive_power) > 0:
        return False
    elif len(firework_effects) == 0 and len(explosive_power) == 0:
        return False
    return True


def determine_bomb_type(firework_effects, explosive_power, palm_firework, willow_firework, crossette_fireworks):
    firework_effect_item = firework_effects.popleft()
    explosive_power_item = explosive_power.pop()
    sum_of_items = firework_effect_item + explosive_power_item
    if sum_of_items % 3 == 0 and not sum_of_items % 5 == 0:
        palm_firework.append(1)
        return palm_firework
    elif sum_of_items % 5 == 0 and not sum_of_items % 3 == 0:
        willow_firework.append(1)
        return willow_firework
    elif sum_of_items % 5 == 0 and sum_of_items % 3 == 0:
        crossette_fireworks.append(1)
        return crossette_fireworks
    else:
        firework_effects.append(firework_effect_item - 1)
        explosive_power.append(explosive_power_item)
        firework_effects = deque([el for el in firework_effects if el > 0])
        explosive_power = [el for el in explosive_power if el > 0]

        return firework_effects, explosive_power


def pouch_full(palm_firework, willow_firework, crossette_firework):
    if len(palm_firework) >= 3 and len(willow_firework) >= 3 and len(crossette_firework) >= 3:
        return True
    return False


def print_result(*args):
    if pouch_full(palm_firework, willow_firework, crossette_firework):
        print('Congrats! You made the perfect firework show!')
    else:
        print("Sorry. You can’t make the perfect firework show.")

    if firework_effects:
        print(f'Firework Effects left: {", ".join([str(el) for el in firework_effects])}')
    if explosive_power:
        print(f'Explosive Power left: {", ".join([str(el) for el in explosive_power])}')

    print(f'Palm Fireworks: {len(palm_firework)}')
    print(f'Willow Fireworks: {len(willow_firework)}')
    print(f'Crossette Fireworks: {len(crossette_firework)}')


firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]
firework_effects = deque([el for el in firework_effects if el > 0])
explosive_power = [el for el in explosive_power if el > 0]

palm_firework = []
willow_firework = []
crossette_firework = []

while while_is_valid(firework_effects, explosive_power) and not pouch_full(palm_firework, willow_firework,
                                                                           crossette_firework):
    determine_bomb_type(firework_effects, explosive_power, palm_firework, willow_firework, crossette_firework)

print_result(firework_effects, explosive_power, palm_firework, willow_firework, crossette_firework)