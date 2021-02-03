from textblob import TextBlob

# myList = ["Incorret", "spellin"]
wrong_words = input().split()
corrected_list = []

for word in wrong_words:
    corrected_list.append(TextBlob(word))
print("Corrected text:")

for word in corrected_list:
    print(word.correct(), end=" ")