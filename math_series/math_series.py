# used as a reference: https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/

# Returns nth number Fibonacci sequence
def fibonacci(num):
  '''
  Given a fibonacci sequence, return the nth number 
  sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
  if number is 0 return 0
  if number is 1 return 1
  if number is 1 return 1
  if number is 2 return 1
  if number is 3 return 2
  if number is 5 return 3
  '''
  # covers negative numbers
  if num <= 0:
    return 0
  elif num == 1:
    return 0
  elif num == 2:
    return 1
  
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)

# Returns nth number Lucas sequence
def lucas(num):
  '''
  Given a lucas sequence, return the nth number 
  sequence: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199
  if number is 0 return 2
  if number is 1 return 1
  if number is 3 return 3
  if number is 4 return 4
  if number is 7 return 18
  if number is 5 return 7
  '''
  
  # covers negative numbers
  if num < 0:
    return print("Incorrect number")
  elif num == 0:
    return 2
  elif num == 1:
    return 1
  else:
    return lucas(num - 1) + lucas(num - 2)

# if num2 and num 3 starting numbers match Fibonacci or Lucas sequence then run the coresponding function, if not then run custom sequence to find nth number

def sum_series(num1, num2=0, num3=1):
  '''
  Given 1 required parameter and 2 optional parameters, check if num2 and num 3 starting numbers match Fibonacci or Lucas sequence then run the coresponding function, if not then run custom sequence to find nth number
  
  if 2nd and 3rd parameter match Fibonacci then run fibonacci
  if 2nd and 3rd parameter match Lucas then run Lucas
  else run custom sequencer
  '''
  if num2 == 2 and num3 == 1:
    print(lucas(num1))
  elif num2 ==0 and num3 == 1:
    print(fibonacci(num1))
  else:
    return custom_sequence(num1, num2, num3)
  
def custom_sequence(num1, num2, num3):
  '''
  Return nth number of sequence based off of 2nd and 3rd paramters
  '''
  if num1 == 1:
    return num2
  else:
    return num3 * custom_sequence(num1-1, num2, num3)
    
print(fibonacci(3))
print(lucas(7))
print(sum_series(1,2,3))
