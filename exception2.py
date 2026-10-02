try:
    num1 = int(input("enter 1 number "))
    num2 = int(input("enter 2nd number "))
    num3 = num1 / num2
    print(num3)
except ZeroDivisionError as ex:
    print("exception", ex)
except ValueError as fx:
    print("error", fx)
except:
    print("wrong input")
else: 
    print("no exceptions")
finally:
    print("execute no matter what!!! ;)")