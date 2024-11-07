correct_answers = 0

while True:
    user_answer = input("Какая версия языка сейчас актуальна? ")
    if user_answer.lower() == "python3":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")

while True:
    user_answer = input("Какая кодировка используется в строках? ")
    if user_answer.lower() == "utf8":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")
correct_answers = 0

while True:
    user_answer = input("Какая версия языка сейчас актуальна? ")
    if user_answer.lower() == "python3":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")

while True:
    user_answer = input("Какая кодировка используется в строках? ")
    if user_answer.lower() == "utf8":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")
while True:
    user_answer = input("Какой тип данных используется для хранения целых чисел? ")
    if user_answer.lower() == "int":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")

while True:
    user_answer = input("Какой метод используется для получения длины строки? ")
    if user_answer.lower() == "len":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")

while True:
    user_answer = input("Какая функция превращает строку в число? ")
    if user_answer.lower() == "int":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")

while True:
    user_answer = input("Как называется операция сложения строк? ")
    if user_answer.lower() == "конкатенация":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")

while True:
    user_answer = input("Какой цикл используется для перебора элементов? ")
    if user_answer.lower() == "for":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")
while True:
    user_answer = input("Как называется функция для преобразования числа в строку?")
    if user_answer.lower() == "str":
        print(f"Ответ {user_answer} верен")
        correct_answers += 1
        break
    else:
        print("Неверный ответ.")


print(f"Вы ответили правильно на {correct_answers} из 10 вопросов.")


