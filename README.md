# Coup RL Desktop App

The Coup RL desktop app allows humans to play against an RL agent.
You can choose to train the agent through your games, or play with an agent trained through some other method.

## Usage
```bash
$ python app/main.py
```
First, make your selections on the main menu.
- When creating a new agent:
    - File location to save to
    - Learning Rate
    - Discount Factor
    - Epsilon
- When using an existing agent:
    - Existing agent file location
- Whether to train the agent (whether the value function will be saved with updated values after this game or not)
- Which player has the first turn  
![Coup RL Desktop App Menu](./img/menu1.png)
![Coup RL Desktop App Menu](./img/menu2.png)

After pressing start, the game will begin. You'll see your opponent on the top and your information on the bottom. For both players you can see the cards, the last move they took, and the number of coins they have. The opponent's cards stay hidden until they have been eliminated. 

Between the two players is a list of actions you can take. Invalid actions are grayed out depending on the state of the game. For example, below I don't have 7 coins, so the Coup action is grayed out.

Play the game by selecting a valid action.
![Coup RL Desktop App Board](./img/board.png)

Some actions require the selection of 1 or more of your cards and pressing the confirm button.
![Coup RL Desktop App Board Card Select](./img/board_card_select.png)