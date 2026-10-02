try:
    num = int(input("enter a number: "))
    print(num)
except ValueError as ex:
    print("wrong")
    print("error", ex)
    
