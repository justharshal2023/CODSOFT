import streamlit as st
import numpy as np

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="🎮")

st.title("🎮 Tic-Tac-Toe: Play vs Unbeatable AI (Minimax)")
st.markdown("You are ❌. AI is ⭕. Good luck!")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"  # Human always starts

# Winning combinations
WIN_COMBOS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def check_winner(board):
    for i, j, k in WIN_COMBOS:
        if board[i] == board[j] == board[k] and board[i] != "":
            return board[i]
    if "" not in board:
        return "Draw"
    return None


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -np.inf
    move = -1
    for i in range(9):
        if st.session_state.board[i] == "":
            st.session_state.board[i] = "O"
            score = minimax(st.session_state.board, False)
            st.session_state.board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    st.session_state.board[move] = "O"
    st.session_state.turn = "X"


def handle_click(index):
    if st.session_state.board[index] == "" and st.session_state.turn == "X":
        st.session_state.board[index] = "X"
        st.session_state.turn = "O"
        winner = check_winner(st.session_state.board)
        if not winner:
            ai_move()


# Display the board
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i, use_container_width=True):
            handle_click(i)

# Show result
winner = check_winner(st.session_state.board)
if winner:
    st.success(f"Game Over: {winner} wins!" if winner != "Draw" else "It's a draw!")
    if st.button("Play Again"):
        st.session_state.board = [""] * 9
        st.session_state.turn = "X"
