import math

def calculate_factorial(n):
    if n < 0:
        return "Ошибка: факториал не определяется для отрицательных чисел."
    else:
        return math.factorial(n)

def main():
    print("Введите положительное целое число:")
    user_input = input()
    
    if user_input.isdigit():
        number = int(user_input)
        if number < 0:
            print("Ошибка: введено отрицательное число.")
        else:
            result = calculate_factorial(number)
            print(f"Факториал числа {number} равен {result}")
    else:
        print("Ошибка: введены нечисловые данные. Пожалуйста, введите положительное целое число.")

main()