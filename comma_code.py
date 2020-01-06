def comma_code(list):
    for count,item in enumerate(list): #creates index for each item
        if count != len(list)-1: #checks if last item to put "and"
            print(str(item) +', ', end ='')
        else:
            print('and',item)

spam = ['apples','bananas','tofu','cats', 7]
comma_code(spam)
