# run-py-script

An API service that takes any python script as input and returns the result of the script execution as output.

## Run Project

1. Build: `docker build --target development -t run-py-service .`

2. Run: `docker run -d --name run-py-service -p 8080:8080 run-py-service`

## Example

Input: `curl -X POST http://localhost:8080/execute -H "Content-Type: application/json" -d '{    "script": "\ndef fibonacci(n):\n    if n <= 1:\n        return n\n    a, b = 0, 1\n    for _ in range(n - 1):\n        a, b = b, a + b\n    return b\n\ndef main():\n    n = 200\n    result = fibonacci(n)\n    print(f\"Fibonacci of {n}th:\")\n    print(result)\n    return result\n"}'`

Output: `{  "result": 280571172992510140037611932413038677189525,  "stdout": [    "Fibonacci of 200th:",    "280571172992510140037611932413038677189525"  ]}`
