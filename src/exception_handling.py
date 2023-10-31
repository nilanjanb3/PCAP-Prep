def fun1(age):
    if age<18 :
        raise Exception("Not eligable for vote")
    else:
        print("Welcome to vote...")
    

try:
    fun1(17)
except Exception as e:
    print(e)