!pip install tabulate
import random
import time
from tabulate import tabulate

def power(a, n, p):
    res = 1
    a = a % p

    while n > 0:
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            n = n // 2

    return res % p

def isPrime(n, k):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):
            a = random.randint(2, n - 2)
            if power(a, n - 1, n) != 1:
                return False
    return True

k = 100

"""numbers = [561, 41041, 75361, 126217, 488881, 5394826801, 1436697831295441, 1791562810662585767521,
           1590231231043178376951698401, 349407515342287435050603204719587201,
           12758106140074522771498516740500829830401,70416887142533176417390411931483993124120785701395296424001]  carmichael"""


#numbers = [127, 8191, 131071, 524287, 2147483647, 170141183460469231731687303715884105727 ] #mersenne
numbers = [524287, 6700417, 2147483647, 170141183460469231731687303715884105727, 5210644015679228794060694325390955853335898483908056458352183851018372555735221,
           6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,
           531137992816767098689588206552468627329593117727031923199444138200403559860852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127]

results = []

for num in numbers:
    start_time = time.time()
    prime_result = isPrime(num, k)
    execution_time = time.time() - start_time
    results.append([num, prime_result, execution_time])

header = ["Number", "Is Prime", "Execution Time (s)"]
table = tabulate(results, headers=header, tablefmt="fancy_grid")

print(table)
