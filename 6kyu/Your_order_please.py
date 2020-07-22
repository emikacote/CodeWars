def order(sentence):
    sent_list = sentence.split(" ")
    sorted_sent = []

    for i in range(1,10):
        for word in sent_list:
           if str(i) in word:
               sorted_sent.append(word)

    sorted_sent = " ".join(sorted_sent)
    return sorted_sent
