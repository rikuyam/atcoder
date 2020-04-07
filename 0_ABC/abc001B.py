a=int(input())/1000
if a<0.1:
  ans=0
elif a<=5:
  ans=10*a
elif a<=30:
  ans=a+50
elif a<=70:
  ans=(a-30)//5+80
else:
  ans=89
ans=str(int(ans))
if len(ans)==1:
  ans="0"+ans
print(ans)
