name_person = (input('Digite seu nome:'))

city_of_birth = (input('Digite a sua cidade de nascimento:'))

year_of_birth = int((input('Digite seu ano de nascimento:')))

print(f'Seu nome é: {name_person}')
print(f'Sua cidade de nascimento é: {city_of_birth}')
print(f'Seu ano de nascimento é {year_of_birth}')

age_in_2030 = 2030 - year_of_birth

print(f'Em 2030 você terá {age_in_2030} anos.')