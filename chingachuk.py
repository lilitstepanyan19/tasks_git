import random
import stdiomask


def game_res(inp_piece, game_piece_k, game_piece):
    if inp_piece == game_piece_k:
        return f'comp - {game_piece_k}, you - {inp_piece}, res - draw'
    elif inp_piece == game_piece[0] and game_piece_k == game_piece[1] \
        or inp_piece == game_piece[1] and game_piece_k == game_piece[2]\
        or inp_piece == game_piece[2] and game_piece_k == game_piece[1]:
        return f'comp - {game_piece_k}, you - {inp_piece}, res - you lost'
    elif inp_piece == game_piece[0] and game_piece_k == game_piece[2]\
        or inp_piece == game_piece[1] and game_piece_k == game_piece[0]\
        or inp_piece == game_piece[2] and game_piece_k == game_piece[0]:
        return f'comp - {game_piece_k}, you - {inp_piece}, res - you won'
    
def get_game_with_comp(game_piece):
    inp_piece = input('Enter a piece: ')
    if inp_piece not in game_piece:
        return 'This piece not found'
    game_piece_k = random.choice(game_piece)
    return game_res(inp_piece, game_piece_k, game_piece)

def get_game_with_friend(game_piece):
    friends_piece = stdiomask.getpass(prompt="Friend's piece ", mask='*')
    your_piece = stdiomask.getpass(prompt="Your piece ", mask='*')
    if friends_piece not in game_piece or your_piece not in game_piece:
        return 'This piece not found'
    return game_res(friends_piece, your_piece, game_piece)
    
def get_flayer(game_piece):
    inp = input('Do you want to play with a computer or with a friend? Enter c or f: ')
    if inp == 'c':
        print(get_game_with_comp(game_piece))
    elif inp == 'f':
        return get_game_with_friend(game_piece)
    else:
        return 'Player not found'
    
def main():
    game_piece = ['p', 's', 'r']
    print(get_flayer(game_piece))
    
print(main())
