print("Завдання 1")

import math


def main():
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    sum_squares = a**2 + b**2 + c**2

    average = (a + b + c) / 3

    discriminant = b**2 - 4 * a * c

    hypotenuse = math.sqrt(a**2 + b**2)

    is_triangle = (
        a > 0 and b > 0 and c > 0
        and a + b > c
        and a + c > b
        and b + c > a
    )

    print("Додаткові операції:")
    if b != 0 and c != 0:
        print(f"a / b = {a / b:.2f}")
        print(f"a // b = {a // b:.2f}")
        print(f"a % b = {a % b:.2f}")
    else:
        print("Ділення на нуль неможливе.")

    print(f"a - b = {a - b:.2f}")
    print(f"a * c = {a * c:.2f}")

    print("Результати обчислень:")
    print(f"Сума квадратів: {sum_squares:.2f}")
    print(f"Середнє арифметичне: {average:.2f}")
    print(f"Дискримінант: {discriminant:.2f}")
    print(f"Гіпотенуза: {hypotenuse:.2f}")
    print(f"Чи утворюють числа трикутник: {is_triangle}")


if __name__ == "__main__":
    main()

    print("\n")
    
def main():
    raw_input = input("Введіть число: ")

    print("Перетворення типів:")

    try:
        integer_value = int(raw_input)
        print(f"Ціле число: {integer_value}")
        print(f"Тип: {type(integer_value)}")
    except ValueError:
        print("Неможливо перетворити введення на int.")

    try:
        float_value = float(raw_input)
        print(f"Дійсне число: {float_value}")
        print(f"Тип: {type(float_value)}")

        print(f"Булеве значення: {bool(float_value)}")
    except ValueError:
        print("Неможливо перетворити введення на float.")

    text_value = str(raw_input)
    print(f"Рядкове значення: {text_value}")
    print(f"Тип: {type(text_value)}")

    name = input("Введіть ім'я: ")
    age = int(input("Введіть вік: "))

    print("Інформація:")
    print(f"Ім'я: {name:<15}")
    print(f"Вік: {age:03d}")
    print(f"Наступного року буде: {age + 1} років")

    numbers = list(range(1, 11))

    print("\nРобота зі списком:")
    print(f"Список: {numbers}")
    print(f"Кількість елементів: {len(numbers)}")
    print(f"Ідентифікатор об'єкта: {id(numbers)}")

    print(f"Чи є numbers списком: {isinstance(numbers, list)}")


if __name__ == "__main__":
    main()

print("\nЗавдання 2")
    
def classify_grade(score: int) -> str:
    """Визначає оцінку за шкалою ЄКТС."""

    if 90 <= score <= 100:
        return "A"
    elif 82 <= score <= 89:
        return "B"
    elif 74 <= score <= 81:
        return "C"
    elif 64 <= score <= 73:
        return "D"
    elif 60 <= score <= 63:
        return "E"
    elif 35 <= score <= 59:
        return "FX"
    else:
        return "F"


def main():
    raw = input("Введіть оцінку (0-100): ")

    try:
        score = int(raw)

        if score < 0 or score > 100:
            print("Помилка: оцінка має бути від 0 до 100.")
        else:
            grade = classify_grade(score)

            print(f"Оцінка {score} → ЄКТС: {grade}")

            passed = grade not in ("FX", "F")

            if passed:
                print("Результат: Зараховано")
            else:
                print("Результат: Не зараховано")

    except ValueError:
        print("Помилка: потрібно ввести ціле число.")


if __name__ == "__main__":
    main()

print("\n")

import math

def triangle_type(a: float, b: float, c: float) -> str:
    """Визначає тип трикутника за його сторонами."""

    if a <= 0 or b <= 0 or c <= 0:
        return "не є трикутником"

    if not (a + b > c and a + c > b and b + c > a):
        return "не є трикутником"

    x, y, z = sorted([a, b, c])

    if a == b and b == c:
        return "рівносторонній"
    elif a == b or b == c or a == c:
        return "рівнобедрений"
    else:
        if abs(x**2 + y**2 - z**2) < 1e-9:
            return "прямокутний"
        else:
            return "різносторонній"


def triangle_area(a: float, b: float, c: float) -> float:
    """Обчислює площу трикутника за формулою Герона."""

    p = (a + b + c) / 2

    area = math.sqrt(
        p * (p - a) * (p - b) * (p - c)
    )

    return area


def main():
    try:
        a = float(input("Введіть сторону a: "))
        b = float(input("Введіть сторону b: "))
        c = float(input("Введіть сторону c: "))

        result = triangle_type(a, b, c)

        print("\nРезультати:")

        if result == "не є трикутником":
            print("Введені сторони не утворюють трикутник.")
        else:
            area = triangle_area(a, b, c)

            print(f"Тип трикутника: {result}")
            print(f"Площа трикутника: {area:.2f}")

    except ValueError:
        print("Помилка: введіть коректні числові значення.")


if __name__ == "__main__":
    main()

print("\nЗавдання 3")


def factorial(n: int) -> int:
    """Обчислює факторіал числа n."""

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def harmonic_sum(n: int) -> float:
    """Обчислює суму гармонічного ряду."""

    result = 0

    for i in range(1, n + 1):
        result += 1 / i

    return result


def multiplication_table(n: int) -> None:
    """Виводить таблицю множення n × n."""

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end="")
        print()


def main():
    try:
        n = int(input("Введіть число n: "))

        if n < 0:
            print("Помилка: число повинно бути невід'ємним.")
            return

        print(f"\n{n}! = {factorial(n)}")
        print(f"Гармонічна сума H({n}) = {harmonic_sum(n):.6f}")

        print(f"\nТаблиця множення {n}×{n}:")
        multiplication_table(n)

        print("\nПарні числа від 2 до n:")
        for i in range(2, n + 1, 2):
            print(i, end=" ")

        print("\nЧисла у зворотному порядку:")
        for i in range(n, 0, -1):
            print(i, end=" ")

        print()

    except ValueError:
        print("Помилка: потрібно ввести ціле число.")


if __name__ == "__main__":
    main()

print("\n")


def calculator():
    """Інтерактивний калькулятор."""

    print("=== Калькулятор ===")
    print("Введіть вираз у форматі: число оператор число")
    print("Доступні оператори: +, -, *, /, //, %, **")
    print("Введіть 'quit' для виходу, 'history' для історії.")

    history = []

    while True:
        user_input = input("\n> ").strip()

        if user_input.lower() == "quit":
            print("Завершення роботи калькулятора.")
            break

        if user_input.lower() == "history":
            if history:
                print("\nІсторія обчислень:")
                for item in history:
                    print(item)
            else:
                print("Історія порожня.")
            continue

        parts = user_input.split()

        if len(parts) != 3:
            print("Помилка: введіть вираз у форматі 5 + 3.")
            continue

        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("Помилка: ділення на нуль.")
                    continue
                result = num1 / num2

            elif operator == "//":
                if num2 == 0:
                    print("Помилка: ділення на нуль.")
                    continue
                result = num1 // num2

            elif operator == "%":
                if num2 == 0:
                    print("Помилка: ділення на нуль.")
                    continue
                result = num1 % num2

            elif operator == "**":
                result = num1 ** num2

            else:
                print("Помилка: невідомий оператор.")
                continue

            expression = (
                f"{parts[0]} {operator} {parts[2]} = {result}"
            )

            print("Результат:", result)
            history.append(expression)

        except ValueError:
            print("Помилка: введіть коректні числа.")

        except (OverflowError, ZeroDivisionError):
            print("Помилка: неможливо виконати обчислення.")


if __name__ == "__main__":
    calculator()
