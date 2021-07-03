import random
game_list = ['rock','paper','scissor']
player = False
while player == False:
    ai = game_list[random.randint(0,2)]
    print('Please pick among rock, paper, scissor')
    player = input()
    if player == ai:
        print('this game is tie. you both picked {0}'.format(player))
    elif player == 'rock':
        if ai == 'paper':
            print(' you are doomed. AI won')
        else:
            print('Yee ! you won against AI. You saved the world from AI')
    elif player == 'paper':
        if ai == 'scissor':
            print(' you are doomed. AI won')
        else:
            print('Yee ! you won against AI. You saved the world from AI')
    elif player == 'scissor':
        if ai == 'rock':
            print(' you are doomed. AI won')
        else:
            print('Yee ! you won against AI. You saved the world from AI')
    else:
        print('you gave the wrong word buddy. go eduacate yourself first !!')
    player == False

