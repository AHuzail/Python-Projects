# Python Snake Game using OOPs


A classic Snake Game implemented in Python, where the player maneuvers a snake to collect food, growing in length with each piece consumed. The game ends if the snake collides with itself or the boundaries.

## Features

- **Responsive Controls**: Use arrow keys to navigate the snake.
- **Score Tracking**: Displays the current score and retains the highest score achieved during the session.
- **Modular Code Structure**: Organized into multiple modules for clarity and maintainability.

## Modules

- `main.py`: Initializes and runs the game loop.
- `snake.py`: Defines the `Snake` class, handling movement and growth mechanics.
- `food.py`: Defines the `Food` class, managing food generation at random positions.
- `scoreboard.py`: Defines the `Scoreboard` class, displaying the current and high scores.

## Requirements

- Python 
- `turtle` module

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AHuzail/Python-Projects.git
   cd Python-Projects
   ```

2. **Execute the Game**:
   ```bash
   python main.py
   ```

   Ensure you have Python installed on your system. If not, download it from the [official website](https://www.python.org/).

## How to Play

- **Start the Game**: Run `main.py` to launch the game window.
- **Control the Snake**: Use the arrow keys to direct the snake:
  - Up Arrow: Move Up
  - Down Arrow: Move Down
  - Left Arrow: Move Left
  - Right Arrow: Move Right
- **Objective**: Guide the snake to consume the food items that appear randomly on the screen. Each time the snake eats, it grows longer, and your score increases.
- **Game Over**: The game ends if the snake collides with itself or the screen boundaries. The highest score achieved during the session is displayed.

