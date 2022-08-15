from tkinter import messagebox,Tk
import tkinter
import pygame
import andom

# initializing the constructor
pygame.init()
  
# screen dimensions
dime = (900,600)
screen = pygame.display.set_mode(dime)
bg= pygame.image.load("Arr.png")

# white color for font on button
#color is based on Red Green Blue 
color = (255,255,255) #white
# color change for button
light_color = (170,170,170)
dark_color= (100,100,100)
  
# constants based on screen dimensions
width = screen.get_width()
height = screen.get_height()
screen.blit(bg,(0,0))  
# defining a font and test for butttons
btn_font = pygame.font.SysFont('Corbel',35)
text =btn_font.render('Quit', True , color)

while True:
      
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2 <= mouse[0] <= width/2+40 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()
                tk= Tk()
                messagebox.showinfo('Close','Pygame will be closing the window')     
                tk.destroy()
                #andom.factorial(10)

    # fills the screen with a color
    # screen.fill((220,220,220))
      
    # gets mouse coordiates
    mouse = pygame.mouse.get_pos()
      
    # if mouse is hovered on a button it
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen,light_color,[width/2,height/2,100,40])
          
    else:
        pygame.draw.rect(screen,dark_color,[width/2,height/2,100,40])
      
    # positioning text on button
    screen.blit(text,(width/2+20,height/2))
    
    pygame.display.update()
