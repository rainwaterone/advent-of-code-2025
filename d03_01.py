
def max_joltage(bank: str) -> int:
    bankstr = list(bank)
    bankint = [int(x) for x in bankstr]
    first_digit = max(bankint)
    # if the largest digit is the last one in the list, make it the second digit
    fidx = bankint.index(first_digit)
    if fidx == len(bankint) - 1:
        second_digit = first_digit
        first_digit = max(bankint[:fidx])
    else:
        second_digit = max(bankint[fidx + 1:])
    return first_digit * 10 + second_digit

if __name__ == "__main__":
    total_jolts = 0
    battery_file = "d03_01_input.txt"
    with open(battery_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                mj = max_joltage(line)
                print(f"Max joltage for bank {line} is {mj}")
                total_jolts += mj
    print(f"Total joltage from all banks: {total_jolts}")
    
