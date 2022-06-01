

 # fibonacci
 # Accept an integer and output what Fibonacci value that integer corresponds with The integer input represents the index of the output value.


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
 # Accept an integer and output what Lucas value that integer corresponds with The integer input represents the index of the output value.

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
  # Accept an integer and two optional arguments, which are set to 0 and 1 respectively by default (AKA the starting numbers for Fibonacci). If those two optional arguments are passed into the function call,
  # they represent the first two numbers in a new sequence that follows the same rule as Fibonacci and Lucas (AKA, those two optional arguments represent index 0 and 1 of the new sequence).
  # The required integer input represents the index of the output value.

def sum_series(n, n1=0, n2=1):

  if n == 0:
    return n1
  elif n == 1:
    return n2
  else:
    return(sum_series(n-1, n1, n2) + sum_series(n-2, n1, n2))

