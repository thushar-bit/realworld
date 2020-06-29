chess_position = input('enter the position of the chess board')
chess = chess_position[0]
numbers = int(chess_position[1])
if chess == 'a':
    number = 1
elif chess == 'b':
    number = 2
elif chess == 'c':
    number = 3
elif chess == 'd':
    number = 4
elif chess == 'e':
    number = 5
elif chess == 'f':
    number = 6
elif chess == 'g':
    number = 7
elif chess == 'h':
    number = 8
if number % 2 and numbers % 2:
        print('it is black')
elif number == numbers:
    print('it is black')
else:
    print('it is white')


