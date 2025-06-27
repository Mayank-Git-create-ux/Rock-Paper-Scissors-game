import random
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# --- Game Logic ---
# Function to determine the winner of a round
def determine_winner(player_choice, computer_choice):
    """
    Determines the winner of a Rock, Paper, Scissors round.

    Args:
        player_choice (str): The player's choice ('rock', 'paper', 'scissors').
        computer_choice (str): The computer's choice ('rock', 'paper', 'scissors').

    Returns:
        str: The outcome of the round ('win', 'lose', 'draw').
    """
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'win'
    else:
        return 'lose'

# --- Flask Routes ---

@app.route('/')
def index():
    """
    Renders the main game page.
    """
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    """
    Handles the game logic when a player makes a move.
    Receives player's choice, generates computer's choice, determines winner,
    and returns the result as JSON.
    """
    # Get the player's choice from the POST request
    player_choice = request.json.get('choice')

    # Validate player's choice
    choices = ['rock', 'paper', 'scissors']
    if player_choice not in choices:
        return jsonify({'error': 'Invalid choice'}), 400

    # Computer makes a random choice
    computer_choice = random.choice(choices)

    # Determine the winner
    outcome = determine_winner(player_choice, computer_choice)

    # Prepare the response
    response_data = {
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'outcome': outcome
    }
    return jsonify(response_data)

# --- Run the Application ---
if __name__ == '__main__':
    # Run the Flask app in debug mode (for development)
    # In a production environment, you would use a production-ready WSGI server like Gunicorn.
    app.run(debug=True)
