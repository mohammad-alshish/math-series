# fibonacci

def fibonacci(n):
  if type(n) != int :
    return 'Enter a number please'
  elif n < 0:
    return('Enter a whole number >= 0')
  elif n == 1 or n == 0:
    return n
  else:
    return(fibonacci(n-1) + fibonacci(n-2))


# Lucas

def Lucas(n):
  if type(n) != int :
    return 'Enter a number please'
  elif n < 0:
    return('Enter a whole number >= 0')
  elif n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return(Lucas(n-1) + Lucas(n-2))



# Sum series

def sum_series(n, n1=0, n2=1):

  if n == 0:
    return n1
  elif n == 1:
    return n2
  else:
    return(sum_series(n-1, n1, n2) + sum_series(n-2, n1, n2))

