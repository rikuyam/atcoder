n=int(input())
a=[0 for _ in range(482)]

for _ in range(n):
  s,e=input().split("-")
  s=int(s[:2])*60+int(s[2:])//5*5
  e=int(e[:2])*60+int(e[2:])//5*5+5*(int(e[2:])%5>0)
  s//=5
  e//=5
  for i in range(s,e):
    a[i]=1
  if a[e]==0:
    a[e]=2
  
   
t=1
for i in range(0,482):
  if a[i]==t:
    if t==1:
      t=2
      ans1=str(i//12*100+i%12*5)
      if len(ans1)<4:
        ans1="0"*(4-len(ans1))+ans1
    else:
      t=1
      ans2=str((i)//12*100+(i)%12*5)
      if len(ans2)<4:
        ans2="0"*(4-len(ans2))+ans2
      print(ans1+"-"+ans2)