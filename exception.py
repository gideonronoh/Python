try:
    numerator=int(input("Enter a number to divide by: "))
    denominator= int(input("Enter a number to divide with: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
   print("You can't divide by  zero idiot")    
except Exception:
  print("Something went wrong") 
except ValueError:
   print("Enter only numbers please")  
else :(result)
finally:
   print("This is the end of the program")
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input. Please enter a valid number.")
