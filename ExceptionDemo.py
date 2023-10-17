class NumeratorError (Exception):
     def __init__(self, message):
        self.message = message
   
     def __str__(self):
        return(self.message)




try:
    n=int(input("Enter Numerator:"))
    d=int(input("Enter Divisor:"))
    if n<d :
        raise NumeratorError("Numerator must greater than Divisor")
    r=n/d
    print("The result:",r)
except ArithmeticError:
    print("Divide by zero not possible")
except ValueError:
    print("Input must be whole number")
except NumeratorError as error1:
    print(error1)
finally:
    print("Prog is over")
    
