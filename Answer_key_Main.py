import os,qwa
os.startfile(r"C:\Users\B K NASKAR\Desktop\OMR input on py\te.py")

def auto_sav(fileis):
    savekey=open(fileis,"w")
    savekey.write(str(answer_key))

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
"""def marked_for_rev(uint):
    i=1
    temp=""
    while i<=75:
        if uint[i]=="*":
            temp+=" "+str(i)
        else:
            i+=1
"""

import time
test_name=str(raw_input("Enter the name of test: "))
answer_key=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
time_key=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
qwa.analyzergraph(test_name,time_key)
answer_key[0]=test_name
fileis= test_name+".akey"
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
            end=time.time()
            time_key[response]=(end-reqt)/60
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
        auto_sav(fileis)
        if end>=start+10800:
            break
else:
    while True:
        print "Close program"
print answer_key, time_key
print "Time elapsed so far is ",end-start,"seconds out of 10800"
fileis= test_name+".akey"
savekey=open(fileis,"w")
savekey.write(str(answer_key))
savekey.close()
print "OPENING ANALYZER"
qwa.analyzergraph(test_name,time_key)
execfile('Analyzer.py')
