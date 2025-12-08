

import numpy as np

def adjacent_sum_np(arr: np.ndarray) -> int:
    # arr = np.asarray(arr, dtype=int)
    rows, cols = arr.shape
    count = 0
    
    # Define the 8 possible neighbor offsets (including diagonals)
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]
    
    # Initial number of paper rolls
    initial_rolls = np.sum(arr)
    final_rolls = initial_rolls - 1  # Allows the while loop to start
    
    while final_rolls != initial_rolls:
        initial_rolls = final_rolls  # set 
        # Iterate through each element in the array
        for i in range(rows):
            for j in range(cols):
                neighbor_sum = 0
                
                if not arr[i, j]:
                    continue  # Skip if the current cell is not '@' (i.e., 1)
                
                # Sum all valid neighbors
                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    # Check if neighbor is within bounds
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbor_sum += arr[ni, nj]
                
                # Check if sum is less than 4
                if neighbor_sum < 4:
                    count += 1
                    
                    # Remove the paper roll
                    arr[i, j] = 0
                    
        final_rolls = np.sum(arr)
        print("Rolls removed this pass:", initial_rolls - final_rolls)
    
    return count
    

def read_grid_from_file(file_path: str) -> np.ndarray:
    arr = np.genfromtxt(file_path, dtype='U1', delimiter=1)
    return (arr == '@').astype(int)  # Convert '@' to 1, others to 0


if __name__ == "__main__":
    input_file = "d04_01_input.txt"
    
    grid = read_grid_from_file(input_file)
    sum_grid = adjacent_sum_np(grid)
    print("Grid of adjacent '@' counts:")
    print(sum_grid)