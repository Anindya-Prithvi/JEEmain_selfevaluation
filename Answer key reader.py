import os
import time

def t():
    m=str(input("Enter name of the answer key (case sensitive): "))
    try:
        f=open(m,'r')
        return f
    except:
        try:
            f=open(m+".akey",'r')
            return f
        except:
            print("Write correctly")
            t()

a=t().read()
with open('k.py','w') as g:
    g.write("a="+a)
from k import a
print("The name of the question set is ",a[0])
for i in range(0,75):
    print("The answer given for question number" ,i+1,"is",a[i+1])
os.remove('k.py')
time.sleep(10000000)
