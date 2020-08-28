import numpy as np
import math


def main():
    print('***Basic Operator***')
    basic_operator = ['+','-','*','/'] #basisc operator
    print(basic_operator) 

    print('||Advance Operator ||')
    advance_operator = ['matrix','mean','median','sin','tan','cos','degress','radian','log','rint','lcm','gcd','sqrt','cbrt'] #advance
    print(advance_operator)  


    a = int(input("||Enter First Number||:"))  # first number
    op = input("||Enter Operator||:")  # operator like  + - / *
    b = int(input("||Enter Second Number||:"))  # second number

    a = np.array([(a)])  # making integer as a array first array
    b = np.array([(b)])  # making integer as a array second array


    def adding_num():  # function for adding first and second
        try:
            if op == '+':  # the user type + then ...
                print(f'**adding**: {np.add(a, b)}')  # adding two numbers
        except:
            pass  # passsing


    adding_num()  # calling the function


    def subtracting():  # function for subtracting first number and second number
        try:
            if op == '-':  # when user type - then... op == - then..
                print(f'**subtract**:{np.subtract(a, b)}')  # subtracting two numbers
        except:
            pass  # passsing


    subtracting()  # calling function


    def mutiplying():  # function for mutiplying first number and second number
        try:  # trying function
            if op == '*':  # if statment to check if user type * then.. else no answer
                print(f'**multiple**: {np.multiply(a, b)}')  # multiplying a and b
        except:
            pass  # passing


    mutiplying()  # calling the function


    def divdiing():  # function for divding first num and second num
        try:  # trying function
            if op == '/':  # if statement to check if the user type / so when we can print output they want
                print(f'**divdie**:{np.divide(a, b)}')  # dividing a and b
        except:
            pass  # passing


    divdiing()  # calling the function


    def finding_mean():  # function for finding mean of first num and second num
        try:  # trying function
            if op == 'mean':  # if statement to check if the user type mean so when we can print output they want
                print(f'**mean**:{np.mean((a, b))}')  # finding mean
        except:
            pass  # passing


    finding_mean()  # calling the function


    def finding_median():  # function for finding the median of a,b
        try:  # trying function
            if op == 'median':  # if statement to check if the user type median so when we can print output they want
                print(f'**median**:{np.median((a, b))}')
        except:
            pass  # passsing


    finding_median()  # calling the function


    def getting_matrix():  # function for matrix
        try:  # trying function
            if op == 'matrix':  # if statement to check if the user type matrix so when we can print output they want
                # getting the matrix of a and b
                print(f'||matrix||:{np.matrix((a, b))}')
        except:
            print('')
            pass


    getting_matrix()  # calling the function


    def getting_pi():  # function for getting pi
        try:  # trying function out try is good
            if op == 'pi':  # if statement to check if the user type ip so when we can print output they want
                print(np.pi(a, b))  # getting the pi of a  and b
        except:
            print('')  # empty string
            pass  # passing


    getting_pi()  # calling the function


    def finding_sin():  # function for finding sin
        try:  # try function
            if op == 'sin':  # if statement to check if the user type sin so when we can print output they want
                print(f'**sin**:{np.sin((a, b))}')  # showing the sin of a and b
        except:
            print('')  # empty print for no reason but looks good
            pass  # passing the function


    finding_sin()  # calling the function


    def finding_tan():  # function for finding tan
        try:  # trying function
            if op == 'tan':  # if statement to check if the user type tan so when we can print output they want
                print(f'**tan**:{np.tan((a, b))}')  # showing the tan of a and b
        except:
            print('')
            pass


    finding_tan()  # calling the function


    def finding_cos():  # function for finding cos
        try:  # trying function
            if op == 'cos':  # if statement to check if the user type cos so when we can print output they want
                print(f'cos:{np.cos((a, b))}')  # showing the cos of a and b
        except:
            print(
                'Sorry unfortunately we got an a error , give me 5 min to fix the error')
            pass  # passing


    finding_cos()  # calling the function


    def getting_the_degrees():  # function for getting the degrees
        try:  # trying function to get whatever i need
            if op == 'degrees':  # if statement to check if the user type degrees so when we can print output they want
                # showing the degrees of a and b
                print(f'**degress**:{np.degrees((a, b))}')
        except:
            print("")  # printting empty string if there any error
            pass  # pass


    getting_the_degrees()  # calling the function


    def radians_function_yes():  # function for getting the radians
        try:  # trying the function to get whatever god damn thing i need
            if op == 'radians':  # if statement for whatever some reason if manage to gget randian that why if user type randian we need to show them the radians of a and b ok
                # showing the radians of a and b
                print(f'**radians**:{np.radians((a, b))}')
        except:
            pass  # passing :)


    radians_function_yes()  # calling the function to work this function


    def log_promising():  # funciton for getting the log
        try:  # trying function
            if op == 'log':  # if statement to check if the user type log so when we can print output they want
                print(f'**log**:{np.log((a, b))}')  # showing the log of a and b
        except:
            print('Sorry undefined')


    log_promising()  # calling the function


    def rint_function():  # function for rint
        try:  # try method
            if op == 'rint':  # if user type rint then show the rint of a and b
                print(f'**rint**:{np.rint((a, b))}')  # showing the rint of a and b
        except:
            print("Sorry we got an error or u did a undefined ")
            pass


    rint_function()


    def lower_common_muitplie():  # function for getting the lcm
        try:  # try method
            if op == 'lcm':  # if user type lcm then show the rint of a and b
                print(f'**lcm**:{np.lcm(a, b)}')  # showing lcm of a and b
        except:
            print('Sorry undefined ..')
            pass  # passing


    lower_common_muitplie()  # calling the funciton


    def great_common_muitplie():  # function for gcd
        try:  # try method to get no error
            if op == 'gcd':  # if user type gcd then show the gcd of a and b
                print(f'**gcd**:{np.gcd(a, b)}')  # showing the gcd of a and b
        except:
            print('We got an error')
            pass  # passing


    great_common_muitplie()  # calling the function


    def sqrt_function():  # function for sqrt
        try:  # try method not to get error
            if op == 'sqrt':  # if user type sqrt then show the gcd of a and b
                print(f'sqrt{np.sqrt((a, b))}')  # showing the sqrt of a and b
        except:
            print("You have a mistake please check the mistake!")
            pass  # passing
    sqrt_function()

    def final_one():  # function for cbrt
        try:  # try method for no get error
            if op == 'cbrt':  # if user type cbrt then show the gcd of a and b
                print(f'**cbrt**:{np.cbrt((a, b))}') # showing the sqrt of a and b
        except:
                pass  # passing if there is any a error
    final_one()  # calling the function

main()