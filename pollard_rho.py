!pip install tabulate
import time
from tabulate import tabulate

def pollards_rho(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def rho_pollard_iteration(x, n):
        return (x**2 + 1) % n

    a, b = 2, 2
    p = 1

    start_time = time.time()

    while p == 1:
        a = rho_pollard_iteration(a, n)
        b = rho_pollard_iteration(rho_pollard_iteration(b, n), n)
        p = gcd(abs(a - b), n)

    end_time = time.time()

    if p == n:
        return None, None, None, None

    q = n // p

    success = "Success" if p > 1 and q > 1 else "Failure"
    execution_time = end_time - start_time

    return p, q, success, execution_time

#numbers = [2916425411, 11752700814259, 1341849068550433, 41723662237262923, 432501171954594013, 8763301721976902561, 49808531654765413631,
           #2936653455160738453027,1473079949540259829229771, 12369352403768659453215077,268889892902937863375973328747,56839690024188205150194976305169]

numbers = [2916425411]

results_table = []

for num in numbers:
    p, q, success, execution_time = pollards_rho(num)

    if p:
        success_percentage = 100 if success == "Success" else 0
        results_table.append([num, p, q, success, execution_time, success_percentage])
    else:
        results_table.append([num, "Factorization failed.", "-", "Failure", "-", 0])

headers = ["n", "p", "q", "Success", "Execution Time (s)", "Success Percentage"]
print(tabulate(results_table, headers=headers, tablefmt="fancy_grid"))
