# Minimax Algorithm - Coin Game (pick from LEFT or RIGHT end)
# Coins with different values are placed in a row. Players take turns picking
# one coin from the left end or the right end. Highest total wins.
# Computer = MAX (tries to maximize its total), Human = MIN.

coins = [4, 10, 6, 3, 8, 2]

# Returns the best TOTAL the computer can get from coins[left..right]
def minimax(left, right, is_max):
    if left > right:                       # no coins left
        return 0
    if is_max:                             # computer's turn: pick best option
        take_left = coins[left] + minimax(left + 1, right, False)
        take_right = coins[right] + minimax(left, right - 1, False)
        return max(take_left, take_right)
    else:                                  # human's turn: computer gets nothing
        take_left = minimax(left + 1, right, True)
        take_right = minimax(left, right - 1, True)
        return min(take_left, take_right)  # human tries to minimize computer's total

def computer_move(left, right):
    take_left = coins[left] + minimax(left + 1, right, False)
    take_right = coins[right] + minimax(left, right - 1, False)
    return "L" if take_left >= take_right else "R"


left, right = 0, len(coins) - 1
human_score = computer_score = 0
turn = "human"

while left <= right:
    print("\nCoins:", coins[left:right + 1])
    if turn == "human":
        choice = ""
        while choice not in ("L", "R"):
            choice = input("Your move - pick Left or Right (L/R): ").upper().strip()
        turn = "computer"
        if choice == "L":
            human_score += coins[left]
            left += 1
        else:
            human_score += coins[right]
            right -= 1
    else:
        choice = computer_move(left, right)
        if choice == "L":
            print("Computer picks LEFT coin:", coins[left])
            computer_score += coins[left]
            left += 1
        else:
            print("Computer picks RIGHT coin:", coins[right])
            computer_score += coins[right]
            right -= 1
        turn = "human"

print("\nYour score    :", human_score)
print("Computer score:", computer_score)
if computer_score > human_score:
    print("Computer WINS!")
elif human_score > computer_score:
    print("You WIN!")
else:
    print("It's a DRAW!")