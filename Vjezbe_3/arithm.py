import math

# a)

N = []

for i in range(10):

    n = float(input("Unesi točku: "))

    N.append(n)

ar_sred = sum(N)/len(N)

sum = 0

for i in N : 

    sum += (i - ar_sred)**2

stand_dev = math.sqrt(sum/ (len(N)-1))

print(N)
print(ar_sred)
print(stand_dev)

# b) korištenje gotovih modula , npr. statistics

import statistics 

N = []

for i in range(10):

    n = float(input("Unesi točku: "))

    N.append(n)

print(N)
print(statistics.mean(N))
print(statistics.stdev(N))