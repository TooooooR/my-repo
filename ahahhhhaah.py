book = "Вміння спілкуватись"
print(book)


is_adult = False
is_child = True

print(is_adult or is_child)


is_sunny = False
is_cloudy = False

print(not is_sunny)
print(not is_cloudy)

# ----------------------

x = 166.124
z = 15.839

result = x**-1 + 2*((x**2 + z)**-1) + 3*((x**3 + z**2)**-1) + 4*((x**4 + z**3)**-1) + 5*((x**5 + z**4)**-1)
result1 = 1/x + 2/(x**2 + z) + 3/(x**3 + z**2) + 4/(x**4 + z**3) + 5/(x**5 + z**4)


print(result)
print(result1)