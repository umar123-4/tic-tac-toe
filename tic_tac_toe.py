import streamlit as st
import numpy as np

# Initialize the game state
def initialize_game():
    return np.zeros((3, 3), dtype=int), 1  # 0: empty, 1: Player 1, -1: Player 2

def check_winner(board):
    for player in [1, -1]:
        # Check rows, columns, and diagonals
        if any(np.all(board[i, :] == player) for i in range(3)) or \
           any(np.all(board[:, i] == player) for i in range(3)) or \
           np.all(np.diag(board) == player) or \
           np.all(np.diag(np.fliplr(board)) == player):
            return player
    return 0

def main():
    st.title("Tic Tac Toe")

    if 'board' not in st.session_state:
        st.session_state.board, st.session_state.current_player = initialize_game()

    def reset_game():
        st.session_state.board, st.session_state.current_player = initialize_game()

    st.button("Restart Game", on_click=reset_game)

    board = st.session_state.board
    current_player = st.session_state.current_player

    # Display the game board
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            if board[i, j] == 0:
                if cols[j].button("", key=f"{i}-{j}", use_container_width=True):
                    board[i, j] = current_player
                    st.session_state.current_player *= -1
            elif board[i, j] == 1:
                cols[j].button("X", key=f"{i}-{j}", use_container_width=True)
            else:
                cols[j].button("O", key=f"{i}-{j}", use_container_width=True)

    winner = check_winner(board)
    if winner == 1:
        st.write("Player 1 (X) wins!")
    elif winner == -1:
        st.write("Player 2 (O) wins!")
    elif not np.any(board == 0):
        st.write("It's a tie!")

if __name__ == "__main__":
    main()
