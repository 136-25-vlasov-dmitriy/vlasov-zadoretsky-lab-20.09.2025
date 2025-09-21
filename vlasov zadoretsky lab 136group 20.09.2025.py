a = int('17')
b = float('3.14')

print(a+b, a-b, a*b, a/b)
print(type(a/b))

r = 5
pi = 3.14159

result = round(pi*r**2, 2)
s = f'{result}'
print(s)

text1 = " Hello, Python! "
text2 = text1.replace('!','?')
print(text2.strip())

print(text2.upper().strip())
print(text1.lower().strip())

numbers = [7, 2, 5]
numbers.append(4)
numbers.insert(1, 10)
numbers.extend([1, 1, 1])
numbers.remove(7)
pop = numbers[-1]
numbers.remove(numbers[-1])
numbers.sort()
numbers.reverse()
print(numbers.count(2))
print(numbers.index(1))
print(numbers)

copy = numbers.copy()
print(copy)
deepcopy = numbers.copy()
print(deepcopy)
numbers.clear()
print(numbers)

t = (1, 2, 3)
#t[1] = 100
t1 = (4, 5)

t2 = t + t1
print(t2.count(3))
print(t2.index(4))
print(t)

values = [3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
print(unique_values, len(unique_values))

other = {2, 4, 5}

print(unique_values & other)
print(unique_values | other)
print(unique_values - other)
print(other - unique_values)

scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95

print(scores.get("Alice"))
print(scores.get("Dave"))
scores.pop("Alice")
print("Alice" not in scores)
print(scores, len(scores))
print(scores.keys(), scores.values())

text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""

print(text.lower().strip())
text.replace("!", ".")

text.split(".")

txt1 = "python is a powerful programming language"
print(txt1.split(" "), txt1.count("python"))

print(txt1.startswith("python") , txt1.endswith("python"))
print(len(txt1), txt1.count("a"), txt1.find("data"))

print(txt1.split(" "))
print("-".join(txt1.split(" ")))

txt2 = "python is a powerful programming language"
word_counts = {}
for i in txt2.split():
    word_counts[i] = word_counts.get(i, 0) + 1

print(word_counts)

import re
def clean_text(intext):
    newtext= re.sub(r'[^A-Za-z]','',intext).lower()
    return newtext

print(clean_text(text))