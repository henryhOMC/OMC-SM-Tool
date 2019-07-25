from itertools import zip_longest

def percentSame(str1, str2):
    iterator = 0
    similarityCount = 0
    for i in zip_longest(str1, str2):
        if str1[iterator] == str2[iterator]:
            similarityCount += 1
        iterator += 1

    percent = (similarityCount/iterator)*100

    return(percent) #   % difference



print(percentSame("hello", "hello"))

print(percentSame("hello", "Hello"))

print(percentSame("hello", "hellllo"))