userInput = int(input('Within how many numbers you want to calculate it\'s average? \n'))
listt = []

for i in range(0,userInput):
    '''
    this will iterate over items and add in empty list
    '''
    i = int(input('Enter your number:\t'))
    listt.append(i)
y = sum(listt)

print(y/userInput)
# print(listt)