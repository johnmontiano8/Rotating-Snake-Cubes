# Rotating Snake Cubes

This project is a simple OpenGL application using Pygame to render and animate a series of rotating cubes.

## Requirements

- Python 3.x
- Pygame
- PyOpenGL

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install the required libraries using pip:
   ```sh
   pip install pygame PyOpenGL
   ```

## Running the Application

To run the application, execute the following command in your terminal:

```sh
python RotatingSnakeCubes.py
```

Workspace
(rerun without)
Collecting workspace information

Here is a README.md file for your project:

## Controls

- A: Move the cubes to the left.
- D: Move the cubes to the right.
- W: Start rolling the cubes upwards.
- S: Start rolling the cubes downwards.
- R: Start rotating the cubes automatically.

## Code Overview

- The main script is RotatingSnakeCubes.py.
- The script initializes a Pygame window with an OpenGL context.
- It defines the vertices and triangles for the cubes.
- The draw_cube function renders a single cube with a specified color.
- The draw_cubes function renders a series of cubes with different colors.
- The main loop handles user input and updates the cube transformations.

## License

This project is licensed under the MIT License.
