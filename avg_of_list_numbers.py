file=open("AvgOfListNums.txt",'w')
abc=[1,2,3,4,5,6,7,8]
sum=0
i=0
while(i<len(abc)):
    sum=sum+abc[i]
    i=i+1
avg=sum/len(abc)
print('the average is:', avg)
file.write("the average of list numbers,")
file.write(str(avg))
file.close()