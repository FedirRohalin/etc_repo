import sys

def calculate_sum(n):
    if n < 0:
        raise ValueError("Число n не може бути меншим за 0")
    
    result = (n / 2) * (2 * 1 + (n - 1) * 3)
    return int(result)

if __name__ == "__main__":
    try:
        user_input = input("Введіть кількість членів прогресії (n): ")
        n = int(user_input)
        print(f"Сума перших {n} членів: {calculate_sum(n)}")
    except ValueError as e:
        print(f"Помилка: {e}")
        sys.exit(1)