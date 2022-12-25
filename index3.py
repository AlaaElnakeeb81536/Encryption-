#try to find num of word and num of charachter in sentence
def count (sentence):
    res=0
    c=0
    for word in sentence.split():
        res+=1
        for i in word:
            c+=1
    print(res) #res refer to num of word in sentence
    print(c) #c refers to num of char in sentence 
count("Alaa Elnakeeb")
            
        
        
