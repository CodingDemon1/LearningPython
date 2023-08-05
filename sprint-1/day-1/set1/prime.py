n=14
flag=0
if n < 2:
  flag=1
for i in range(2, n):
  if n % i == 0:
      flag=1
if flag==0:
  print(f"{n} is Prime number")
else:
  print(f"{n} is not Prime number")