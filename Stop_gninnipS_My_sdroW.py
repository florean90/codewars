def spin_words(sentence):
    return " ".join(word if len(word) < 5 else word[::-1] for word in sentence.split())




a = "This is another test"
print(spin_words(a))