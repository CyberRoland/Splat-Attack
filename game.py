from tkinter import *
import tkinter as tk
import time
from customtkinter import *
import random
from pygame import mixer

def dosom(event):
    global last_click_time, xvelocity, score, ufo_hight, i, apple, minus_five
    current_time = time.time()
    time_diff = current_time - last_click_time
    last_click_time = current_time

    enemy_coords = canvas.coords(ufo)
    click_coords = [event.x, event.y]

    if i == 0:
        canvas.delete(apple)
        apple = canvas.create_image(event.x,event.y,image=appl,anchor=CENTER)


    if (enemy_coords[0] <= click_coords[0] <= enemy_coords[0] + ufo_width) and (enemy_coords[1] <= click_coords[1] <= enemy_coords[1] + ufo_hight):
        print("Enemy hit within 0.5 seconds!")
        xvelocity = random.randint(-10 ,10)  # Increase the speed by 50%
        score += 5
        # mixer.music.load("")
        show_score.configure(text=f"""Score:
{score}""")
    else:
        score -= 1
        show_score.configure(text=f"""Score:
{score}""")
    print(f"{event.x}, {event.y}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


WIDTH =  1920
HEIGHT  = 1080
xvelocity = 1
yvelocity = 1
last_click_time = time.time()
score = 0
i = 0

windy = Tk()
windy.title("Splat Attack")
windy.geometry("1200x563")
windy.attributes('-fullscreen',True)

canvas = Canvas(windy,width=WIDTH,height=HEIGHT)
canvas.pack()

canvas.bind("<Button-1>", dosom)

show_score = CTkLabel(windy, text=f"""Score:
{score}""",
                     font=("Super Boys",55),
                       fg_color='#990606',
                         text_color='#FFF',
                         )
show_score.place(relx=0.5,rely=0.25, anchor='center')


ph =  PhotoImage(file="Python\Tomato bad things\Images\g.png")
bbg = canvas.create_image(0,0,image=ph,anchor=NW)

losefive = PhotoImage(file="Python\Tomato bad things\Images\minus 5.png")
minus_five = canvas.create_image(-10,-10,image=losefive,anchor=CENTER)

appl = PhotoImage(file="Python\Tomato bad things\Images\spalt.png")
apple = canvas.create_image(0,0,image=appl,anchor=CENTER)

photo = PhotoImage(file="Python\Tomato bad things\Images\p.png")
ufo = canvas.create_image(300,550, image=photo,anchor=NW)

ufo_width = photo.width()
ufo_hight = photo.height()

icon = PhotoImage(file='Python\Tomato bad things\Images\Apple.png')
windy.iconphoto(True, icon)
while True:
    cords =  canvas.coords(ufo)
    #print(cords)
    if(cords[0]>=((1500-ufo_width)) or cords[0]<300):
        xvelocity = -xvelocity
    canvas.move(ufo,xvelocity,0)
    windy.update()
    time.sleep(0.005)



windy.mainloop()