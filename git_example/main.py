"""
Simple script iterating and printing the iteration number.
"""
import time

ITERATIONS = 10
SLEEP_TIME = 0.1

for iteration in range(ITERATIONS):
    print(iteration)
    time.sleep(SLEEP_TIME)
