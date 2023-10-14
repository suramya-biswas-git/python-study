calculator = lambda operand1, operand2, operator : operand1+operand2 if operator=="+" else\
(operand1-operand2 if operator=="-" else (operand1* operand2  if operator=="*" else operand1/operand2))
    


#print(calculator(4,5,"-"))

  
