


def in_ranges(x: int, ranges: list[tuple[int, int]]) -> bool:
    return any(start <= x <= end for start, end in ranges)

    
def process_input_file(input_file: str) -> list[tuple[int, int]]:    
    
    fresh_ingredient_ranges = []
    
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            
            # if the line is blank, stop reading ingredient ranges
            if not line:
                print("Finished reading fresh ingredient ranges.")
                break
            
            else:
                line_split = line.split("-")
                fresh_ingredient_ranges.append((int(line_split[0]), int(line_split[1]) + 1))
           
    return fresh_ingredient_ranges


def get_available_ingredients(fresh_ingredient_rngs: list[tuple[int, int]]) -> set[int]:
    avail_fresh_ingredients = set()
    for rng in fresh_ingredient_rngs:
        for ingredient in range(rng[0], rng[1]):
            avail_fresh_ingredients.add(ingredient)
    return avail_fresh_ingredients

def count_available_ingredients(fresh_ingredient_rngs: list[tuple[int, int]]) -> int:
    if not fresh_ingredient_rngs:
        return 0
    
    # Sort ranges by start point
    sorted_rngs = sorted(fresh_ingredient_rngs)
    
    # Merge overlapping ranges
    merged = [sorted_rngs[0]]
    for start, end in sorted_rngs[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # Overlapping or adjacent
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    # Sum the lengths of merged ranges
    return sum(end - start for start, end in merged)

if __name__ == "__main__":

    input_file = "d05_01_input.txt"

    fresh_ingredient_rngs = process_input_file(input_file)
   
    # avail_fresh_ingredients = get_available_ingredients(fresh_ingredient_rngs)
    
    
    print(f"Number of fresh ingredients available: {count_available_ingredients(fresh_ingredient_rngs)}")
    