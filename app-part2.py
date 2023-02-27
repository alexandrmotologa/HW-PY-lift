from time import sleep
import os

def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

DIRECTION_UP = -1
DIRECTION_STOPPED = 0
DIRECTION_DOWN = 1

building_roof = True
building_floors = 9
building_parking = True

lift_floor = 1
lift_open = True
lift_dir = DIRECTION_STOPPED
lift_target_floor = 1

human_floor = 6
human_in_lift = False

clear_console()
while True:
    if not human_in_lift:
        call_lift = input("Call the lift (y/n)? ").strip() == 'y'
    if call_lift:
        if not human_in_lift:
            lift_target_floor = human_floor
        else:
            try:
                lift_target_floor = int(input('Where to? ').strip())
            except ValueError:
                human_in_lift = False
                

    lift_open = False

    if lift_floor < lift_target_floor:
        speed = +1
        lift_dir = DIRECTION_UP
    if lift_floor > lift_target_floor:
        speed = -1
        lift_dir = DIRECTION_DOWN
    if lift_floor == lift_target_floor:
        speed = 0
        
    ################### ANIMATION ###################

    while True:
        lift_floor += speed

        if lift_floor == lift_target_floor:
            lift_open = True
            lift_dir = DIRECTION_STOPPED
            if not human_in_lift:
                human_in_lift = True
            else:
                
                human_in_lift = False
                human_floor = lift_target_floor

        ################### RENDER FRAME ###################
        clear_console()


        for floor in range(building_floors+1 if building_roof else building_floors+1, 0, -1):

            lift = '       '
            shaft = '       '
            human = ''
            if floor == lift_floor + 1:
                if lift_dir == DIRECTION_DOWN:
                    lift = '   v   '
                    if not human_in_lift and floor == human_floor:
                        human = "H"
                elif lift_dir == DIRECTION_UP:
                    lift = '   ^   '
                    if not human_in_lift and floor == human_floor:
                        human = "H"
                elif lift_dir == DIRECTION_STOPPED and lift_open:
                    lift = '  < >  '
                    if not human_in_lift and floor == human_floor:
                        human = "H"
            elif floor == lift_floor:
                lift = '|     |'
                shaft = '|-----|'
                if human_in_lift:
                    lift = '|  H  |'
                elif not human_in_lift and floor == human_floor:
                    lift = '|     |'
                    human = "H"
            elif floor == lift_floor - 1:
                shaft = '|-----|'
                if not human_in_lift and floor == human_floor:
                    human = "H"
            elif floor == human_floor:
                if not human_in_lift:
                    human = "H"

            
            if floor <= building_floors:
                print(f'---|{shaft}|----')
                print(f"{floor:^3}|{lift}|{human}")
            elif floor >= building_floors:
                if building_roof:
                    print('---|-------|----')
                    print(' R |       |    ')
                    print('---|-------|----')
                    print(f'---|{lift}|----')
                else:
                    print('---|-------|----')
                    print('---|-------|----')
                    print(f'---|{lift}|----')
                
        if building_parking:
            if floor == lift_floor:
                print('---||-----||----')
                print(' P |       |    ')
                print('---|-------|----')
            else:
                print('---|       |----')
                print(' P |       |    ')
                print('---|-------|----')
        else:
            if floor != lift_floor:
                print('---|-------|----')
            else:
                print('---||-----||----')

        sleep(1)
        if lift_floor == lift_target_floor:
            break
        ################### RENDER FRAME ###################
    ################### ANIMATION ###################
    sleep(.5)