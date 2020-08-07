#function to add 2 numbers
def add(x,y):
    return x+y
#function to sub 2 numbers
def sub(x,y):
    return x-y
#function to mul 2 numbers
def mul(x,y):
    return x*y
#function to mul 2 numbers
def div(x,y):
    return x/y
#to show the possible opearatiom
print("select the operation you want")
print("1.add 2 numbers")
print("2.subtract 2 numbers")
print("3.multiplying 2 numbers")
print("4.dividing 2 numbers")

while True:
    #taking input from user
    choice=input("enter the choice:[1,2,3,4] ")
    #to check the choice if it is 1 to 4
    if choice in['1','2','3','4']:
        num1=float(input("enter the first number"))
        num2 = float(input("enter the first number"))
        if choice=='1':
            print(num1,'+',num2,'=',add(num1,num2))
        elif choice == '2':
            print(num1, '-', num2, '=', sub(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', mul(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', div(num1, num2))
        break
    else:
        print('invalid input')






