def palindrom():
  s = input()
  if s.lower() == s[::-1].lower():
    return True
  else:
    return False
print(palindrom())
#одинаковые буквы разного регистра считаются одинаковыми