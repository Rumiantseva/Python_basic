name = int(input("Введите имя "))
surname = int(input("Введите фамилию "))
year = int(input("Введите год рождения "))
city = int(input("Введите год рождения "))
email = input('enter email')
telephone = input('input telephone')
def my_func(name, surname, year, city, email, telephone):
return join([name," .", surname," .", year," .", city," .", email," .", telephone])
'''
print(my_func(surname = 'Rumiantseva', name = 'Tatiana', year = '1994', city = 'Moscow', email = 'rumitat@gmail.com', telephone = '8-925-999-99-88'))