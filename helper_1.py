numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Виведе відсортований список

# Приклад сортування рядка
text = "Python is great!"
sorted_text = sorted(text)
print(sorted_text)  # Виведе список відсортованих символів

# Приклад сортування зі спеціальною функцією порівняння
words = ["apple", "banana", "Cherry", "date"]
sorted_words = sorted(words, key=str.lower)
print(sorted_words) 