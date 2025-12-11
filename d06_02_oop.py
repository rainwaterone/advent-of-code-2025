from math import prod
from typing import Callable
from pathlib import Path


class DataParser:
    """Handles parsing and splitting of string data based on indices."""
    
    @staticmethod
    def nonspace_indices(s: str) -> list[int]:
        """Find indices of all non-space characters."""
        return [i for i, ch in enumerate(s) if ch != ' ']
    
    @staticmethod
    def split_by_indices(s: str, indices: list[int]) -> list[str]:
        """Split string into parts based on given indices."""
        parts = []
        for i in range(len(indices) - 1):
            start = indices[i]
            end = indices[i + 1]
            parts.append(s[start:end-1])
        parts.append(s[indices[-1]:])
        return parts
    
    @staticmethod
    def str_to_num(numstr: str) -> int | float:
        """Convert string to int or float."""
        try:
            return int(numstr)
        except ValueError:
            try:
                return float(numstr)
            except ValueError:
                raise ValueError(f"Valid number not found in {numstr}")


class Operation:
    """Handles mathematical operations on lists of numbers."""
    
    OPERATIONS = {
        "+": sum,
        "*": prod
    }
    
    @classmethod
    def perform(cls, op: str, numbers: list[float]) -> float:
        """Perform operation on a list of numbers."""
        if op not in cls.OPERATIONS:
            raise ValueError(f"Operator must be one of {list(cls.OPERATIONS.keys())}")
        return cls.OPERATIONS[op](numbers)


class ColumnData:
    """Represents a single column of data with its values and operator."""
    
    def __init__(self, values: list[int | float], operator: str):
        self.values = values
        self.operator = operator
    
    def calculate(self) -> float:
        """Calculate the result of applying the operator to values."""
        return Operation.perform(self.operator, self.values)
    
    def __repr__(self):
        return f"ColumnData(values={self.values}, operator='{self.operator}')"


class DataFile:
    """Represents and processes a data file with rows and columns."""
    
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.raw_lines: dict[int, str] = {}
        self.parsed_data: dict[int, list[str]] = {}
        self.operator_line: str = ""
        self.operator_indices: list[int] = []
        self.columns: list[ColumnData] = []
        
    def load(self) -> 'DataFile':
        """Load file contents into memory."""
        with open(self.filepath, 'r') as f:
            for i, line in enumerate(f):
                self.raw_lines[i] = line.rstrip('\n')
        
        if not self.raw_lines:
            raise ValueError("File is empty")
            
        # Last line contains operators
        last_key = max(self.raw_lines.keys())
        self.operator_line = self.raw_lines[last_key]
        
        return self
    
    def parse(self) -> 'DataFile':
        """Parse the loaded data based on operator positions."""
        # Find column boundaries from operator positions
        self.operator_indices = DataParser.nonspace_indices(self.operator_line)
        
        # Split each data line by the operator indices
        last_key = max(self.raw_lines.keys())
        for key in self.raw_lines:
            if key != last_key:  # Skip operator line
                self.parsed_data[key] = DataParser.split_by_indices(
                    self.raw_lines[key], 
                    self.operator_indices
                )
        
        return self
    
    def extract_columns(self) -> 'DataFile':
        """Extract column data by reading vertically through the parsed data."""
        num_columns = len(self.operator_indices)
        operators = self.operator_line.split()
        
        for col_idx in range(num_columns):
            col_values = []
            
            # Get column width from first row
            if self.parsed_data:
                first_key = min(self.parsed_data.keys())
                col_width = len(self.parsed_data[first_key][col_idx])
                
                # Read each column right-to-left, top-to-bottom
                for pos in range(col_width - 1, -1, -1):
                    accumulator = ""
                    for row_key in sorted(self.parsed_data.keys()):
                        accumulator += self.parsed_data[row_key][col_idx][pos]
                    col_values.append(int(accumulator))
            
            # Create column object
            column = ColumnData(col_values, operators[col_idx])
            self.columns.append(column)
        
        return self
    
    def validate(self) -> bool:
        """Validate that all data rows have the same number of columns."""
        if not self.parsed_data:
            return False
        
        values = list(self.parsed_data.values())
        data_len = len(values[0])
        is_valid = all(len(v) == data_len for v in values)
        
        print(f"Each line has the same number of values or operators? {is_valid}")
        if is_valid:
            print(f"Number of operations: {len(self.columns)}")
        
        return is_valid
    
    def calculate_total(self) -> float:
        """Calculate the sum of all column operations."""
        total = sum(col.calculate() for col in self.columns)
        return total
    
    def print_columns(self):
        """Print all columns for debugging."""
        for i, col in enumerate(self.columns):
            print(f"Column {i}: {col}")


def main():
    """Main execution function."""
    input_file = "d06_input.txt"
    
    # Process the data file using method chaining
    data_file = (DataFile(input_file)
                 .load()
                 .parse()
                 .extract_columns())
    
    # Validate and display results
    data_file.validate()
    data_file.print_columns()
    
    total = data_file.calculate_total()
    print(f"Sum of all operations: {total}")


if __name__ == "__main__":
    main()