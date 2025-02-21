def reverse_sentence(sentence):
    words = sentence.split(" ")
    words = words[::-1]
    print(' '.join(words))
    
sentence1 = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence1)

sentence2 = "Pooh"
reverse_sentence(sentence2)