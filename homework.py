a, b, c = map(int, input().split())

disc = b**2 - 4 * a * c

if disc > 0:
    x1 = (-b + disc**0.5) / 2 * a
    x2 = (-b - disc**0.5) / 2 * a
    print(x1, x2)

elif disc == 0:
    x1 = (-b + disc**0.5) / 2 * a
    print(x1)

else:
    print("Нет решения!")
