import time
import math
miliseconds = int(input())
number = int(input())
time.sleep(miliseconds / 1000)
print(f"Square root of {number} after {miliseconds} miliseconds is {math.sqrt(number)}")
