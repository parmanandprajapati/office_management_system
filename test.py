def helper(str1):
    for i in str1:
	    if(i>='a' and i<='z') or (i>='A' and i<='Z') or i==' ':
		    pass
	    else:
		    return False
	return True
tc=int(input())
countV=0
countIn=0
for _ in range(tc):
 	str1=input()
    ans=helper(str1)
    if(ans):
    	counrV+=1
    else:
         countIn+=1
print(f"Count Of Valid Strings= {countV}")
print(f"Count Of Invalid Strings= {countIn}")