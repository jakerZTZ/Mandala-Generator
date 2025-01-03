import turtle
import random

def draw_circle_pattern(t, radius, step_angle, color):
    """Draws a circular pattern with the given radius and step angle."""
    t.color(color)
    for _ in range(int(360 / step_angle)):
        t.circle(radius)
        t.right(step_angle)

def draw_mandala():
    """Creates a mandala design using Turtle graphics."""
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Mandala Art")

    artist = turtle.Turtle()
    artist.speed(0)
    artist.hideturtle()

    colors = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#9B59B6"]

    # Draw multiple layers of circles
    for i in range(6):
        color = random.choice(colors)
        radius = 50 + i * 20
        step_angle = random.choice([10, 15, 20])
        draw_circle_pattern(artist, radius, step_angle, color)

    # Add decorative lines
    for i in range(12):
        artist.penup()
        artist.goto(0, 0)
        artist.pendown()
        artist.color(random.choice(colors))
        artist.setheading(i * 30)
        artist.forward(200)

def start_animation():
    """Waits for a keypress to start the animation."""
    screen = turtle.Screen()
    screen.listen()
    screen.onkey(draw_mandala, "1")  # Press '1' to start
    screen.mainloop()

if __name__ == "__main__":
    start_animation()
