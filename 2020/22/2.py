with open('input_m') as f:
    lines = "".join(f.readlines()).split("\n\n")

player1_deck = [int(i) for i in lines[0].split(":\n")[1].split("\n")]
player2_deck = [int(i) for i in lines[1].split(":\n")[1].split("\n")]

def compute_score(deck):
    score = 0
    for i in range(0, len(deck)):
        score += int(deck[i])*(len(deck)-i)
        print('+', deck[i], '*', len(deck)-i)
    return score

def recursive_combat(deck1, deck2, game_count):
    global global_game_count
    states = []
    round_count = 1
    player1_wins = False

    print('=== Game', game_count, '===')
    while(not(deck1 == [] or deck2 == [])):
        print('-- Round', round_count, '(Game', str(game_count) + ') --')
        print('Player 1\'s deck', deck1)
        print('Player 2\'s deck', deck2)

        if ([deck1, deck2] in states):
            print("Player 1 wins!")
            player1_wins = True
            break
        states.append([deck1[:], deck2[:]])

        player1_top = deck1.pop(0)
        player2_top = deck2.pop(0)

        print('Player 1 plays', player1_top)
        print('Player 2 plays', player2_top)

        if(len(deck1) >= player1_top and len(deck2) >= player2_top):
            copy1 = deck1[:player1_top]
            copy2 = deck2[:player2_top]
            global_game_count += 1

            print('Playing a sub-game to determine the winner...')
            if(recursive_combat(copy1, copy2, global_game_count)):
                deck1.append(player1_top)
                deck1.append(player2_top)
            else:
                deck2.append(player2_top)
                deck2.append(player1_top)
            print('...anyway, back to game 1.')

        else:
            winner = 1
            if(int(player1_top) > int(player2_top)):
                deck1.append(player1_top)
                deck1.append(player2_top)
            else:
                deck2.append(player2_top)
                deck2.append(player1_top)
                winner = 2
            print('Player', winner, 'wins round', round_count, 'of game', game_count, '!\n')

        round_count += 1
    
    if(player1_wins or deck2 == []):
        print('The winner of game', game_count, 'is player 1!')
        if(game_count == 1):
            print(deck1, deck2)
            print('Score:', compute_score(deck1))
        return True
    else:
        print('The winner of game', game_count, 'is player 1!')

        if(game_count == 1):
            print(deck1, deck2)
            print('Score:', compute_score(deck2))
        return False


global_game_count = 1
recursive_combat(player1_deck, player2_deck, global_game_count)

print('p1', player1_deck)
print('p2', player2_deck)

print('=', end='')
print(compute_score(player1_deck))
print(compute_score(player2_deck))


