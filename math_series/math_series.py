def fibonacci(num):
  '''
  Given a sequence that starts with 0 and 1 return a sequence so that each number is the sum of the two previous numbers
  sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
  if number is 0 return 0
  if number is 1 return 1
  if number is 1 return 1
  if number is 2 return 2
  if number is 3 return 3
  if number is 5 return 5
  '''
  # covers negative numbers
  if num <= 0:
    return 0
  if num == 1:
    return 0
  if num == 2:
    return 1
  
  print(fibonacci(num - 1) + fibonacci (num - 2))
  return fibonacci(num - 1) + fibonacci(num - 2)
