import random

#Генератор парных чисел

max_number = random.randrange(100)
even_numbers = [x for x in range(max_number) if x % 2 == 0]
print(f"Список парных чисел: {even_numbers}")


# Генератор чисел Фибоначчи

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()

print("\nПервые 10 чисел Фибоначчи:")
for _ in range(10):
    print(next(fib))