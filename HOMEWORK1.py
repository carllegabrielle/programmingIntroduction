def calculateStringLength():
    word = input('type a word:')
    result = len(word)
    print('character\'s quantity:',result)
    print('last character:',word[-1])
    print('last character in 70° position:\n'+'x'*(70-result)+word)
    

calculateStringLength()
