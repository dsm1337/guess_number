from random import randint

begin = 0
end = 100
the_number = randint(begin, end)
guess = 101
while guess != the_number:
    guess = int(input())
    if guess == the_number:
        print('Отличная интуиция! Вы угадали число :)')
    elif guess > the_number:
        print('Ваше число больше того, что загадано')
    else:
        print('Ваше число меньше того, что загадано')
