from tictactoe.presentation.messages import alert

def join_and_enclose(list, separator):
  return separator + separator.join(list) + separator

def present_board(state):
  border_top = join_and_enclose(['---'] * state.size, '-')
  print('\n' + border_top)
  for i in range(state.size):
    row = join_and_enclose(state.squares[i * state.size : (i + 1) * state.size], ' | ')
    print(row.strip())
    print(border_top)
  print('\n')
    
def show(state):
    if (not state.started):
        alert('\nWelcome to the TicTacToe Game!!!\n')
    present_board(state)
