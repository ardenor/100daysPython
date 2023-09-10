sentence = "What is the airspeed velocity of an Unladen Swalllow"

sentence_list = sentence.split()

print(sentence_list)

result = {word:len(word) for word in sentence_list}
print(result)