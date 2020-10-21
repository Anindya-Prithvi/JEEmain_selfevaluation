import time
analysis=open("Analysis.txt","a")
punch=time.time()
punch=time.ctime(punch)
punch=str(punch)
testname=str(input("Enter the name of the test:"))
testname="TEST NAME: "+ testname
comments="COMMENTS : "+ str(input("Enter comments for the test:"))
weak="WEAK TOPICS :"+ str(input("Weak topics :"))
strong="STRONG TOPICS :"+ str(input("Strong topics :"))
work="CAN WORK ON :"+str(input("CAN BE WORKED UPON :"))
note="Special Note :"+str(input("Enter any notes for the test :"))
analyzed="\n"+punch + "\n" +testname+"\n"+comments+"\n"+strong+"\n"+weak+"\n"+work+"\n"+note+"\n"+"Evaluation Ended"+"\n"
print(analyzed)
analysis.write(analyzed)
print("written in Analysis.txt")
