print("Hello World!")

#-------> tes factorial
print("faktorial")
print("---------------")
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
        
#-------> tes input fn fact
fact_inpt = input("masukan nomer fact ")
print("---------------")
print(fact(int(fact_inpt)))

#-------> tes loop pake rekursi biasa
print("perulangan rekursi")
print("---------------")
def count(n):
    if n > 10:
        return
    print(n)
    count(n+1)
        
count_inpt1 = input("masukan nomer count ")
print("---------------")
count(int(count_inpt1))

#-------> tes loop pake rekursi dengan bantuan list
print("perulangan rekursi")
print("---------------")
def count(n):
    if n > 10:
        return []
    return [n] + count(n + 1)

count_inpt2 = input("masukan nomer count list ")
print("---------------")
print(count(int(count_inpt2)))
