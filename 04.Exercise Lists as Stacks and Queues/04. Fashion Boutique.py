cloths = list(map(int, input().split()))
capasity_rack = int(input())

curent_capasity = capasity_rack
stacks = []
quantity_rack = 1
counter = 0
while len(cloths) > 0:
    counter+=1
    curent_cloth = cloths.pop()
    if curent_cloth <= curent_capasity:
        curent_capasity -= curent_cloth
    else:
        quantity_rack += 1
        curent_capasity = capasity_rack
        curent_capasity -= curent_cloth

print(quantity_rack)