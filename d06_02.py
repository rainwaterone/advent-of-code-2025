

def nonspace_indices(s: str) -> list[int]:
    return [i for i, ch in enumerate(s) if ch != ' ']


def split_by_indices(s: str, indices: list[int]) -> list[str]:
    parts = []
    for i in range(len(indices) - 1):
        start = indices[i]
        end = indices[i + 1]
        parts.append(s[start:end-1])
    # Add final segment from the last index to the end of the string
    parts.append(s[indices[-1]:])
    return parts


def perform_operation(op: str, numbers: list[float]) -> float:
    if op == "+":
        return sum(numbers)
    elif op == "*":
        return prod(numbers)
    else:
        raise ValueError("Operator must be a '+' or a '*'")
    
    
def str_to_num(numstr: str) -> int | float:
    try:
        return int(numstr)
    except ValueError:
        try:
            return float(numstr)
        except ValueError:
            print(f"Valid number not found in {numstr}")
        

def read_file(input_file: str) -> dict[int, str]:
    f_dict = {}
    with open(input_file, 'r') as f:
        for i, line in enumerate(f):
            line = line.replace('\n', '')
            f_dict[i] = line
    return f_dict


def check_data_length(file_dict: dict[int, list[str]]) -> int:
    values = file_dict.values()
    data_len = len(next(iter(values)))  # gets the length of the first value
    check_length = all(len(v) == data_len for v in values)
    print(f"Each line has the same numer of values or operators? {check_length}")
    if check_length:
        print(f"Number of operations: {len(file_dict[-1:])}")
    return data_len


def sum_all_operations(perform_operation, str_to_num, file_dict, first_len):
    sumlist = 0
    op_list = file_dict[list(file_dict)[-1]]
    for col in range(0, first_len):
        col_list = []
        for key in list(file_dict)[:-1]:
            col_list.append(str_to_num(file_dict[key][col]))
        # print(col_list)
        sumlist += perform_operation(op_list[col], col_list)
    return sumlist


if __name__ == "__main__":
    
    from math import prod, log10

    input_file = "d06_input.txt"
    
    file_dict = read_file(input_file)
    
    # the position of the operators is the only consistent delimiter between columns.
    # therefore, we will use the operator line to determine break points for the data lines

    op_list = file_dict[list(file_dict)[-1]]  # get the last line of the dictionary, which contains the operators
    op_indices = nonspace_indices(op_list)
    
    # reconstruct the file_dict so that each entry is a list of strings representing the values in each column
    for key in list(file_dict)[:-1]:
        file_dict[key] = split_by_indices(file_dict[key], op_indices)
            
    # do all values in the dict have the same length?
    first_len = check_data_length(file_dict)
        
    sumlist = 0
    op_list_split = op_list.split()
    for col in range(0, first_len):
        numlist = []
        col_len = len(file_dict[1][col])

        for pos in range(col_len-1, -1, -1):  # iterates right-to-left on each line of column
            accumulator = ""

            for key in list(file_dict)[:-1]:  # iterate over all but the last line of each column
                string = (file_dict[key][col][pos])
                accumulator += string
            numlist.append(accumulator)

        numlist = [int(n) for n in numlist]
        print(numlist)
        sumlist += perform_operation(op_list_split[col], numlist)
    print(f"Sum of all operations: {sumlist}")