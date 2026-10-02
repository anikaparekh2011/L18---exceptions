valid = True

while valid:
    try:
        num = int(input("enter a number; "))
        while num % 2 == 0:
            print("bye bye")
        else:
                valid = False
                num = int(input("enter a number; "))
        
    except:
        print("invalid!!")        
    
