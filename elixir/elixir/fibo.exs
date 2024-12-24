defmodule FiboKecil do
	def fib(0), do: 0
	def fib(1), do: 1
	def fib(n) when n > 1, do: fib(n - 1) + fib(n - 2)
end

IO.puts FiboKecil.fib(9)

defmodule FiboBesar do
  def fib(n), do: fib(n, 0, 1)
  defp fib(0, a, _b), do: a
  defp fib(n, a, b) when n > 0, do: fib(n - 1, b, a + b)
end

IO.puts FiboBesar.fib(10000)
