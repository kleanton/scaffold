# Игра по угадыванию чисел
import random

guessesTaken = 0
myName= input('Привет! Как тебя зовут?\n')
number = random.randint(1,20)
print(myName+' ,загадываю число от 1 до 20.')

for guessesTaken in range(6):
    guess=int(input('Попробуй угадать.\n'))

    if guess < number:
        print('Не угадал. Моё число больше твоего')
    elif guess > number:
        print('Не угадал. Моё число меньше твоего')
    elif guess==number:
        break

if guess==number:
    guessesTaken=str(guessesTaken+1)
    print('Отлично, ' + myName + '! Ты справился за ' + guessesTaken +' попытки!')
elif guess != number:
    number=str(number)
    print('Увы. Я загадал число '+number + '.')
