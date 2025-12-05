


# function to read a file of comma-separated values and return a list of strings
def read_csv_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        content = f.read()
    return [item.strip() for item in content.split(',')]

# function to take a string that represents two integers separated by a hyphen and return the two integers as a tuple
def parse_hyphenated_integers(hyphenated_str: str) -> tuple:
    parts = hyphenated_str.split('-')
    return (int(parts[0].strip()), int(parts[1].strip()))


def is_repeated(n: int) -> bool:
    s = str(n)
    if len(s) <= 1:
        return False
    return s in (s + s)[1:-1] if len(s) > 1 else False

def is_double(n: int) -> bool:
    s = str(n)
    l = len(s)
    
    if l < 2 or l%2 != 0:
        return False
    
    half = l//2
    first, second = s[:half], s[half:]
    if first != second:
        return False
    return True


def repeated_sequences(a: int, b: int) -> list:
    lo, hi = (a, b) if a <= b else (b, a)
    return [i for i in range(lo, hi + 1) if is_repeated(i)]
    


if __name__ == "__main__":
    csv_file = "d02_01_input.txt"
    
    csv_values = read_csv_file(csv_f
    idsum = 0
    
    for element in csv_values:
        int_tuple = parse_hyphenated_integers(element)
        repeated_nums = repeated_sequences(int_tuple[0], int_tuple[1])
        print(f"Repeated sequences between {int_tuple[0]} and {int_tuple[1]}: {repeated_nums}")
        idsum += sum(repeated_nums)
        
    print(f"Total sum of repeated sequences: {idsum}")

            

        
        
        
