from string import punctuation


text = input("Введите текст: ")

text = text.lower()

for mark in punctuation:
    text = text.replace(mark, " ")

words = text.split()


#print(words)
print("Количество разных слов:", len(set(words)))

word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Частота слов:")

for word, freq in word_frequency.items():
    print(f" {word} : {freq}")