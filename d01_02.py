
        
def count_passes(start_point:int, displacement:int) -> int:
    num_full_rotations = abs(displacement) // 100
    remainder = abs(displacement) % 100
    if displacement > 0:
        if start_point + remainder >= 100:
            num_full_rotations += 1
    else:
        if start_point != 0 and remainder >= start_point:
            num_full_rotations += 1
    return num_full_rotations
    

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