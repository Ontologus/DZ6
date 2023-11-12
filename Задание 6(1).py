s = input()
def palindrom(s):
  if s.lower() == s[::-1].lower():
    return True
  else:
    return False
print(palindrom(s))
#одинаковые буквы разного регистра считаются одинаковыми
#сделал ввод снаружи, т.к увидел информацию в тг
