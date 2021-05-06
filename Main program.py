#made by Anindya Prithvi
#son of Biplab Kumar Naskar and Anindita Naskar

import os,qwa
os.startfile(r"te.py")

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

import time

test_name=str(input("Enter the name of test: "))
answer_key=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
time_key=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
answer_key[0]=test_name
fileis= test_name+".akey"
print("""
To terminate type TERMINATE (in place of question number)
To mark for review an answer type * in the input for the specific question
To see key type SHOWKEY""")
prompt=str(input("Would you like to start your test? (y/n): "))
if prompt=="y" or prompt=="Y":
    start=time.time()
    while True:
        reqt=time.time()
        end=time.time()
        response=(input("\nEnter question number: "))
        if response=="TERMINATE":
            break
        elif response=="SHOWKEY":
            print(answer_key)
        key=(input("Enter your answer (A/B/C/D) or Number :"))
        try:
            response=int(response)
            key=str(key)
            answer_key[response]=key
            end=time.time()
            time_key[response-1]=(end-reqt)/60
        except:
            print("""

ERROR HAS OCCURED
LAST ANSWER HAS NOT BEEN UPDATED
Probable errors:
        1.Question number is greater than 75
        2.Question number is alphanumeric
        3.This error cant be traced
""")
        end=time.time()
        print( "Time elapsed so far is ",end-start,"seconds")
        print( "Time elapsed in the current question =",end-reqt,"seconds")
        print( "Number of attempts so far :",attempt_counter(answer_key)-1)
        print( "The Questions marked for review are",mfr(answer_key))
        auto_sav(fileis)
        if end>=start+10800:
            break
else:
    while True:
        print("Close program")
print("This is the answer key--> \n",answer_key,'\n and this is the time taken in every question', time_key)
print("Time elapsed so far is ",end-start,"seconds out of 10800")
fileis= test_name+".akey"
savekey=open(fileis,"w")
savekey.write(str(answer_key))
savekey.close()
print("OPENING ANALYZER")
qwa.analyzergraph(test_name,time_key)
os.startfile('Analyzer.py')
print("\nYou can close this now OR it will close automatically \nin 60 seconds")
time.sleep(60)
