def factorial(n):

  if n <=1:
    return 1
  else:
    print(n / 0)
    return n * factorial(n - 1)

try:
  print(factorial(1000))
except RecursionError:
  print('This program cannot calculate factorials this large')
except ZeroDivisionError:
  print('Division by 0')
except (NotImplementedError, PermissionError):
  print('Method not implemented or permission error')

print('Program terminating')