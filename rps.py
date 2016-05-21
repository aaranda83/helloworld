



class rock:

    def winsAgainst(self, otherWeapon):

        if (type(otherWeapon) is rock):
            return 'draw'
        if (type(otherWeapon) is paper):
            return 'lose'
        if (type(otherWeapon) is scissors):
            return 'win'


class paper:

    def winsAgainst(self, otherWeapon):
        if type(otherWeapon) is rock:
            return 'win'
        if (type(otherWeapon)is paper):
            return 'draw'
        if (type(otherWeapon) is scissors):
            return 'lose'

class scissors:

    def winsAgainst(self, otherWeapon):
        if (type(otherWeapon) is rock):
            return 'lose'
        if (type(otherWeapon) is paper):
            return 'win'
        if (type(otherWeapon) is scissors):
            return 'draw'

def returntype(playerchoice):
    settype = ()
    if playerchoice == "rock":
        settype = rock()
    if playerchoice == "paper":
        settype = paper()
    if playerchoice == "scissors":
        settype = scissors()

    return settype


def battle(weapon1, weapon2, player1, player2):


    if type(weapon1) is type(weapon2):
        return 'It\'s a draw'

    if type(weapon1) is rock:
        if type(weapon2) is paper:
            return player2 + ' wins'
        if type(weapon2) is scissors:
            return player1 + ' wins'

    if type(weapon1) is paper:
        if type(weapon2) is scissors:
            return player2 + ' wins'
        if type(weapon2) is rock:
            return player1 + ' wins'

    if type(weapon1) is scissors:
        if type(weapon2) is rock:
            return player2 + ' wins'
        if type(weapon2) is paper:
            return player1 + ' wins'

def setcpu(num):
    return "cpu " + num


playercount = 1


print('Welcome to Rock, Paper Scissors!')
print('')
print('Type a name for each player.  Or type \'cpu\' to have the computer play')

player1 = input("Player" + str(playercount) + ": ")

if player1 == "cpu":
    player1 = setcpu(playercount)

print("Player " + str(playercount) + " is: " + player1)

playercount += 1

player2 = input("Player " + str(playercount) + ": ")

if player2 == "cpu":
    player2 = setcpu(playercount)
print("Player " + str(playercount) + " is: " + player2)



choice1 = returntype(input(player1 + " , Choose your weapon: ").lower())

choice2 = returntype(input(player2 + " , Choose your weapon: ").lower())

print(battle(choice1,choice2, player1, player2))
