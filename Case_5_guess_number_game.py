import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5

    print("Я загадал число от 1 до 100. Попробуй угадать его!")

    while attempts > 0:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            
            if user_guess < 1 or user_guess > 100:
                print("Пожалуйста, введите число в диапазоне от 1 до 100.")
                continue

            if user_guess == number_to_guess:
                print("Поздравляю! Вы угадали число.")
                break
            elif user_guess < number_to_guess:
                print("Слишком маленькое число.")
            else:
                print("Слишком большое число.")
            
            attempts -= 1
            print(f"У вас осталось {attempts} попыток.")
        
        except ValueError:
            print("Ошибка: введено не число. Пожалуйста, введите целое число.")
    
    if attempts == 0:
        print(f"Вы проиграли. Загаданное число было {number_to_guess}.")

guess_number_game()