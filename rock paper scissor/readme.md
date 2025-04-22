# Rock Paper Scissors Game - Design Principles (In My Own Words)

I created a simple Rock Paper Scissors game using Python. In this game, the user plays against the computer. The computer randomly chooses one of the three options – rock, paper, or scissors – and the user inputs their choice. Then, the game checks who wins. While writing this code, I tried to follow several important design principles. Here’s how I used them:

---

## 1. KISS (Keep It Simple, Stupid)

I kept the code as simple as possible. I used only one class and one main method to run the game. The logic is clear, and everything is easy to understand. This way, if someone else reads my code, they won’t get confused.

---

## 2. DRY (Don’t Repeat Yourself)

I used a single set of conditions to check who wins. Instead of writing multiple “if-else” statements again and again, I wrote all the win conditions in one place. This helped me avoid repeating the same logic.

---

## 3. Single Responsibility Principle

My class RockPaperScissors is only responsible for one thing – the game. It stores the possible choices and runs the game logic. It doesn’t handle anything else like saving scores or making menus. That’s how I made sure this class has only one job.

---

## 4. Separation of Concerns (SoC)

Inside the play() method, I handled each part of the game step-by-step:
- First, I asked the user to choose.
- Then, the computer randomly chose.
- After that, the game logic checked who won.
- Finally, I printed the result.

Each part is clearly separated, which makes the code neat and easy to follow.

---

## 5. Clean Code Over Clever Code

I didn’t try to be too clever. I used simple variable names like user_choice and computer_choice, and I wrote code that’s easy to read. This makes it easier for me and others to understand and fix the code later.

