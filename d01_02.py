"""
Docstring for d01_02
Reads a file containing rotation instructions and simulates spinning a point on a circular track of 100 positions.
It counts how many times the point traverses position zero after executing all rotations.

The get_new_position_and_traversals function takes a starting position and a rotation instruction (e.g., 'L10' or 'R20') and returns the new position 
along with the number of times zero was traversed.
travel is calculated by slicing the instruction string to get the numeric part and multiplying by -1 for left rotations and 1 for right rotations.
The count_passes function calculates how many times zero is traversed based on the starting position and total displacement.
Floor division is used to determine the number of full rotations, and the remainder is checked to see if it causes an additional traversal of zero.
As an example, if starting at position 95 and rotating right by 10, the point would move to position 5, traversing zero once.
Conversely, if starting at position 5 and rotating left by 10, the point would move to position 95, also traversing zero once, which is 
handled in the else block of count_passes.
"""

        
def count_passes(start_point:int, displacement:int) -> int:
    num_passes = 0
    num_full_rotations = abs(displacement) // 100
    remainder = abs(displacement) % 100
    if displacement > 0:
        if start_point + remainder >= 100:
            num_passes = num_full_rotations + 1
    else:
        if start_point != 0 and remainder >= start_point:
            num_passes = num_full_rotations + 1
    return num_passes
    

def get_new_position_and_traversals(initial_position, line):
    line = line.strip().upper()
    travel = int(line[1:]) * (-1 if line.startswith('L') else 1)
    final_position = (initial_position + travel) % 100
    traversals = count_passes(initial_position, travel)
    return final_position,traversals


if __name__ == "__main__":
    initial_position = 50
    total_traversed_zeros = 0
    rotation_file = "d01_01_input.txt"
    # Read rotations one line at a time
    with open(rotation_file, 'r') as f:
        for line in f:
            final_position, traversals = get_new_position_and_traversals(initial_position, line)
            total_traversed_zeros += traversals
            initial_position = final_position
    print(f"Number of times the rotation traversed zero: {total_traversed_zeros}")