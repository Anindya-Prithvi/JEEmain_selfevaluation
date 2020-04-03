import time,os
l=0
while True:
    timed=time.time()
    while True:
        timeaft=time.time()
        if timeaft>=timed+60:
            l+=1
            print "A minute has passed; time passed=", l ,"minutes"
            ls=("|"*l)
            print ls.strip()
            break
        else:
            time.sleep(1)
