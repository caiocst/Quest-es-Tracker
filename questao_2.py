def teste_fibonacci(num):
  num_1 = 0
  num_2 = 1
  while num_2 < num:
    num_1 = num_2
    num_2 += num_1

  if num_2 == num:
    return True
  else:
    return False
  


num = 8
if teste_fibonacci(num):
  print(f"{num} pertence à sequência de Fibonacci.")
else:
  print(f"{num} não pertence à sequência de Fibonacci.")


