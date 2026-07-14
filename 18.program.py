#write a function to remove a element from list 
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["sadha","sisha","vishan","an"]        
print(rem(l,"an"))