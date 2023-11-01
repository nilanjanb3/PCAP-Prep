import os
import subprocess

print(os.getcwd()) # current working directory
res = os.system("pwd")
print(res)

print(subprocess.run("pwd", shell=True))

res = subprocess.check_output("pwd", text=True)
print(res)