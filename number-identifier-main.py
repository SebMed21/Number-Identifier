
#define function
# compare the variables using relational operators
def identifier(num1, num2, num3, num4, num5):

        if num1 > num2 and num1> num3 and num1 > num4 and num1 > num5:
            return(num1)
        elif num2 > num3 and num2 > num4 and num2 > num5:
            return (num2)
        elif num3 > num4 and num3 > num5:
            return (num3)
        elif num4 > num5:
            return (num4)
        else: 
            return (num5)
        
#input values of the variables

num1 = int(input("Input the first number: "))
num2 = int(input("Input the second number: "))
num3 = int(input("Input the third number: "))
num4 = int(input("Input the fourth number: "))
num5 = int(input("Input the fifth number: "))

#call the defined function
largest_number = identifier(num1, num2, num3, num4, num5)

#display the larguest number
print(f"The largest number in the given list is : {largest_number}")

