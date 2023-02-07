def reverseSentence(s):
    s = s.split(" ")
    l = list(s)
    l.reverse()
    for i in l:
        print(i, end = ' ')

# reverseSentence("We are ready")
# result: ready are We