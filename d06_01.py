

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
        

def read_file(input_file):
    f_dict = {}
    with open(input_file, 'r') as f:
        for i, line in enumerate(f):
            f_dict[i] = line.strip().split()
    return f_dict


def check_data_length(file_dict):
    values = file_dict.values()
    data_len = len(next(iter(values)))  # gets the length of the first value
    check_length = all(len(v) == data_len for v in values)
    print(f"Each line has the same numer of values or operators? {check_length}")
    if check_length:
        print(f"Number of operations: {len(file_dict[0])}")
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
    
    from math import prod

    input_file = "d06_input.txt"
    
    operator_list = []

    file_dict = read_file(input_file)    
            
    # do all values in the dict have the same length?
    first_len = check_data_length(file_dict)
        
    sumlist = sum_all_operations(perform_operation, str_to_num, file_dict, first_len)
    print(f"Sum of all operations: {sumlist}")