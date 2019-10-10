import turtle

from game_modules import objects

playing = True

def close_screen():
    global playing
    playing = False

screen = objects.create_screen("Atari Combat", 1000, 800)
root = screen.getcanvas().winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", close_screen)

while playing:
    screen.update()
