from random import choice

with open("list_words.txt", "r", encoding="utf-8") as words_file:
    words = words_file.readlines()

play = "Да"
while play.lower() == "да":  # ДА да Да дА upper/lower

    word_with_hint = choice(words).split("|")
    word = word_with_hint[0]  # рандомно выбранное слово из файла
    hint = word_with_hint[1]  # подсказка (пользователю) к этому слову

    attempt = 5  # количество попыток
    print(hint)
    # + * len()
    # "2" * len(...) = "222"
    cipher = "_" * len(word)  # зашифрованное слово, которое будет угадывать пользователь
    print(cipher)
    while cipher.count("_") > 0:
        letter = input("Введите одну букву: ")  # буква которую введет пользователь
        while len(letter) > 1 or letter.isalpha() == False:
            print("Не верный ввод данных, попробуйте снова")
            letter = input("Введите одну букву: ")
        # авто -> т "авто".count("т") > 0 ____ т -> __т_
        # т in авто -> True, False
        if letter in word:
            for i in range(len(word)):
                if letter == word[i]:
                    cipher = cipher[:i] + letter + cipher[i + 1:]
            print("Буква угадана\n" + cipher)
        else:
            print("Этой буквы нет в этом слове")
            attempt -= 1
            if attempt == 0:
                print("Вы проиграли!")
                break
            print(f'У Вас осталось попыток: {attempt}')
    else:
        print("Поздравляю, слово угаданно! Продолжаем Игру? Да/Нет")
    play = input()
