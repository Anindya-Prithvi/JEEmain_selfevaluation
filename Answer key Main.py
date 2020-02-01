def attempt_counter(uint):
    count=0
    for i in uint:
        if i!=None and i!="None" and i!="*":
            count+=1
    return count

def mfr(uint):
    temp=''
    for i in range(1,76,1):
        if uint[i]=='*':
            temp+=str(i)+','
    return temp+"..."

import time
test_name=str(raw_input("Enter the name of test: "))
answer_key=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]

answer_key[0]=test_name
print """
To terminate type TERMINATE
To mark for review an answer type * in the input for the specific question"""
prompt=str(raw_input("Would you like to start your test? (y/n): "))
if prompt=="y":
    start=time.time()
    while True:
        reqt=time.time()
        end=time.time()
        response=(raw_input("Enter question number: "))
        if response=="TERMINATE":
            break
        elif response=="SHOWKEY":
            print answer_key
        key=(raw_input("Enter your answer (A/B/C/D) or Number :"))
        try:
            response=int(response)
            key=str(key)
            answer_key[response]=key
        except:
            print """

ERROR HAS OCCURED
LAST ANSWER HAS NOT BEEN UPDATED
Probable errors:
        1.Question number is greater than 75
        2.Question number is alphanumeric
        3.Uncaught Error
"""
        end=time.time()
        print "Time elapsed so far is ",end-start,"seconds"
        print "Time elapsed in the current question =",end-reqt,"seconds"
        print "Number of attempts so far :",attempt_counter(answer_key)-1
        print "The Questions marked for review are",mfr(answer_key)
        if end>=start+10800:
            break
else:
    while True:
        print "Close program"
print answer_key
print "Time elapsed so far is ",end-start,"seconds out of 10800"
fileis= test_name+".akey"
savekey=open(fileis,"w")
savekey.write(str(answer_key))
savekey.close()
execfile('Analyzer.py')
