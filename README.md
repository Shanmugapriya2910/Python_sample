This project provides functionality to categorize numbers in a specified range into even, odd, and prime numbers.

## Features
- **Categorization of Numbers**: Divides numbers into even, odd, and prime numbers.
- **File Output**: Saves results to a file named `numbers.txt`.
- **Unit Tests**: Verifies result using Python's `unittest` framework.

### Files
1. `numbers.py`
   - Contains the main functionality to numbers.
   - Accepts user input for range (`start` and `end`).
   - Writes results to `numbers.txt`.

### Output File
- `numbers.txt`: Stores the numbers (even, odd, and prime).

### Requirements
- Python 3.7+

## Code Structure
### `numbers(start, end)`
This function takes a starting and ending number and returns a dictionary with three keys:
- `even`: A list of even numbers in the range.
- `odd`: A list of odd numbers in the range.
- `prime`: A list of prime numbers in the range.

#### Parameters
- `start` (int): The starting number of the range.
- `end` (int): The ending number of the range.

#### Returns
Returns a dictionary with the numbers.

### Helper Function
#### `is_prime(num)`
Determines whether a number is prime.


#### Returns
- `True` if the number is prime.
- `False` otherwise.

## Example Output
### Input
```
Enter starting number: 1
Enter ending number: 10
```

### Console Output
```
{'even': [2, 4, 6, 8, 10], 'odd': [1, 3, 5, 7, 9], 'prime': [2, 3, 5, 7]}
```

### File Output 
```
Even Numbers: [2, 4, 6, 8, 10]
Odd Numbers: [1, 3, 5, 7, 9]
Prime Numbers: [2, 3, 5, 7]
```



