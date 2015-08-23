#######This script tests the behaviour of api : https://www.calcatraz.com/calculator/api?c=[number][operator][number] e.g:- https://www.calcatraz.com/calculator/api?c=3%2B3 with respect to addition operation

import urllib2
import random
import sys
import datetime
import re
import string
import os

global resultdir
global tcpassed
global tcfailed
global tccount

def Report():
	global tccount
	global tcpassed
	global tcfailed
	fout=open(resultdir,'a');
	fout.write("\n\n*****************************\n");
	fout.write("\nTotal Test Cases Executed : "+str(tccount));
	fout.write("\nTotal Test Cases Passed : "+str(tcpassed));
	fout.write("\nTotal Test Cases Failed : "+str(tcfailed));
	fout.write("\n\n*****************************\n");
	fout.close();



def integerAddition (op1,op2):
	try:
		global resultdir
		global tccount
		global tcpassed
		global tcfailed
		fout=open(resultdir,'a');
		url="https://www.calcatraz.com/calculator/api?c="+str(op1)+"%2B"+str(op2);
		getRequest=urllib2.urlopen(url);
		respData=getRequest.read();
		respData=respData.replace(" ","");		
		
		respCode=getRequest.getcode();
		result=int(op1)+int(op2);
		if(result<=0):
			if((respCode==200)and respData==""):
				resultString=str(op1)+"+"+str(op2)+":"+"Passed ---- API:"+str(respData)+",Manual:"+",Status code:"+str(respCode)+"\n";
				print resultString;
				tcpassed=tcpassed+1;
				fout.write(resultString);
				fout.close();
				return;
			else:
				resultString=str(op1)+"+"+str(op2)+":"+"Failed ---- API:"+str(respData)+",Manual:"+",Status code:"+str(respCode)+"\n";
				print resultString;
				tcfailed=tcfailed+1;
				fout.write(resultString);
				fout.close();
				return;
		
		
		
		respData=float(respData);
		difference=result-respData;
		differencepercentage=(difference/result)*100;
		
		if((respCode==200)and (abs(differencepercentage) < 0.001)):
			resultString=str(op1)+"+"+str(op2)+":"+"Passed ---- API:"+str(respData)+",Manual:"+str(result)+",Difference:"+str(difference)+"("+str(differencepercentage)+")"+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcpassed=tcpassed+1;
		else:
			resultString=str(op1)+"+"+str(op2)+":"+"Failed ---- API:"+str(respData)+",Manual:"+str(result)+",Difference:"+str(difference)+"("+str(differencepercentage)+")"+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcfailed=tcfailed+1;
		
		fout.write(resultString);
		fout.close();
	except Exception as e:
			e = sys.exc_info();
			resultString=str(op1)+"+"+str(op2)+":"+str(e)+":Failed\n";
			print resultString;
			fout.write(resultString);	
			fout.close();
	
def generalAddition(op1,op2,expected):
	try:
		global resultdir
		global tccount
		global tcpassed
		global tcfailed
		fout=open(resultdir,'a');
		url="https://www.calcatraz.com/calculator/api?c="+str(op1)+"%2B"+str(op2);
		getRequest=urllib2.urlopen(url);
		respData=getRequest.read();
		respData=respData.replace(" ","");		
		respData=respData;
		respCode=getRequest.getcode();
		
		if(respData==""):
			if((respCode==200)and respData==expected):
				resultString=str(op1)+"+"+str(op2)+":"+"Passed ---- API:"+str(respData)+",Manual:"+str(expected)+",Status code:"+str(respCode)+"\n";
				print resultString;
				tcpassed=tcpassed+1;
				fout.write(resultString);
				fout.close();
				return;
			else:
				resultString=str(op1)+"+"+str(op2)+":"+"Failed ---- API:"+str(respData)+",Manual:"+str(expected)+",Status code:"+str(respCode)+"\n";
				print resultString;
				tcfailed=tcfailed+1;
				fout.write(resultString);
				fout.close();
				return;
					
		difference=float(expected)-float(respData);
		differencepercentage=(difference/expected)*100;
		
		if((respCode==200)and (abs(differencepercentage) < 0.001)):
			resultString=str(op1)+"+"+str(op2)+":"+"Passed ---- API:"+str(respData)+",Manual:"+str(expected)+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcpassed=tcpassed+1;
		else:
			resultString=str(op1)+"+"+str(op2)+":"+"Failed ---- API:"+str(respData)+",Manual:"+str(expected)+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcfailed=tcfailed+1;
		
		fout.write(resultString);
		fout.close();
	except Exception as e:
			e = sys.exc_info();
			resultString=str(op1)+"+"+str(op2)+":"+str(e)+":Failed\n";
			print resultString;
			fout.write(resultString);	
			fout.close();
		
def stringAddition(op1,op2,expected):
	try:
		global resultdir
		global tccount
		global tcpassed
		global tcfailed
		fout=open(resultdir,'a');
		url="https://www.calcatraz.com/calculator/api?c="+str(op1)+"%2B"+str(op2);
		getRequest=urllib2.urlopen(url);
		respData=getRequest.read();
		respData=respData.replace(" ","");		
		respData=respData;
		respCode=getRequest.getcode();
		
		if((respCode==200)and respData==expected):
			resultString=str(op1)+"+"+str(op2)+":"+"Passed ---- API:"+str(respData)+",Manual:"+str(expected)+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcpassed=tcpassed+1;
			
		else:
			resultString=str(op1)+"+"+str(op2)+":"+"Failed ---- API:"+str(respData)+",Manual:"+str(expected)+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcfailed=tcfailed+1;
			
		fout.write(resultString);	
		fout.close();	
	
	except Exception as e:
			e = sys.exc_info();
			resultString=str(op1)+"+"+str(op2)+":"+str(e)+":Failed\n";
			print resultString;
			fout.write(resultString);	
			fout.close();
		
def floatAddition (op1,op2):
	try:
		global resultdir
		global tccount
		global tcpassed
		global tcfailed
		fout=open(resultdir,'a');
		url="https://www.calcatraz.com/calculator/api?c="+str(op1)+"%2B"+str(op2);
		getRequest=urllib2.urlopen(url);
		respData=getRequest.read();
		respData=respData.replace(" ","");		
		
		respCode=getRequest.getcode();
		result=op1+op2;
		if(result<0):
			if((respCode==200)and respData==""):
				resultString=str(op1)+"+"+str(op2)+":"+"Passed ---- API:"+str(respData)+",Manual:"+",Status code:"+str(respCode)+"\n";
				print resultString;
				tcpassed=tcpassed+1;
				fout.write(resultString);
				fout.close();
				return;
			else:
				resultString=str(op1)+"+"+str(op2)+":"+"Failed ---- API:"+str(respData)+",Manual:"+",Status code:"+str(respCode)+"\n";
				print resultString;
				tcfailed=tcfailed+1;
				fout.write(resultString);
				fout.close();
				return;
		respData=float(respData);
		result=round(result,5);
		difference=result-respData;
		differencepercentage=(difference/result)*100;
		if((respCode==200)and (abs(differencepercentage) < 0.001)):
			resultString=str(op1)+"+"+str(op2)+":"+"Passed ---- API:"+str(respData)+",Manual:"+str(result)+",Difference:"+str(difference)+"("+str(differencepercentage)+")"+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcpassed=tcpassed+1;
		else:
			resultString=str(op1)+"+"+str(op2)+":"+"Failed ---- API:"+str(respData)+",Manual:"+str(result)+",Difference:"+str(difference)+"("+str(differencepercentage)+")"+",Status code:"+str(respCode)+"\n";
			print resultString;
			tcfailed=tcfailed+1;
		
		fout.write(resultString);
		fout.close();
	except Exception as e:
			e = sys.exc_info();
			resultString=str(op1)+"+"+str(op2)+":"+str(e)+":Failed\n";
			print resultString;
			fout.write(resultString);	
			fout.close();	



tccount=0	
tcpassed=0
tcfailed=0
if not os.path.exists(r'c:\Python27\OpenTable\Results'): 
	os.makedirs(r'c:\Python27\OpenTable\Results')


### Creating Result file for individual test iteration ###
resultdir="Results\\"+str(datetime.datetime.now())
resultdir=resultdir.replace(" ","");
resultdir=resultdir.replace(".","-");
resultdir=resultdir.replace(":","-");
fout=open(resultdir,"w");
fout.close();
#####################################################





##### Small integer number addition test #####	
i=0;

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.randint(1,100)*sign;
	op2=random.randint(1,100)*sign;
	tccount=tccount+1;
	integerAddition(op1,op2);

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.randint(1000,65535)*sign;
	op2=random.randint(1000,65535)*sign;
	tccount=tccount+1;
	integerAddition(op1,op2);

###############################################

##### Semi Large integer number addition test #####	
i=0;

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.randint(100000,1000000000)*sign;
	op2=random.randint(100000,1000000000)*sign;
	tccount=tccount+1;
	integerAddition(op1,op2);


##### Very Large integer number addition test #####	
i=0;

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.randint(1000000000,100000000000)*sign;
	op2=random.randint(1000000000,100000000000)*sign;
	tccount=tccount+1;
	integerAddition(op1,op2);

'''

'''
##### Addition with zeros test ######
no=[+1,-1]	;
sign=random.choice(no);
op1=random.randint(1,1000000000)*sign;
op2=0;
tccount=tccount+1;
integerAddition(op1,op2);

##### Addition with zero as negative string in url and as second operand  ######
no=[+1,-1]	;
sign=random.choice(no);
op1=random.randint(1,1000000000)*sign;
op2='-0';
tccount=tccount+1;
integerAddition(op1,op2);



sign=random.choice(no);
op1=0;
op2=random.randint(1,10000000000)*sign;
tccount=tccount+1;
integerAddition(op1,op2);

##### Addition with zero as negative string in url  and first operand ######
no=[+1,-1]	;
sign=random.choice(no);
op2=random.randint(1,1000000000)*sign;
op1='-0';
tccount=tccount+1;
integerAddition(op1,op2);



##### Addition of two zeros test ######
op1=0;
op2=0;
tccount=tccount+1;
generalAddition(op1,op2,"");

##### Addition with zeros as negative string in url as first and second operand ######

op2='-0';
op1='-0';
tccount=tccount+1;
integerAddition(op1,op2);



##### No operands test  ######
op1='';
op2='';
tccount=tccount+1;
generalAddition(op1,op2,'');

##### One operand Blank test  ######
op1=random.randint(1,100000000000);
op2='';
tccount=tccount+1;
generalAddition(op1,op2,op1);

op2=random.randint(1,100000000000);
op1='';
tccount=tccount+1;
generalAddition(op1,op2,op2);



##### String Addition test  ######
i=0
for i in range(0,20):
	op1=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op2=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');


##### String and positive integer number addition test #####
i=0
for i in range(0,10):
	op1=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op2=random.randint(1,100000000000);
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');
for i in range(0,10):
	op2=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op1=random.randint(1,100000000000);
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');


##### String and negative integer number addition test #####
i=0
for i in range(0,10):
	op1=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op2=random.randint(1,100000000000)*-1;
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');
for i in range(0,10):
	op2=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op1=random.randint(1,100000000000)*-1;
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');



##### Small float number addition test #####	
i=0;

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.uniform(1,100)*sign;
	op2=random.uniform(1,100)*sign;
	tccount=tccount+1;
	floatAddition(op1,op2);

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.uniform(1000,65535)*sign;
	op2=random.uniform(1000,65535)*sign;
	tccount=tccount+1;
	floatAddition(op1,op2);

###############################################

##### Semi Large Float number addition test #####	
i=0;

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.uniform(100000,1000000000)*sign;
	op2=random.uniform(100000,1000000000)*sign;
	tccount=tccount+1;
	floatAddition(op1,op2);


##### Very Large Float number addition test #####	
i=0;

for i in range(0,20):
	
	no=[+1,-1]	;
	sign=random.choice(no);
	op1=random.uniform(1000000000,100000000000)*sign;
	op2=random.uniform(1000000000,100000000000)*sign;
	tccount=tccount+1;
	floatAddition(op1,op2);



##### Small float and integer number addition test #####	
i=0;

for i in range(0,10):
	
	op1=random.uniform(1,100);
	op2=random.randint(1,100);
	tccount=tccount+1;
	floatAddition(op1,op2);

for i in range(0,10):
	
	op2=random.uniform(1000,65535);
	op1=random.randint(1000,65535);
	tccount=tccount+1;
	floatAddition(op1,op2);

###############################################

##### Semi Large float and integer number addition test #####	
i=0;

for i in range(0,10):
	
	op1=random.uniform(100000,1000000000);
	op2=random.randint(100000,1000000000);
	tccount=tccount+1;
	floatAddition(op1,op2);
	
for i in range(0,10):
	
	op2=random.uniform(100000,1000000000);
	op1=random.randint(100000,1000000000);
	tccount=tccount+1;
	floatAddition(op1,op2);


##### Very Large float integer number addition test #####	
i=0;

for i in range(0,10):
	
	op1=random.uniform(1000000000,100000000000);
	op2=random.randint(1000000000,100000000000);
	tccount=tccount+1;
	floatAddition(op1,op2);
	
for i in range(0,10):
	
	op2=random.uniform(1000000000,100000000000);
	op1=random.randint(1000000000,100000000000);
	tccount=tccount+1;
	floatAddition(op1,op2);



##### String and positive float number addition test #####
i=0
for i in range(0,10):
	op1=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op2=random.uniform(1,100000000000);
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');
for i in range(0,10):
	op2=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op1=random.uniform(1,100000000000);
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');
	


##### String and negative float number addition test #####
i=0
for i in range(0,10):
	op1=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op2=random.uniform(1,100000000000)*-1;
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');
for i in range(0,10):
	op2=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits +'!@#$%^&*') for _ in range(random.randint(1,10)));
	op1=random.uniform(1,100000000000)*-1;
	tccount=tccount+1;
	stringAddition(op1,op2,'answer');


Report();	



