TicTacToe Game

This application runs over Python 3.8.3

```mermaid
graph TD;
    Game --> GameState;
    Game --> Ai;
    Game --> Board
    Game --> Messages
    Ai --> GameState
```

To run:
```
python -m tictactoe
```
