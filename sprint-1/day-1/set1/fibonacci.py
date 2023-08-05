n=10
fibonacci=[0,1]
while len(fibonacci)<n:
  fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)