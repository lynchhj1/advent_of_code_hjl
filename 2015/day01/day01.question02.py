line_sum=0
file = open('input', 'r')
lines = file.readlines()
for line in lines:
    floors_up=0
    floors_down=0
    current_floor=0
    current_character=0
    for c in line:
        current_character=current_character+1
        if c=='(':
            current_floor=current_floor+1
        else:
            current_floor=current_floor-1
        if current_floor==-1:
            print(current_character)
            break
