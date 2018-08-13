try:
    a=str(input("enter the name:"))
    b=input("enter the no:")
    c=a-b
except:
    print("mismatch type of value is added")
else:
    print(c)
finally:
    print("I am in finally")