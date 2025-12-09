


def in_ranges(x: int, ranges: list[tuple[int, int]]) -> bool:
    return any(start <= x <= end for start, end in ranges)

def process_input_file(input_file: str) -> tuple[list[tuple[int, int]], list[int]]:    
    
    read_ingredients = False
    fresh_ingredient_ranges = []
    ingredient_ids = []
    
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            
            # if the line is blank, start reading ingredient_id
            if not line:
                read_ingredients = True
                print("Finished reading fresh ingredient ranges.")
            
            if not read_ingredients:
                line_split = line.split("-")
                fresh_ingredient_ranges.append((int(line_split[0]), int(line_split[1]) + 1))

            else:
                # Read each line as an ingredient
                if line:
                    ingredient_ids.append(int(line))
                else:
                    continue
            
    return fresh_ingredient_ranges, ingredient_ids


if __name__ == "__main__":

    input_file = "d05_01_input.txt"

    fresh_ingredient_rngs, ingredient_ids = process_input_file(input_file)
    
    # num_fresh_ingredients = fresh_ingredients & set(ingredient_ids)
    
    avail_fresh_ingredients = 0
    for ingredient in ingredient_ids:
        if in_ranges(ingredient, fresh_ingredient_rngs):
            avail_fresh_ingredients += 1
    
    # print(f"Total fresh ingredients available: {len(fresh_ingredient_ranges)}")
    print(f"Total ingredients listed: {len(ingredient_ids)}")
    
    print(f"Number of fresh ingredients used: {avail_fresh_ingredients}")
    