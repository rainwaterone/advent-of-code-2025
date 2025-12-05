

def spin(start:int, rotate:str) -> int:
    rotate = rotate.strip().upper()
    if rotate.startswith('L'):
        direction = -1
    else:
        direction = 1
    displacement = int(rotate[1:])*direction
    return (start + displacement) % 100
        
if __name__ == "__main__":
    start_point = 50
    rotation_file = "d01_01_input.txt"
    zeros = 0
    # Read rotations one line at a time
    with open(rotation_file, 'r') as f:
        for line in f:
            start_point = spin(start_point, line)
            if start_point == 0:
                zeros += 1
    print(f"Number of times the rotation landed on zero: {zeros}")