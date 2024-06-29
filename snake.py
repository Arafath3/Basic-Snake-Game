from turtle import Turtle

POSIITION = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.make_segments()
        self.head = self.segments[0]

    def make_segments(self):
        for position in POSIITION:
            self.add_segments(position)

    def add_segments(self, position):
        snake_segments = Turtle(shape="square")
        snake_segments.color("white")
        snake_segments.penup()
        snake_segments.goto(position)
        self.segments.append(snake_segments)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        segments = self.segments
        for box_num in range(len(segments) - 1, 0, -1):
            new_x = segments[box_num - 1].xcor()
            new_y = segments[box_num - 1].ycor()
            segments[box_num].goto(new_x, new_y)

        segments[0].forward(MOVE_DISTANCE)

    def up(self):
        first_seg = self.head
        if first_seg.heading() != DOWN:
            first_seg.setheading(UP)

    def down(self):
        first_seg = self.head
        if first_seg.heading() != UP:
            first_seg.setheading(DOWN)

    def left(self):
        first_seg = self.head
        if first_seg.heading() != RIGHT:
            first_seg.setheading(LEFT)

    def right(self):
        first_seg = self.head
        if first_seg.heading() != LEFT:
            first_seg.setheading(RIGHT)
