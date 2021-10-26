# Ex:1

my_string = input("Tell me some word\n\t")

if len(my_string) > 2:
	if my_string[-3:] == "ing":
		print(my_string + "ly")
	else:
		print(my_string + "ing")
else:
	print(my_string)

# Ex:2

my_sentence = input("Writh a sentence\n\t")
word_not = my_sentence.find("not")
word_poor = my_sentence.find("poor")

if word_poor > word_not and word_not>0 and word_poor>0:
    new_sentence = sentence.replace(my_sentence[word_not:(word_poor+4)], 'good')
    print(new_sentence)
else:
     print(my_sentence)

# Ex:3
word = input("Tell me some word\n")
first_letter = word[0] 
word = word.replace(first_letter, "$")
print(first_letter + word[1:])


# Ex:4

sentence = input("Write a sentence.\n")
letters = 0
numbers = 0
other = 0
for i in sentence:
    if i.isalpha():
	    letters = letters + 1
    elif i.isdigit():
        numbers = numbers + 1
    else:
        other = other + 1
print("The length of the string: ", letters + numbers + other)


# Ex:5

sentence_1 = input("Write a sentence.\n")
for i in range(len(sentence_1)):
	if i % 2 == 0 and i != 0:
		print(sentence_1[i], end='')

