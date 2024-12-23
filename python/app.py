def main():

    print("Hello World!")
    print("It Works!!")

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
            
    count_inpt1 = input("masukan nomer count count start loop (dibawah angka 10) ")
    print("---------------")
    count(int(count_inpt1))

    #-------> tes loop pake rekursi dengan bantuan list
    print("perulangan rekursi")
    print("---------------")
    def count(n):
        if n > 10:
            return []
        return [n] + count(n + 1)

    count_inpt2 = input("masukan nomer count start loop w/ bantuan list (dibawah angka 10) ")
    print("---------------")
    print(count(int(count_inpt2)))

    #-------> tes fibonacci menggunakan rekursi
    print("fibonacci")
    print("---------------")

    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)

    fib_inpt = input("masukan nomer fib ")
    print(fib(int(fib_inpt)))
    
if __name__ == "__main__":
    main()
