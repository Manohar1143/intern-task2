def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("select operation:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

while True:
    choice=input("Enter choice (1/2/3/4):")
    if choice in('1','2','3','4'):
        try:
            num1=float(input("enter a number:"))
            num2=float(input("enter b number:"))
        except ValueError:
            print("invalid")
            continue

        if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))
        if choice =='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        if choice =='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        if choice =='4':
            print(num1,"/",num2,"=",divide(num1,num2))

        next_cal=input(" do you want next cal?(yes/no):")
        if next_cal=="no":
            break
    else:
        print("invalid input")
            
            
