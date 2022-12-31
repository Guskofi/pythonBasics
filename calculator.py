##############################################################################
#this program simulates a calculator that can do 4 basic arithmetric +,/,*,-
#it always assumes the user will continue adding operands after the initial results
#the user can restart with a c or quit with a q.
#############################################################################

import sys
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        sys.exit('You cant divide by 0')
    else:
        return a / b
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

#a function to accept the number input. user has 3 attempts
def enternumber():
    n_num = 3
    while n_num > 0:
        try:
            tempvalue = float(input('enter number: '))
            break
        except ValueError:
            n_num -=1
            if n_num ==0:
                sys.exit('invalid input')
    return tempvalue

#function to accept operator
def enteroperator():
    n = 3
    while n > 0:
        tempaction = input('enter operator: ')
        if tempaction not in list(actions.keys()):
            n -= 1
            if n == 0:
                action = 'q'
            else:
                print('enter valid sign\n')
        else:
            action = tempaction.lower()
            break
    return action

#2 dummy functions to add restart and quit for our options. this help to avoid writing several if else
def restart():
    pass

def end():
    pass

actions = {'+':add, '-':subtract, "*":multiply, '/':divide, 'c':restart, 'q':end}
restarted = True
while restarted:
    keep_result = True
    num1 = enternumber()
    while keep_result:
        operator = enteroperator()
        if operator == 'q':
            print('Going off\n')
            restarted = False
            keep_result = False

        elif operator == 'c':
            print('New calculation started\n')
            keep_result = False
            continue
        else:
            num2 = enternumber()
            operation = actions[operator]
            result = operation(num1, num2)
            print(f'{num1} {operator} {num2} = {result}')
            num1 = result

