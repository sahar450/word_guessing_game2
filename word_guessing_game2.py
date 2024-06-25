import random
name = input("what`s your name?")

print("you can guess 14 ,  good luck!")
words=['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

target = random.choice(words)
guess = input("please enter the select char:")
print(target)
count = len(target)
print("the number of letters in a word:" ,count)
correct=[]
for item in range(0,14,1):
    
    if guess in target:
        print("yes" , guess)
        correct+=guess
        guess = input("please enter the select char:")
        print("correct :",correct)
         
        
    else:
        print("falt")
        guess = input("please enter the select char:")
        print("correct :",correct)


            
        