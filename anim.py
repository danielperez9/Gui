import tkinter
import time

window_width=900
window_height=900

Ball_init_xpos=50
Ball_init_ypos=50
ball_rad=40
ball_mov=10
Rfr=0.001# refresh rate
def Animation_window():
    window=tkinter.Tk()
    window.title("python Guides")

    window.geometry(f'{window_width}x{window_height}')
    return window

def animation_canvas(window):
    canvas=tkinter.Canvas(window)
    canvas.configure(bg="Blue")
    canvas.pack(fill="both",expand=True)
    return canvas

def anim_ball(window, canvas,xinc,yinc):
    ball=canvas.create_oval(Ball_init_xpos,
    Ball_init_ypos-ball_rad,
    Ball_init_xpos,
    Ball_init_ypos+ball_rad,
    fill="Red", outline="Black", width=4)

    while True:
        canvas.move(ball,xinc,yinc)
        window.update()
        time.sleep(Rfr)
        ball_pos=canvas.coords(ball)
        al,bl,ar,br= ball_pos
        if al<abs(xinc) or ar > window_width-abs(xinc):
            xinc=-xinc
        if bl< abs(yinc) or br > window_height-abs(yinc):
            yinc=-yinc

Animation_Window=Animation_window()
Animation_Canvas=animation_canvas(Animation_Window)
anim_ball(Animation_Window,Animation_Canvas,ball_mov,ball_mov)

