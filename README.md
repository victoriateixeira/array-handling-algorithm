# Array Handling Algorithm

This algorithm traverses a one-dimensional array containing letters and numbers and performs the following operations:

- Obtains an array containing only letters.
- Obtains an array containing only numbers.
- Finds the largest number from the numbers array.

## Algorithm Implementation

The algorithm is implemented in Python using a function called `alg_handling`. The function takes an input array and returns a list containing the following:

1. Array containing only letters.
2. Array containing only numbers.
3. Largest number from the numbers array.

The algorithm makes use of helper functions, `same_type_array` and `largest_number`, to filter the array based on type and find the largest number respectively.

## Usage

To use the algorithm, you can pass your input array to the `alg_handling` function. Here's an example usage:

```python
mixed_array = ["a", 10, "b", "hello", 122, 15]
result = alg_handling(mixed_array)
print(result)
```
The output will be a list containing the array of letters, the array of numbers, and the largest number in the aforementioned array of numbers.

### Note
The algorithm assumes that the input array is a one-dimensional array.
The algorithm differentiates between letters (strings) and numbers (integers).



<hr>
<p align="center">
Developed by Victoria Teixeira
</p>
