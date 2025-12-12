


def read_grid_from_file(file_path: str) -> np.ndarray:
    arr = np.genfromtxt(file_path, dtype='U1', delimiter=1)  # Read file as an ndarray of single characters
    return (arr != '.').astype(int)  # Convert '@' to 1, others to 0


def get_idx_of_nonzero(int_list: list[int]) -> list[int]:
    return [i for i, n in enumerate(int_list) if n]


def process_grid_splits(grid: np.ndarray) -> None:
    
    # find the starting positions of the beams in the first row
    start_row = get_idx_of_nonzero(grid[0])
    num_rows = grid.shape[0]

    split_list = []
    for row in range(1, num_rows):
        splits = []

        row_splits = get_idx_of_nonzero(grid[row])
        hits = list(set(start_row) & set(row_splits))
        if hits:
            print(f"Splits occurred in row {row} at columns {hits}")
            # Add back any beams that didn't get split

            splits = list(set([hit + d for hit in hits for d in (-1, 1)]))
            split_list.extend(hits)
            for beam in start_row:
                if beam not in hits:
                    splits.append(beam)
            
            start_row = list(set(splits))
            print(f"Beams now at {start_row}")
    return split_list


if __name__ == "__main__":
    import numpy as np
    input_file = "d07_input.txt"
    
    grid = read_grid_from_file(input_file)
    
    split_list = process_grid_splits(grid)
            
    print(f"Total splits: {len(split_list)}")