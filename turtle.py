#친구 과제 - 그림그리기

import turtle
import random

win = turtle.Screen()
t1 = turtle.Turtle()
t1.color("blue")
t1.shape("turtle")
t1.penup()
t1.speed(2)

def draw_shape(shape, num):
    for _ in range(num):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t = turtle.Turtle()
        t.penup()
        t.speed(1)
        t.goto(x, y)
        
        if shape == 'circle':
            t.shape('circle')
            t.color('black')
        elif shape == 'square':
            t.shape('square')
            t.color('red')
        elif shape == 'triangle':
            t.shape('triangle')
            t.color('green')

#키 이벤트 처리 함수
def handle_key_1():
    draw_shape('circle', 5)

def handle_key_2():
    draw_shape('square', 5)

def handle_key_3():
    draw_shape('triangle', 5)

#키 이벤트 핸들러 등록
win.onkey(handle_key_1, '1')
win.onkey(handle_key_2, '2')
win.onkey(handle_key_3, '3')
win.listen()

turtle.done()
