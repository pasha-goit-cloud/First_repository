#print('Hello World')
#print('hello Git')
#name = input('What is your name?')
#name = 'wendi\'s dog'
#print (name)
#name = input('база даних')
#print (name)
"""dict = {"key": "value"}
#У цьому словнику перераховано загальну кількість пунктів меню
menu_dict = {"sandwiches": {
        "price": 6,
        "description": "Зі свіжою шинкою та сиром"             
} ,
 "wraps": 4, "soup": 1}  """
#У цьому словнику перераховані елементи облікового запису користувача Instagram
"""user_dict = {"name": "Wendy", "active": False, "followers": 2}
print (menu_dict["sandwiches"]["description"], menu_dict["sandwiches"]["price"])
print (user_dict["active"])
menu = ["sandwich","soup","salad","wraps"]
for i in menu:
print (i) """
# Змініть вхідні дані на ціле число
'''age = int (input('How old are you now' ))
print('How old will you be next year?')
print(f"Next year you will be {age + 1}!")
#print(age + 1)'''
#*********************************************************
'''
item = input('Що ви купуєте ?')
price = float(input(f'яка ціна за 1кг {item} грн. ?'))
count = int(input('Скільки штук берете?'))
total = price*count
print ('-'*20)
print (f'Ваше замовлення {item}')
print (f'Сумма замовлення {total :.2f} грн.')
'''
#*********************************************************
'''
my_lucky_number = 7
guess = int(input('Guess my lucky number! I think it is: '))
while my_lucky_number != guess:
     guess = int(input('Oops! Not it. Try again: '))
print('Congrats! You guessed it.')'''
#*************************************************************
#x = ascii("My name is Ståle")
#print(x)
#************************************************************
#number = 45
#x = hex(number)
#print(x)
#**************************************************************
#   isalpha()	Чи тільки літери?
#   isdigit()	Чи тільки цифри?
#   isalnum()	Чи тільки літери АБО цифри?
#   islower()	Чи всі букви маленькі?

'''phone = input("Введіть номер: ")
if phone.isdigit():
    print("Дякую, обробляю номер...")
else:
    print("Помилка! Номер має містити лише цифри.")'''
#У функції print є прихований параметр sep (від англ. separator — розділювач).
#  За замовчуванням він дорівнює пробілу, але ми можемо змінити його на символ 
# переносу рядка \n
'''name = "Марія"  # str
age = 25  # int
weight = 60.5  # float
is_student = True  # bool

print(name, age, weight, is_student)
print(name + "\n" + str(age) + "\n" + str(weight))'''

''''
first_name = "John"
first_name1 = 12
last_name = "Doe"
last_name1 = "GGGG"

def get_initials(x, y, z, e):

    return last_name + " " + str(first_name1) + " " + first_name[0] + "." + " " + last_name1
formatted_name = get_initials(first_name, last_name, last_name1,first_name1)
print(formatted_name) '''


vegitabls = ["banans", "apple", "cherry", "kiwi"]
vegitabls.append ("shot")
vegitabls.insert(1,"shot")
print (vegitabls[0],vegitabls[1],vegitabls[2],vegitabls[3],vegitabls[-1])
print(vegitabls[-3])

vegitabls = [0, 0, 0, 0]
vegitabls.append (1)
vegitabls.insert(1,2)
print (vegitabls[0] + 245,vegitabls[1],vegitabls[2],vegitabls[3],vegitabls[-1])
print(vegitabls[-3])
