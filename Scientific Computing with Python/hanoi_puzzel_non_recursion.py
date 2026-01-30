NUMBER_OF_DISKS = 4
number_of_moves = 2 ** NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}

def make_allowed_move(rod1, rod2):    
    move_forward = False
    if not rods[rod2]:
        move_forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        move_forward = True
    if move_forward:
        rods[rod2].append(rods[rod1].pop())
    else:
        rods[rod1].append(rods[rod2].pop())
  
    print(rods, '\n')

def move(n, source, auxiliary, target):

    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        if remainder == 1:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)
                

move(NUMBER_OF_DISKS, 'A', 'B', 'C')