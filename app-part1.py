from os import system

DIR_UP = -1
DIR_STOPPED = 0
DIR_DOWN = 1

building_roof = True
building_floors = 9
building_parking = True

lift_floor = 3
lift_open = False
lift_dir = DIR_DOWN

human_floor = 3
human_in_lift = True

building_structure = '---|-------|----'


################### RENDER FRAME ###################
system("cls")

if building_roof:
    print(building_structure)
    print(' R |       |    ')
else:
    print(building_structure)

for floor in range(9, 0, -1):
    if floor == lift_floor - 1 or floor == lift_floor:
        b = '|-----|'
    else:
        b = '       '

    print(f'---|{b}|----')

    if floor == human_floor and not human_in_lift:
        h = ' H   '
    else:
        h = '      '

    if floor == lift_floor + 1:
        if lift_open:
            l = '  < >  '
        else:
            if lift_dir == DIR_UP:
                l = '   ^   '
            elif lift_dir == DIR_DOWN:
                l = '   v   '
            else:
                l = '       '
    else:
        l = '       '

    if floor == lift_floor and not human_in_lift:
        l = '|     |'
    elif floor == lift_floor and human_in_lift:
        l = '|  H  |'

    print(f"{floor:^3}|{l}|{h} ")

if building_parking:
    print('---|       |----')
    print(' P |       |    ')
    print(building_structure)
else:
    print(building_structure)


################### RENDER FRAME ###################
