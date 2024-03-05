cases = {3:'fizz', 5:'buzz'}

for i in range(1, 101):
  hit = False
  ans="";
  for j in cases:
    if(i%j==0):
      ans+=cases[j]
      hit = True
  if(not hit):
    ans+=str(i)
  print(ans)

