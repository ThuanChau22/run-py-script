import json

# script = """
# import numpy as np
# def main():
#     data = {
#         "ids": ["one", "two", "three"],
#         "entities": {
#             "one": 1,
#             "two": 2,
#             "three": 4
#         }
#     }
#     print("this is a test")
#     print(np.arange(15).reshape(3, 5))
#     return data
# """

# script = """
# def fibonacci(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(n - 1):
#         a, b = b, a + b
#     return b

# def main():
#     n = 200
#     result = fibonacci(n)
#     print(f"Fibonacci of {n}th:")
#     print(result)
#     return result
# """

script = """
def main():
    count = 0
    while(True):
      count += 1
"""

print(json.dumps(script))
