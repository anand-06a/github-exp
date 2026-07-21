a=7,'p',9
print(type(a))

# try to find out vowel from sentence
sentence = 'Hello, how are you?'
vowels = "aeiouAEIOU"

for letter in sentence:
    if letter in vowels:
        print(letter)


sentence = "Hello, how are you?"
vowels = [letter for letter in sentence if letter.lower() in "aeiouAEIOU"]
print(vowels)        