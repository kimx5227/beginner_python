def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
spam = eggs(spam)
print(spam)
