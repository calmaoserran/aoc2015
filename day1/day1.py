#!/usr/bin/python3

# Read input file into string
file_name = 'input'
input = [line.rstrip() for line in open(file_name)][0]

def calculate_final_floor(movements: list) -> int:
    """
    Returns the outcome floor after following the instructions in the movements
    """
    return movements.count('(') - movements.count(')')

def find_basement_move(movements: list) -> int:
    """
    Returns the index of the movement that brings santa to the basement (floor -1)
    """
    floor = 0
    for idx,movement in enumerate(movements,start=1):
        # Go down
        if movement == ')':
            # If floor is 0 and we are going down we have found the movement index 
            if floor == 0:
                return idx
            floor -=1
        # Else go up
        else:
            floor +=1

if __name__ == "__main__":
    print(f'Challenge 1 solution: {calculate_final_floor(input)}')
    print(f'Challenge 2 solution: {find_basement_move(input)}')