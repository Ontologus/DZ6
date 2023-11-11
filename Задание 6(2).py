def reg():
  last_name = input('Введите фамилию ')
  first_name = input('Ввдите имя ')
  patronymic = input('Введите отчество ')
  age = input('Введите возраст ')
  birth_year = 2023 - int(age)
  res = (last_name, first_name, patronymic, str(birth_year), 'г.р.', 'зарегистрирован')
  return ' '.join(res)
print(reg())
