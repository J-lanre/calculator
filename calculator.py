def check_and_calculate(num1, num2, operation):
  """
  This function checks if two inputs are numeric and performs the specified operation.
  """
  if not (num1.isnumeric() or num2.isnumeric()):
    print("Error: Please enter only numeric values.")
    return None
  
  try:
    # Convert to numbers using float() for better handling of decimals
    num1 = float(num1)
    num2 = float(num2)
  except ValueError:
    print("Error: Please enter only numeric values.")
    return None

  # Perform the operation based on input
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
      return None
    else:
      result = num1 / num2
  else:
    print("Error: Invalid operation. Choose +, -, *, or /.")
    return None

  return result

# Example usage (with input)
number_1 = input("Enter first number: ")
number_2 = input("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

# Check and calculate
result = check_and_calculate(number_1, number_2, operation)

if result is not None:
  print(number_1, operation, number_2, "=", result)
else:
  print("Invalid input. No result available.")