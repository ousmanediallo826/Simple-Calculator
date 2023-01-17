def calc():
  print("Enter the operation sign + - * /")
  operator_signs = input()
  print("Enter the first number:")
  num1 = float(input())
  print("Enter the second number: ")
  num2 = float(input())
  if operator_signs == '+':
    print("result is, ", num1 + num2)
  elif operator_signs == '-':
    print("result is, ", num1 - num2)
  elif operator_signs == '*':
    print("result is, ", num1 * num2)
  elif operator_signs == '/':
    print("result is, ", num1 / num2)

  else:
    print("Invalid input")
calc()

