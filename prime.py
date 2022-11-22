# to check whther a number is prime or not
n = int(input())
is_prime = True
if n% 2 ==0:
    is_prime = False
for i in range(3,n,2):
    if n%i ==0:
        is_prime = False
if is_prime:
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')