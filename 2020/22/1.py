# Slow
import math

with open('input_s') as f:
    lines = "".join(f.readlines()).split("\n\n")

player1_deck = lines[0].split(":\n")[1].split("\n")
player2_deck = lines[1].split(":\n")[1].split("\n")

print(player1_deck, player2_deck)
for i in range(0, len(player1_deck)):
    player1_deck[i] = int(player1_deck[i])
for i in range(0, len(player1_deck)):
    player2_deck[i] = int(player2_deck[i])

print(player1_deck, player2_deck)
# input()
i = 1
while(not (player1_deck == [] or player2_deck == [])):
    print(i)
    if(int(player1_deck[0]) > int(player2_deck[0])):
        add_me1 = player1_deck.pop(0)
        add_me2 = player2_deck.pop(0)
        player1_deck.append(add_me1)
        player1_deck.append(add_me2)
    else:
        add_me2 = player2_deck.pop(0)
        add_me1 = player1_deck.pop(0)
        player2_deck.append(add_me2)
        player2_deck.append(add_me1)
    i += 1

score = 0
for i in range(0, len(player1_deck)):
    score += int(player1_deck[i])*(len(player1_deck)-i)
    print(player1_deck[i], len(player1_deck)-i)
print(score)

score = 0
for i in range(0, len(player2_deck)):
    score += int(player2_deck[i])*(len(player2_deck)-i)
    print(player2_deck[i], len(player2_deck)-i)
print(score)

print(player1_deck, player2_deck)

# Calculate scores