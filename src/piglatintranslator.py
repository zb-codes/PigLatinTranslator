import string as str

def tokenize(string):
    startOfWord = 0
    index = 0
    tokenized_list = []
    for x in range(0, len(string)):
        char = string[index]
        if char == " " or char in str.punctuation:
            if startOfWord != index:
                tokenized_list.append(string[startOfWord:index])# append word BEFORE punctuation
            tokenized_list.append(char)# append punctuation
            startOfWord = index + 1        
        index += 1
    #tokenized_list.append(string[startOfWord:index+1])
    return tokenized_list

def translate(tokens): #could be improved, works for most basic ruleset currently
    translated_tokens = []
    for token in tokens:
        isUpper = False
        if token[0] == " " or token[0] in str.punctuation or len(token) == 1: # Filter out spaces, punctuation, single character words (IE "I" and "a")
            translated_tokens.append(token)
            continue
        else:
            if token[0].isupper(): #set a flag if starts with captital letter
                isUpper = True
            token = token.lower()

            index = 0
            listofVowels = ["a","e","i","o","u"]
            for char in token:
                if char in listofVowels: #triggers after the first consonant or consonant "cluster"
                    token = token[index:len(token)] + token[0:index] + "ay"
                    if isUpper:
                        token = token.capitalize()
                    break
                index += 1
            
            translated_tokens.append(token)

    return translated_tokens

def reassemble(tokens):
    final_string = ""
    for token in tokens:
        final_string += token
    return final_string

def run(string):
    string = tokenize(string)
    string = translate(string)
    string = reassemble(string)
    return string