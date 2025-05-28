try:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    result=num1/num2
    print("result is:",result)
except ZeroDivisionError:
    print("division by 0 is not allowed")
except ValueError:
    print("please enter numerical value")

except:
    print("Some error occured") 
finally:
    print("Code run Sucessfully") 