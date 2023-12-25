# Code that reads in a string and coverts each alternate character into uppercase and each other alternate character into lowercase.

my_str = "Learning to code is fun"

alternating = ""

for i in range(len(my_str)):
    if i % 2 == 0:
        alternating = alternating + my_str[i].upper() # Each even index number character is uppercase.
    else:
        alternating = alternating + my_str[i].lower() # Each other index number character is lowercase.
print(alternating)

# Code that makes each alternative word in a string lower and upper case.

sentence = "Learning to code is fun"
new_sentence = sentence.split()
print(new_sentence)

alt_sentence = ""

for i in range(len(new_sentence)):
    if i % 2 == 0:
        alt_sentence = alt_sentence + " " + new_sentence[i].lower()
    else:
        alt_sentence = alt_sentence + " " + new_sentence[i].upper()
print(alt_sentence)

# Code that makes each alternative word in a string lower and upper case - using the join function.

sentence = "Learning to code is fun"
new_sentence = sentence.split()
print(new_sentence)

alt_sentence = []

for i, word in enumerate(new_sentence):
    if i % 2 == 0:
        alt_sentence.append(word.lower())
    else:
        alt_sentence.append(word.upper())
print(" ".join(alt_sentence))
