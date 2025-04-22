# Design Principles in My Python Mini-Games

This file explains how I applied software design principles while creating my mini-games using Python. These principles help me write code that is simple, readable, and easier to maintain or improve later.

---

## Rock Paper Scissors Game – Design Principles in Action

In this game, the player and the computer each choose either rock, paper, or scissors. The winner is decided using the basic rules of the game.

### 1. KISS (Keep It Simple, Stupid)

I made sure the game was not too complicated:
- I used one class called RockPaperScissors.
- The play() method handles everything: user input, computer choice, and checking who wins.
- The game only runs for one round.

This makes the game simple to play and easy for anyone (even beginners) to understand the code.

### 2. DRY (Don’t Repeat Yourself)

I followed the DRY principle by:
- Using one set of if, elif, and else statements to check the game result.
- Avoiding writing the same logic multiple times.
- Storing the possible choices (rock, paper, scissors) in a list so that I could reuse it for both the computer's and the player's choices.

This helps me avoid bugs and saves time when I want to change or add something.

### 3. Single Responsibility Principle

The RockPaperScissors class is only responsible for handling the game. It doesn’t do anything else like scorekeeping or handling multiple rounds. This makes the code cleaner and gives each part one clear job.

### 4. Separation of Concerns

I split the code into logical sections:
- The class is responsible for gameplay.
- The main part of the script only creates the game object and starts the game.

This way, the logic of the game and running the program are kept separate, which helps with testing or future improvements.

### 5. YAGNI (You Aren’t Gonna Need It)

I didn’t add extra features like a scoreboard or a menu system, because those were not required at this stage. I focused only on what the game actually needed to work properly.

### 6. Clean Code > Clever Code

Instead of writing tricky code, I focused on writing clean and readable code:
- I used easy-to-understand variable names like user_choice and computer_choice.
- My logic is written in a straightforward way, so anyone reading the code can understand it quickly.

---

## Turtle Catch Game – Design Principles in Action

In this game, the player moves a green turtle around the screen to catch a red circle. When the player touches the red circle, it moves to a new random location.

### 1. KISS (Keep It Simple, Stupid)

I designed the game to be very simple:
- The screen is set up with a basic size and color.
- The player can move using the arrow keys.
- The target appears randomly and moves again when it’s caught.

This simplicity helps make the game fun and fast to test or modify.

### 2. DRY (Don’t Repeat Yourself)

I created one function for each movement direction:
- move_up()
- move_down()
- move_left()
- move_right()

Each function only changes the turtle’s x or y coordinate. I didn’t copy the same logic multiple times. This makes the code easy to manage and update.

### 3. Single Responsibility Principle

Each part of the game does just one thing:
- The player turtle is only responsible for moving.
- The target turtle only needs to be caught.
- The movement functions only handle direction.
- The game loop only checks if the player touches the target.

By giving each section one job, the code stays clear and focused.

### 4. Separation of Concerns

I organized the code into separate sections:
- Setting up the screen.
- Creating turtles for the player and target.
- Writing the movement logic.
- Setting up the keyboard controls.
- Running the game loop.

Each section is easy to read and change if needed.

### 5. YAGNI (You Aren’t Gonna Need It)

I only added the basic features that were needed:
- There is no scoring system.
- There is no countdown or levels.

This kept the game light and focused on the core goal — catching the target.

### 6. Clean Code > Clever Code

I used clear and meaningful names for everything:
- player for the turtle you move.
- target for the red circle.
- move_up, move_down, etc., for each direction function.
-
- ## Conclusion

By using these design principles, I was able to write Python code that is:
- Simple
- Easy to read
- Easy to change later
- Less likely to have bugs

These principles are helpful not just for small games, but also for bigger projects I might work on in the future. They help me become a better programmer by encouraging clean and organized thinking while writing code.
