


def max_joltage(bank: str, nbatt: int) -> int:
    if len(bank) < nbatt:
        raise ValueError("Bank length is less than number of batteries requested")
    bankstr = list(bank)
    bankint = [int(x) for x in bankstr]

    fidx = 0
    digits = []
    subset = bankint
    l = len(subset)
    
    while len(digits) < nbatt:
        digit = max(subset[:l-nbatt+len(digits)+1])
        digits.append(digit)
        fidx = subset.index(digit)
        subset = subset[fidx+1:]
        l = len(subset)
        print(f"Digits so far: {digits}, next subset: {subset}")
        
    return int("".join(map(str, digits)))

    

if __name__ == "__main__":
    total_jolts = 0
    battery_file = "d03_01_input.txt"
    num_batts_per_bank = 12
    with open(battery_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                mj = max_joltage(line, num_batts_per_bank)
                print(f"Max joltage for bank {line} is {mj}")
                total_jolts += mj
    print(f"Total joltage from all banks: {total_jolts}")
    
