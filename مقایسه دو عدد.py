L1=input("enter list 1 :")
L2=input("enter list 2 :")
L3=[]
count=0
print(L1,L2)
for i in range(0,len(L1)) :
    if L1[i]!=L2[i]:
        count+=1
        L3.append(i+1)
print("Number of inequalities :", count)
print("Place this number : ",L3)
Exit=input("Press Enter to exit .")