import numpy as np
from collections import deque

def adjacent_sum_optimized(arr: np.ndarray) -> int:
    """
    Optimized version using a queue to track only cells that need checking.
    Time complexity: O(n*m) where n*m is grid size (single pass through affected cells)
    Space complexity: O(n*m) for the neighbor count array
    """
    rows, cols = arr.shape
    count = 0
    
    # Define the 8 possible neighbor offsets (including diagonals)
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),           (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]
    
    # Precompute neighbor counts for all cells with paper rolls
    neighbor_counts = np.zeros((rows, cols), dtype=int)
    queue = deque()
    
    # Initial pass: compute neighbor counts and identify vulnerable cells
    for i in range(rows):
        for j in range(cols):
            if arr[i, j]:
                neighbor_sum = 0
                for di, dj in neighbors:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbor_sum += arr[ni, nj]
                
                neighbor_counts[i, j] = neighbor_sum
                if neighbor_sum < 4:
                    queue.append((i, j))
    
    # Process removals using queue
    while queue:
        i, j = queue.popleft()
        
        # Check if still needs to be removed (neighbor count might have changed)
        if arr[i, j] == 0 or neighbor_counts[i, j] >= 4:
            continue
        
        # Remove the paper roll
        arr[i, j] = 0
        count += 1
        
        # Update neighbor counts for adjacent cells and check if they become vulnerable
        for di, dj in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and arr[ni, nj]:
                neighbor_counts[ni, nj] -= 1
                if neighbor_counts[ni, nj] < 4:
                    queue.append((ni, nj))
    
    return count



def read_grid_from_file(file_path: str) -> np.ndarray:
    """Read grid from file and convert '@' symbols to 1s."""
    arr = np.genfromtxt(file_path, dtype='U1', delimiter=1)
    return (arr == '@').astype(int)


if __name__ == "__main__":
    input_file = "d04_01_input.txt"
    
    grid = read_grid_from_file(input_file)
    
    # Use optimized version
    result = adjacent_sum_optimized(grid.copy())
    print(f"Total rolls removed: {result}")
    