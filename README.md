# 🐍 Snake PRO

Snake PRO is a 2D Snake game developed in **Python** using **Pygame**.

The project expands the traditional Snake gameplay with multiple levels, a target score system, obstacles, persistent score storage using SQLite, sound effects, custom menus, and victory and game-over screens.

## 🎮 About the Game

The objective is to control the snake, eat apples, increase your score, and avoid collisions.

Before starting a level, the player defines a **target score**.

If the player reaches the target before losing, the game considers the objective completed. After reaching the goal, the player can continue playing and increasing the score.

The game currently includes two different levels.

### Level 1

A traditional Snake experience focused on collecting apples and avoiding:

- Screen boundaries
- The snake's own body
- The score panel

### Level 2

A more difficult version that includes:

- Increased snake speed
- Additional obstacles
- Different visual theme
- Different background music

## ✨ Features

- Two playable levels
- Custom target score system
- Growing snake mechanics
- Random apple spawning
- Collision detection
- Self-collision detection
- Obstacles in Level 2
- Game Over screen
- Victory screen
- Restart option
- Persistent score storage
- Total score tracking
- Last round score
- Background music
- Custom game menus

## 🕹️ Controls

| Action | Key |
|---|---|
| Move Up | ↑ |
| Move Down | ↓ |
| Move Left | ← |
| Move Right | → |
| Confirm option | Enter |
| Return / Exit screen | Esc |

The snake cannot immediately reverse into the opposite direction.

## 🏆 Goal System

Before entering a level, the player chooses a target score.

Each apple collected adds:

```text
10 points
```

When the target score is reached, the objective is considered completed.

The player may continue playing after reaching the goal until a collision occurs.

At the end of the round:

- If the score is equal to or greater than the target, the **WIN** screen is displayed.
- If the score is lower than the target, the **GAME OVER** screen is displayed.

## 💾 Score System

Snake PRO uses **SQLite** to store game information locally.

The database stores:

- Total accumulated score
- Score from the current/latest round
- Target score selected by the player

The SCORE menu displays both the total accumulated score and the last round score.

## 🛠️ Technologies

The project was developed using:

- Python
- Pygame
- SQLite
- Object-Oriented Programming
- Git
- GitHub

## 📂 Project Structure

```text
snake-PRO/
│
├── assets/
│   ├── images
│   ├── backgrounds
│   └── audio files
│
├── game_code/
│   ├── Const.py
│   ├── DBProxy.py
│   ├── Game.py
│   ├── Game_Over.py
│   ├── Level.py
│   ├── Menu.py
│   ├── Objective_game.py
│   ├── Score.py
│   ├── Set_goal.py
│   ├── Win.py
│   └── __init__.py
│
├── main.py
├── LICENSE
└── README.md
```

## 🚀 How to Run

### Requirements

Make sure you have **Python** installed.

You can check your installation with:

```bash
python --version
```

You also need Pygame.

Install it with:

```bash
pip install -r requirements.txt
```

### 1. Clone the repository

```bash
git clone https://github.com/Lazaro277/snake-PRO.git
```

### 2. Open the project directory

```bash
cd snake-PRO
```

### 3. Run the game

```bash
python main.py
```

The game window should open after running the command.

## 🧠 Concepts Practiced

During the development of Snake PRO, I practiced concepts such as:

- Object-Oriented Programming
- Classes and methods
- Modular project organization
- Game loops
- Event handling
- Collision detection
- Timed events
- Grid-based movement
- Dynamic object positioning
- Database integration
- SQLite queries
- Persistent game data
- Menu navigation
- State transitions between screens
- Git version control

## 📚 What I Learned

This project helped me understand how a game can be divided into different modules instead of keeping all logic inside a single file.

I worked with separate classes for the menu, gameplay, score system, database access, game-over screen, victory screen, objective explanation, and target configuration.

I also practiced integrating a local SQLite database with a Pygame application and managing transitions between multiple game states.

## 📜 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.

## 👨‍💻 Author

Developed by **Lázaro Messias** as part of my studies and practice in software development.

If you liked the project, feel free to leave a ⭐ on the repository.
