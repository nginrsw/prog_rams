-module(fibo).
-export([fib/1, fib/3]).

fib(N) when N >= 0 -> fib(N, 0, 1).

fib(0, A, _B) -> A;
fib(N, A, B) when N > 0 -> fib(N -1, B, A + B).
