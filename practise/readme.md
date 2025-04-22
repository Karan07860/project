# Turtle Catch Game - Design Principles (In My Own Words)

I created a fun little game in Python using the turtle module. In this game, there's a green turtle that I can move using the arrow keys on my keyboard. The goal is to catch a red circle that keeps appearing in random spots on the screen. Every time I catch it, it moves to another place.

While making this game, I followed some basic software design principles that help make code clean, easy to understand, and easy to improve in the future.

---

## 1. KISS (Keep It Simple, Stupid)

I made sure the game was not too complex.  
- The player only needs to use four arrow keys to play.  
- The game doesn't have any extra things like timers, scores, or levels.

By keeping the idea and code simple, it’s easy to play and also easy to look at and understand the code. This also helps if I want to teach someone or show this game to a beginner.

---

## 2. DRY (Don’t Repeat Yourself)

Instead of copying the same code over and over for different directions, I wrote four small functions:
- move_up()  
- move_down()  
- move_left()  
- move_right()

Each function only changes the position of the turtle in one direction. This avoids repeating similar lines of code and makes it easier to update things later if needed.

For example, if I want the turtle to move faster, I can just change one number inside each function instead of changing it in 4 different places.

---

## 3. Single Responsibility Principle

In my game:
- The *screen* is only responsible for showing the game area.  
- The *player turtle* is only for movement.  
- The *target turtle* is only for being "caught."  
- The *movement functions* only move the turtle.  
- The *game loop* checks if the player caught the target.

Each part of my code has just one job. That makes my code easier to read and fix. If I need to change the way the turtle moves, I only need to go to the movement functions. If I want to change how the target behaves, I look at the part where I created the target.

---

## 4. Separation of Concerns (SoC)

I organized the code into sections that each handle different things:
- The *first part* sets up the screen.  
- The *second part* creates the turtles (player and target).  
- Then I have the *functions for movement*.  
- After that, I *listen for key presses*.  
- Finally, the *game loop* keeps running and checks if the player caught the target.

This way, I know exactly where to look if I need to update or fix one part. It keeps everything clean and not all mixed up.

---

## 5. Clean Code > Clever Code

I didn’t try to be fancy with tricky code.  
Instead, I used simple variable names like:
- player
- target
- move_up
- screen

This makes the code easier to read — not just for me, but also for others. I don’t want people to get confused when they look at my code. I want them to say, “Oh, I understand what this does!”

---

## 6. YAGNI (You Aren’t Gonna Need It)

Right now, my game doesn’t have levels, scoring, sound, or any advanced features. That’s because I didn’t need those things for this version of the game.

By not adding extra stuff too early, I kept the code clean. I can always add those features later if I really need them.
