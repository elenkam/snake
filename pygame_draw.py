
import pygame


bg_color=(150,150,250) #tuple   RED, GREEN, BLUE


screen = pygame.display.set_mode([500,500])

        
pygame.init()
pygame.display.set_caption("Game1")
 
screen.fill(bg_color)
#game_icon = pygame.image.load('ikonka.png')
#pygame.display.set_icon(game_icon)


#pygame.draw.rect(screen,(50,50,50),[10,10,20,20]) 

#pygame.draw.rect(screen,(50,50,50),[100,0,100,20]) 


def nakresli_obdelnik(x1,y1,x2,y2):
    sizex=x2-x1
    sizey=y2-y1
    pygame.draw.rect(screen,(50,50,50),[x1,y1,sizex,sizey]) 
    
#nakresli_obdelnik(100,100,150,150)
#
#for i in range(10):
#    pygame.draw.rect(screen,(20*i,0,0),[50*(9-i),50*i,50,50])
#    
#
#
#pygame.draw.rect(screen,(0,0,100),[150,150,50,50])
#pygame.draw.rect(screen,bg_color,[155,155,40,40])    
#  
#pygame.draw.rect(screen,(250,125,0),[275,225,40,40],5)    
#  
for i in range(10):
    for j in range(10):
        pygame.draw.rect(screen,(255,255,255),[i*40,j*40,39,39])   











#Toto jsme zatím nedělali

done=False
t=0



while not done:  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
            pass
        if (keys[pygame.K_LEFT]):
            pass
        if (keys[pygame.K_UP]):
            pass
        if (keys[pygame.K_DOWN]):
            pass
        if (keys[pygame.K_RETURN]):
            pass
        
        
    pygame.display.flip()   
    
    t=t+10
    pygame.time.wait(10)

    if (t%100==0):
        pass
    
pygame.display.quit()