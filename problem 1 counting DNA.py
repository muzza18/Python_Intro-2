s=input("enter the sequence:")
print(s)
a,c,g,t=0,0,0,0
for i in s:
     if i=="A":
       a=a+1
     elif i=="T":
       t=t+1
     elif i=="G":
       g=g+1
     elif i=="C":
       c=c+1
print("A -",a)
print("C -",c)
print("G -",g)
print("T -",t)
