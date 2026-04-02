# Fake-Wordle
 A clean, functional recreation of the popular word-guessing game **Wordle** built in Python. This script uses a local word list and terminal color codes to provide an authentic gameplay experience directly in your console.

## 🎮 Features
*   **Color-Coded Feedback**: Uses ANSI escape codes to highlight letters:
    *   🟩 **Green**: Correct letter in the correct position.
    *   🟨 **Yellow**: Correct letter but in the wrong position.
*   **Dynamic Word Loading**: Pulls random 5-letter words from a local `word_list.txt` file.
*   **Tracking System**: 
    *   Displays your current progress with `[_]` placeholders.
    *   Maintains a list of **Incorrect Guesses** to help you eliminate letters.
*   **Automatic Screen Clearing**: Uses `os.system('clear')` to keep the interface tidy after every guess.
*   **Replay System**: Prompts the user to play again without needing to restart the script.

## 🛠️ Requirements
*   **Python 
*   A terminal that supports ANSI colors (VS Code Terminal, macOS Terminal, Linux Bash, etc.)
*   A file named `word_list.txt` in the same directory.

## 📥 Setup & Installation
1.  **Clone the repository** or save the script as `wordle.py`.
2.  **Copy the word list**:
3.  **Run the game**:

## 🕹️ How to Play
1.  You have **6 tries** to guess the hidden 5-letter word.
2.  Type a 5-letter word and press **Enter**.
3.  The game will update the "Word" display:
    *   Green letters are locked in.
    *   Yellow letters mean "try this somewhere else."
4.  Check the **Incorrect Guesses** list to see which letters you've already ruled out.
5.  If you win or lose, press `y` to start a fresh round with a new word!
