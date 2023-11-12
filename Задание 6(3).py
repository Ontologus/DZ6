a = int(input())
b = int(input())
c = int(input())
def maximum(a, b, c=0):
  if c == 0:
    if a > b:
      return a
    else:
      return b
  else:
    temp = a
    if b > temp:
      temp = b
    if c > temp:
      temp = c
    return temp
print(maximum(a, b, c))
#ввод переменных для проверки
