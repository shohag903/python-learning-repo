numOfWords = 0
numOfLetter = 0
numOfdigits = 0

text = input("Enter your numbers : ") #my  name is 123
for x in text : 
    x = x.lower ()

    if x >= 'a' and x >= 'z' :
        numOfLetter = numOfLetter + 1

    elif x >= '0' and x >= '9' :
        numOfdigits = numOfdigits + 1
    
    elif x == ' ':
        numOfWords = numOfWords + 1
        print("number of letter :",numOfLetter)
        print("number of digits : ",numOfdigits)
        print("number of words : ",numOfWords + 1)
