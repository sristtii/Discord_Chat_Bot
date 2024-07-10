# Discord Chat Bot

A simple Discord bot written in Python that responds to user messages with predefined responses and can perform basic actions like rolling dice.

## Features

- Responds to greetings and common phrases
- Rolls a dice when prompted
- Handles private and public messages
- Customizable responses

## Requirements

- Python 3.7+
- discord.py
- python-dotenv

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Discord_Chat_Bot.git
    cd Discord_Chat_Bot
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your Discord bot token:

    ```env
    DISCORD_TOKEN=your-discord-bot-token
    ```

## Usage

1. Run the bot:

    ```bash
    python main.py
    ```

2. Interact with the bot in your Discord server. The bot responds to the following commands and messages:
    - `hello`
    - `how are you`
    - `bye`
    - `roll dice`

## Code Overview

- `main.py`: Main file to run the bot.
- `responses.py`: Contains the logic for generating responses to user messages.
