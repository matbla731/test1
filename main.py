# addition function, takes in 2 numbers returns the result
def add(number1,number2):
    Output=number1+number2
    return Output

# subtraction function, takes in 2 numbers returns the result
def minus(number1,number2):
    Output=number1-number2
    return Output

# multiplication function, takes in 2 numbers returns the result
def multiply(number1,number2):
    Output=number1*number2
    return Output
# division function, takes in 2 numbers returns the result
def divide(number1,number2):
    Output=number1/number2
    return Output
# get input 1
number1=float(input("write stuff here"))
# get input 2
number2=float(input("write stuff here 2"))
# get operator
UserInput3=(input("write operator here"))

#write an if2.3
#  statement that acts like a calculato1


if UserInput3==("divide"):
    outputValue = divide(number1,number2)

    print(outputValue) 


elif UserInput3==("multiply"):
    outputValue = multiply(number1,number2)

    print(outputValue)


elif UserInput3==("add"):
    outputValue = add(number1,number2)


    print(outputValue)


elif UserInput3==("minus"):
    outputValue = minus(number1,number2)


    print(outputValue)

else:   print("error") 