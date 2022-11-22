# to check whther a number is prime or not
n = int(input())
is_prime = True
for i in range(2,n):
    if n%i ==0:
        is_prime = False
        break 
if is_prime:
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')