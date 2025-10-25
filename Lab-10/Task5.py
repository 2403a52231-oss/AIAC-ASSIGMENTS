"""
nums = [i for i in range(1,1000000)]
squares=[]
for n in nums:
    squares.append(n**2)
print(len(squares))    
"""
import time
"""
This script measures the time taken to compute the squares of numbers from 1 to 999,999.

Steps:
1. It creates a list of numbers from 1 to 999,999.
2. It computes the square of each number and stores them in a new list.
3. It prints the total number of squares computed.
4. It prints the time taken to perform the computation.

Example Output:
999999
Time taken to run the code: 0.1234 seconds
"""
start_time = time.time()
nums = [i for i in range(1,1000000)]
squares = []
for n in nums:
    squares.append(n**2)
print(len(squares))
end_time = time.time()
print(f"Time taken to run the code: {end_time - start_time:.4f} seconds")



