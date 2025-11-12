import math
import logging
from datetime import datetime

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate_compound_interest(principal, rate, years, n=12):
    if principal <= 0 or rate <= 0 or years <= 0:
        raise ValueError("Все значения должны быть положительными.")

    try:
        r = rate / 100
        amount = principal * (1 + r / n) ** (n * years)
        return round(amount, 2)
    except Exception as e:
        logging.error(f"Ошибка при расчете: {e}")
        raise

def main():
    print("=== Финансовый калькулятор ===")
    try:
        principal = float(input("Введите сумму вклада: "))
        rate = float(input("Введите годовую процентную ставку (%): "))
        years = float(input("Введите срок вклада (в годах): "))

        final_amount = calculate_compound_interest(principal, rate, years)
        print(f"\nИтоговая сумма через {int(years)} лет: {final_amount} тенге")

        with open('result.txt', 'w', encoding='utf-8') as f:
            f.write(f"Вклад: {principal} тг\n")
            f.write(f"Ставка: {rate}%\n")
            f.write(f"Срок: {years} лет\n")
            f.write(f"Итоговая сумма: {final_amount} тг\n")

        print("\nРабота программы завершена. Результат записан в result.txt")

    except ValueError as ve:
        print("Ошибка: неверный ввод данных.")
        logging.error(f"Ошибка при вводе данных: {ve}")

    except Exception as e:
        print("Произошла непредвиденная ошибка. Подробнее в errors.log.")
        logging.error(f"Непредвиденная ошибка: {e}")

    finally:
        print("\nСпасибо за использование финансового калькулятора!")

if __name__ == "__main__":
    main()