dir,w=map(int,input().split())
if w/60<0.25:
  d="C"
else:
  if 112<dir<338:
    d="NNE"
  elif 337<dir<563:
    d="NE"
  elif 562<dir<788:
    d="ENE"
  elif 787<dir<1013:
    d="E"
  elif 1012<dir<1238:
    d="ESE"
  elif 1237<dir<1463:
    d="SE"
  elif 1462<dir<1688:
    d="SSE"
  elif 1687<dir<1913:
    d="S"
  elif 1912<dir<2138:
    d="SSW"
  elif 2137<dir<2363:
    d="SW"
  elif 2362<dir<2588:
    d="WSW"
  elif 2587<dir<2813:
    d="W"
  elif 2812<dir<3038:
    d="WNW"
  elif 3037<dir<3263:
    d="NW"
  elif 3262<dir<3488:
    d="NNW"
  else:
    d="N"
    
if w/60<0.25:
  w=0
elif w/60<1.55:
  w=1
elif w/60<3.35:
  w=2
elif w/60<5.45:
  w=3
elif w/60<7.95:
  w=4
elif w/60<10.75:
  w=5
elif w/60<13.85:
  w=6
elif w/60<17.15:
  w=7
elif w/60<20.75:
  w=8
elif w/60<24.45:
  w=9
elif w/60<28.45:
  w=10
elif w/60<32.65:
  w=11
else:
  w=12
  
print(d,w)
