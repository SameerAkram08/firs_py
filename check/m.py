# import tkinter as tk

# def hello():
#     label.config(text="Hello, Tkinter!")

# root = tk.Tk()

# label = tk.Label(root, text="Welcome to Tkinter")
# label.pack()

# button = tk.Button(root, text="Click Me", command=hello)
# button.pack()

# root.mainloop()

import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("400x400")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.spawn_food()

        self.direction = "Right"
        self.change_to = self.direction

        self.root.bind("<KeyPress>", self.on_key_press)

        self.score = 0
        self.speed = 100

        self.update()

    def spawn_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return x, y

    def on_key_press(self, event):
        key = event.keysym
        if key == "Left" and self.direction != "Right":
            self.change_to = "Left"
        if key == "Right" and self.direction != "Left":
            self.change_to = "Right"
        if key == "Up" and self.direction != "Down":
            self.change_to = "Up"
        if key == "Down" and self.direction != "Up":
            self.change_to = "Down"

    def move(self):
        new_head = ()
        if self.change_to == "Right":
            new_head = (self.snake[0][0] + 10, self.snake[0][1])
        if self.change_to == "Left":
            new_head = (self.snake[0][0] - 10, self.snake[0][1])
        if self.change_to == "Up":
            new_head = (self.snake[0][0], self.snake[0][1] - 10)
        if self.change_to == "Down":
            new_head = (self.snake[0][0], self.snake[0][1] + 10)

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1
            self.speed -= 2
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def update(self):
        self.move()

        if (
            self.snake[0] in self.snake[1:]
            or self.snake[0][0] < 0
            or self.snake[0][0] >= 400
            or self.snake[0][1] < 0
            or self.snake[0][1] >= 400
        ):
            self.canvas.create_text(
                200, 200, text="Game Over", font=("Helvetica", 30), fill="red"
            )
            return

        self.canvas.delete("all")

        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0],
                segment[1],
                segment[0] + 10,
                segment[1] + 10,
                fill="green",
                outline="black",
            )

        self.canvas.create_oval(
            self.food[0],
            self.food[1],
            self.food[0] + 10,
            self.food[1] + 10,
            fill="red",
        )

        self.canvas.create_text(
            50, 10, text=f"Score: {self.score}", fill="white", anchor="nw"
        )

        self.root.after(self.speed, self.update)

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
