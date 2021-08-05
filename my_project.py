import sys
n=int(input())
if n%2==0:
    print(int(n/2))
    sys.exit()
elif n%2!=0:
    print(n)

    sys.exit()
else:
    print(0)
    sys.exit()