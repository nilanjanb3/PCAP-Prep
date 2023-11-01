file = open("./src/sample.txt","r")
try:
    lines = file.readlines()
    for line in lines:
        print(line)
except Exception as e:
    print("Exception Occured: ",e)
finally:
    file.close()