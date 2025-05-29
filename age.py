try:
    num=int(input("enter your age"))
except ValueError:
    print("Please enter a numerical value")
except:
    print("some error occured")
finally:
    print("Code run sucessfully")
