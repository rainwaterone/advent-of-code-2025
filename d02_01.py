
"""
For the first assignment, we are scanning each range to find any instances where a sequence of digits is repeated exactly once.
For example, in the range 998 to 1200, you have 1010 and 1111, but you don't have 999 because the digit 9 is not repeated exactly once.

Since we have these ranges in a CSV file, I wrote a helper function to read the CSV file and return a list of strings.
Then, for each string in the list, I have another helper function that takes a hyphenated string and returns a tuple of two integers.

Then, I have the repeated_sequences function that takes the two integers and goes through the range represented by those two integers,
checking them against the is_double or is_repeated functions to see if they meet the criteria.

For the first exercise, I used the is_double function to check if the number has a sequence of digits that is repeated exactly once.
It does this by converting the number to a string, checking if the length is even, and then splitting the string in half.
If the two halves are the same, it returns True; otherwise, it returns False.

For the second exercise, I used the is_repeated function to check if the number has any sequence of digits that is repeated exactly once.
It does this by converting the number to a string and checking if the string is found in itself when concatenated with itself, excluding 
the first and last characters.
As an example, 1212 is concatenated to 12121212, and when you exclude the first and last characters, you get 2121212, which contains 1212.
The reason we remove the first and last characters is to avoid counting the original string itself.

"""

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
    
    csv_values = read_csv_file(csv_file)
    idsum = 0
    
    for element in csv_values:
        int_tuple = parse_hyphenated_integers(element)
        repeated_nums = repeated_sequences(int_tuple[0], int_tuple[1])
        print(f"Repeated sequences between {int_tuple[0]} and {int_tuple[1]}: {repeated_nums}")
        idsum += sum(repeated_nums)
        
    print(f"Total sum of repeated sequences: {idsum}")

            

        
        
        
