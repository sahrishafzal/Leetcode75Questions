def solution(message, K):
    if K<3:
        return "..."
    if len(message)<=K:
        return message
    words=message.split()
    truncMessage=[]
    currLen=0# hold the length of character for current len
    #len(turncMessage)-1= total number of spaces
    #lentruncMessage for number of space
    for word in words:
        wordLen=len(word)
        if wordLen+currLen+len(truncMessage)>K-3: 
            break
             
            # don't need to use K-4 and len(truncMessag)-1 
            #as I'm using len(truncMessage)that will add the space after each word and will take care of K-1. that's why I used K-3
        truncMessage.append(word)
        currLen+=wordLen
    if currLen+len(truncMessage)>K-3: # checking if the message acceed the limit 
            truncMessage.pop() # if one word is extra then remove it
    return " ".join(truncMessage)+" ..." if truncMessage else "..."
print(solution("And now here is my secret", 15)) 
print("") # Expected: "And now ..."
print(solution("There is an animal with four legs", 15), end="\n")  # Expected: "There is an ..."
print(solution("super dog", 4),end="\n")  # Expected: "..."
print(solution("how are you", 20),end="\n")  # Expected: "how are you"
