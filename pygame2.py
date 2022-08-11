from tkinter import messagebox
import pygame
import sys
from andom import factorial

# initializing the constructor
pygame.init()
  
# screen dimensions
dime = (800,600)
screen = pygame.display.set_mode(dime)
screen =pygame.display.set_caption("Menu")

menu_state="menu"

# white color for font on button
#color is based on Red Green Blue 
color = (255,255,255) #white
# color change for button
light_color = (170,170,170)
dark_color= (100,100,100)
  
# constants based on screen dimensions
btn_font=pygame.font.SysFont("arialback",30)
#making a button class for all button to follow
class Buttons():
    def __init__(self,x,y,scale): 
        self.clicked=False
    def draw(self, face):
        action=False
        #getting mouse coordinates
        mouse=pygame.mouse.get_pos()
        #hover and click condition of mouse
        if self.rect.collidepoint(po):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True

            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            face.blit((self.rectx,self.rect.y))
            return action

#MAKING BUTTON

close_btn=Buttons(304,125,1)
pointless_btn=Buttons(297,250,1)
python_btn=Buttons(245,25,1)
messagebox_btn=Buttons(334,325,1)


# running game loop
while True:
    width= screen.get_width()
    height=screen.get_height()

    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,light_color,[width/2,height/2,100,40])
          
    else:
        pygame.draw.rect(screen,dark_color,[width/2,height/2,100,40])
    if menu_state=="main":
        if close_btn.draw(screen):
            pygame.quit()
        if pointless_btn.draw(screen):
            print("Hello!", 'Mine Turtle')
        if python_btn.draw(screen):
            factorial(5)
        if messagebox_btn.draw(screen):
            messagebox.showinfo('INFO BOX','The fitness gram pacer test is a multi fitness exam used to measure one ability')


    for e in pygame.event.get():
        if e.type==pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+40 and height/2 <= mouse[1] <= height/2+40:
                messagebox.showwarning("Button has been pressed")
        if e.type==pygame.quit():
            pygame.quit()

    pygame.display.update()