def mysum(l, s=0):
    total_l = 0
    for n in l: 
        total_l+=n
    return s + total_l

print(mysum([1,2,3], 4))

def myavg(l):
    total = 0 
    for n in l:
        total+=n
    return (total/len(l))

print(myavg([1,2,3,4,5,6,7,8,9,10]))

def words(l):
    word_lengths = [len(w) for w in l]
    return min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths)
    
print(words(['myo', 'homeanddecoration', 'no', 'home', 'likeand']))