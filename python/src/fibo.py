import sys

sys.set_int_max_str_digits(1000000)

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
        
sml_fibo = int(input("masukan angka fibo kecil: "))
print(fibo(sml_fibo))

def fibo_L(n, memo={0: 0, 1: 1}):
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]
        
lrg_fibo = int(input("masukan angka fibo besar: "))
print(fibo_L(lrg_fibo))
    
