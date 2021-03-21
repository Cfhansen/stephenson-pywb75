###solution to exercise 75 from ben stephenson's "the python workbook".

x, y = input('Enter two integers:').split(',')
x = int(x)
y = int(y)

d = min(x,y)

while x % d or y % d:
  d -= 1

print(d)
