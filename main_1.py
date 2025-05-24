import random

secret_number = random.randint(1, 20)

for attempt in range(1, 6):
    try:
        guess = int(input(f"Попытка {attempt}: Угадай число от 1 до 20: "))

        if guess == secret_number:
            print("Поздравляю! Ты угадал число!")
            break
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    except ValueError:
        print("Пожалуйста, вводи только числа.")

else:
    print(f"Попытки закончились. Было загадано число {secret_number}")
