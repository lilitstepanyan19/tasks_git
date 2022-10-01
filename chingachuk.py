import random
import getpass
import stdiomask


x = stdiomask.getpass(prompt='PW: ', mask='*')
print(x)
# def get_game(game_piece):
#     game_piece_k = random.choice(game_piece)
#     inp_piece = input('Enter a piece: ')
#     if inp_piece == game_piece_k:
#         return game_piece_k, inp_piece, 'draw't       
#     elif inp_piece == game_piece[0] and game_piece_k == game_piece[1] \
#         or inp_piece == game_piece[1] and game_piece_k == game_piece[2]\
#         or inp_piece == game_piece[2] and game_piece_k == game_piece[1]:
#         return game_piece_k, inp_piece, 'you lost'
#     elif inp_piece == game_piece[0] and game_piece_k == game_piece[2]\
#         or inp_piece == game_piece[1] and game_piece_k == game_piece[0]\
#         or inp_piece == game_piece[2] and game_piece_k == game_piece[0]:
#         return game_piece_k, inp_piece, 'you won'


# def get_flayer(inp):
#     if inp == 'k':
#         print(get_game(game_piece))
#     else:
#         pass

# def main():
#     inp = input('Do you want to play with a computer or with a friend? Enter k or f: ')
#     game_piece = ['p', 's', 'r']
#     print(get_flayer(inp))
    
# print(main())
