def basic_calculator(a,b,operation):

  if (a.isnumeric() & b.isnumeric()):
    a=float(a)
    b=float(b)
    if operation == "toplama" or operation == "+":
      result = a + b
    elif operation == "çıkarma" or operation == "-":
      result = a - b
    elif operation == "bölme" or operation == "/":
      result = a / b
    elif operation == "çarpma" or operation == "*":
      result = a * b
    elif operation == "mod" or operation == "%":
      result = a % b
    else:
      result = "Sadece şunlar geçerlidir: toplama(+), çıkarma(-), bölme(/), çarpma(*), mod(%)"
    
  else:
    result = "Doğru bir sayı girin!"
    

  return result