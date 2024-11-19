# Exercise 1

# Alef
cities: list[str] = ["Shanghai", "Dubai", "Sydney", "London", "Paris", "New York", "Tokyo"]
print('a', sorted(cities, key=lambda c: len(c)))
print('b', sorted(cities, key=lambda c: len(c.split())))
print('c', sorted(cities, key=lambda c: c[-1]))
print('d', sorted(cities, key=lambda c: c[::-1]))

distance = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050, "Europe"],
            ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"],
            ["Shanghai", 4920, "Asia"]]
print('a', sorted(distance, key=lambda d: d[1]))
print('b', sorted(distance, key=lambda d: d[1], reverse=True))
print('c', sorted(distance, key=lambda d: d[2]))
print('d', sorted(distance, key=lambda d: (d[2], d[1])))

# Bet
import random, statistics

random_list: list[int] = [random.randint(1, 100) for _ in range(50)]
print('1', sorted(random_list, key=lambda r: r))
avg_nums = statistics.mean(random_list)
print(f"Average number is {avg_nums}")
print('2', sorted(random_list, key=lambda r: r - avg_nums))

# Exercise 2
text: str = """
This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting.
"""
words: list[str] = (text.lower().replace(".", "").replace(",", "").split())
print(words)
dict_count_words: dict[str: int] = dict()
for word in words:
    dict_count_words[word] = dict_count_words.get(word, 0) + 1
print('a', dict_count_words)
max_key = max(dict_count_words, key=lambda key_dict: dict_count_words[key_dict])
max_value = dict_count_words[max_key]
print(f"The most popular word is {max_key}, it appears {max_value} times")

dict_count_letters: dict[str: int] = dict()
for letter in text.lower():
    dict_count_letters[letter] = dict_count_letters.get(letter, 0) + 1
print('b', dict_count_letters)
min_key = min(dict_count_letters, key=lambda key_dict: dict_count_letters[key_dict])
min_value = dict_count_letters[min_key]
print(f"The less popular letter is {min_key}, it appears {min_value} times")

# Exercise 3
dict_power3: dict[int, int] = dict()
for i in range(1, 20 + 1):
    dict_power3[i] = i ** 3
print(dict_power3)

number: int = int(input("Enter a number: "))
num = number ** 3 if number in dict_power3 else "Not exist"
print(num)
