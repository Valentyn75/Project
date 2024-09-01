def find_primes(a, b):
  """Знаходить усі прості числа між числами a та b (включно).

  Args:
    a: Перше число.
    b: Друге число.

  Returns:
    Список простих чисел між a та b.
  """

  primes = []
  for num in range(min(a, b), max(a, b)+1):
    if num > 1:
      for i in range(2, int(num**0.5)+1):
        if (num % i) == 0:
          break
      else:
        primes.append(num)
  return primes

# Отримання чисел від користувача
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

# Знаходження простих чисел і виведення результату
result = find_primes(a, b)
print("Прості числа між", a, "і", b, ":", result)