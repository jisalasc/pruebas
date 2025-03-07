import time

n = 1000000000  # 1 billion
sum = 0

start = time.time()
for i in range(1, n + 1):
    sum += i
end = time.time()

cpu_time_used = end - start
print(f"Sum: {sum}")
print(f"Time taken: {cpu_time_used} seconds")
# filepath: c:\Users\cotes\Dropbox\Mi PC (DESKTOP-T321991)\Desktop\EDD\pruebas\sum.py
import time

n = 1000000000  # 1 billion
sum = 0

start = time.time()
for i in range(1, n + 1):
    sum += i
end = time.time()

cpu_time_used = end - start
print(f"Sum: {sum}")
print(f"Time taken: {cpu_time_used} seconds")