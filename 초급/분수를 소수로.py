import sys
from decimal import Decimal, getcontext

a,b = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())

getcontext().prec = n
out = Decimal(a)/Decimal(b)
print(round(out,n))