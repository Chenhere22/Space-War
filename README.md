# Space-War
This is a simple Python-based space battle game implemented using the `turtle` graphics library. The player controls a spaceship, maneuvers through space, and faces off against enemies. The game features collision detection, sound effects, and a graphical interface.

## Features

- **Player Controls**: Control a spaceship using keyboard inputs to move left, right, accelerate, and decelerate.
- **Collision Detection**: Detect collisions between sprites (e.g., the player and enemies).
- **Lives System**: The player has a limited number of lives.
- **Customizable Background**: The game uses a background image (`bg.gif`), which can be customized.
- **Sound Effects**: Plays sound effects using the `playsound` module.

## Requirements

- Python 3.x
- `turtle` (included with Python)
- `playsound` for sound effects: Install via `pip install playsound==1.2.2`
- `Pillow` for image support: Install via `pip install Pillow`
- `tkinter` (comes pre-installed with Python on most systems)

## How to Play

1. **Move**: Use the following keys to control the player:
   - Left arrow key: Turn left.
   - Right arrow key: Turn right.
   - Up arrow key: Accelerate.
   - Down arrow key: Decelerate.

2. **Objective**: Navigate your spaceship through space and avoid collisions with enemies.

## Installation

1. Clone the repository or download the source code.

```bash
git clone <repository-url>
```

2. Install the required dependencies.

```bash
pip install playsound==1.2.2 Pillow
```

3. Ensure that the `bg.gif` image is in the same directory as the Python script.

4. Run the game.

```bash
python spacewar.py
```

## Game Assets

- `bg.gif`: The background image used in the game. You can replace this image with any other image by ensuring it is placed in the same directory as the script and is named `bg.gif`.

## Customization

- Modify the `Sprite` class to add more enemies or change the behavior of existing ones.
- Adjust the player's speed and controls by modifying the `Player` class.
- 
## Acknowledge
I appreciate the video from TokyoEdtech

## License

This project is open-source. You are free to modify and distribute it as you like.
