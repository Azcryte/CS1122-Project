import pygame
import random
import math

import mage
import warrior
import rogue

BLACK = (0, 0, 0)
GRAY = (95, 95, 95)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

TEXT_XPOS = 20
TEXT_YPOS = [365, 410, 455]
CLASS_SELECT_Y = [150, 195, 200]
CLASS_SELECT_X = [20, 275, 530]
ACTION_CHOICE_X = [20, 250, 500]
HEALTH_TEXT_X = [20, 500]
HEALTH_TEXT_Y = 100

class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename):
        super(Sprite,self).__init__()
        sprite = pygame.image.load(filename).convert()
        self.image = sprite
        #self.rect = pygame.Rect((0,0), (self.image.get_width(), self.image.get_height()))
        #self.image = pygame.transform.scale(sprite, (100,100))
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CS1122 Project")
 
done = False
clock = pygame.time.Clock()

spriteList = pygame.sprite.Group()
ball = Sprite("Ball Graphic.png")
trophy = Sprite("trophy.png")

mage = mage.Mage()
warrior = warrior.Warrior()
rogue = rogue.Rogue()

classes = [mage, warrior, rogue]

"""
class 0 == mage
class 1 == warrior
class 1 == rogue
"""
player1Class = -1
player2Class = -1

"""
state -2: player 2 won
state -1: player 1 won
state 0: start menu
state 1: player 1 class select
state 2: player 2 class select
state 3: player 1 turn
state 4: player 2 turn
"""
state = 0

#ball = Sprite("mageIdle.png")
#spriteList.add(ball)
font = pygame.font.SysFont('Calibri', 30, False, False)
pastActionText = font.render("Insert Text Here", True, WHITE)

# -------- Main Program Loop -----------
while not done:
# --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
# ----------- Game Logic --------------------------------

    key = pygame.key.get_pressed()

    if state == 0:
        if key[pygame.K_RETURN] or key[pygame.K_SPACE]:
            state = 1

        #rect_x_pos += rect_x_vel
        #rect_y_pos += rect_y_vel
        #if rect_y_pos> 500 or rect_y_pos < 0:
        #    rect_y_vel = rect_y_vel * -1
        #if rect_x_pos > 700 or rect_x_pos < 0:
        #    rect_x_vel = rect_x_vel * -1
        
        #ball.rect.x = rect_x_pos
        #ball.rect.y = rect_y_pos

    # ------- player 1 class select ---------
    if state == 1:
        if key[pygame.K_1]:
            player1Class = 0
            #classes[player1Class].image = pygame.transform.flip(classes[player1Class].image, True, False)
            state = 2
        elif key[pygame.K_2]:
            player1Class = 1
            #classes[player1Class].image = pygame.transform.flip(classes[player1Class].image, True, False)
            state = 2
        elif key[pygame.K_3]:
            player1Class = 2
            #classes[player1Class].image = pygame.transform.flip(classes[player1Class].image, True, False)
            state = 2

    # ------- player 2 class select ---------
    if state == 2:
        if player1Class == 0:
            if key[pygame.K_2]:
                player2Class = 1
                state = 3
            elif key[pygame.K_3]:
                player2Class = 2
                state = 3
        elif player1Class == 1:
            if key[pygame.K_1]:
                player2Class = 0
                state = 3
            elif key[pygame.K_3]:
                player2Class = 2
                state = 3
        elif player1Class == 2:
            if key[pygame.K_1]:
                player2Class = 0
                state = 3
            elif key[pygame.K_2]:
                player2Class = 1
                state = 3
                
    # ----------- player 1 turn ----------  
    if state == 3:
        #attack
        if key[pygame.K_q]:
            rand = random.randint(0, 10)
            dmgDealt = 0
            if rand == 2:
                dmgDealt = int(math.floor(classes[player1Class].attack * 1.5))
                classes[player2Class].subtractHealth(dmgDealt)
                pastActionText = font.render("Player 1 has critical attacked for {0} damage".format(dmgDealt), True, BLACK)
            else:
                dmgDealt = classes[player1Class].attack
                classes[player2Class].subtractHealth(dmgDealt)
                pastActionText = font.render("Player 1 has attacked for {0} damage".format(dmgDealt), True, BLACK)
            classes[player1Class].update()
            state = 4
        if classes[player1Class].lastSpecial > classes[player1Class].cooldown:
            if key[pygame.K_w]:
                rand = random.randint(0, 10)
                dmgDealt = 0
                if rand == 2:
                    dmgDealt = int(math.floor(classes[player1Class].special * 1.5))
                    classes[player2Class].subtractHealth(dmgDealt)
                    pastActionText = font.render("Player 1 has critical special attacked for {0} damage".format(dmgDealt), True, BLACK)
                else:
                    dmgDealt = classes[player1Class].special
                    classes[player2Class].subtractHealth(dmgDealt)
                    pastActionText = font.render("Player 1 has special attacked for {0} damage".format(dmgDealt), True, BLACK)
                classes[player1Class].lastSpecial = 0
                classes[player1Class].update()
                state = 4
        if classes[player1Class].potionsUsed < 3:
            if key[pygame.K_e]:
                classes[player1Class].usePotion()
                pastActionText = font.render("Player 1 has used a potion and healed to {0} health".format(classes[player1Class].health), True, BLACK)
        
                classes[player1Class].update()
                state = 4

    # ----------- player 2 turn ----------  
    if state == 4:
        if key[pygame.K_i]:
            rand = random.randint(0, 10)
            dmgDealt = 0
            if rand == 2:
                dmgDealt = int(math.floor(classes[player2Class].attack * 1.5))
                classes[player1Class].subtractHealth(dmgDealt)
                pastActionText = font.render("Player 2 has critical attacked for {0} damage".format(dmgDealt), True, BLACK)
            else:
                dmgDealt = classes[player2Class].attack
                classes[player1Class].subtractHealth(dmgDealt)
                pastActionText = font.render("Player 2 has attacked for {0} damage".format(dmgDealt), True, BLACK)
            classes[player2Class].update()
            state = 3
        if classes[player2Class].lastSpecial > classes[player2Class].cooldown:
            if key[pygame.K_o]:
                rand = random.randint(0, 10)
                dmgDealt = 0
                if rand == 2:
                    dmgDealt = int(math.floor(classes[player2Class].special * 1.5))
                    classes[player1Class].subtractHealth(dmgDealt)
                    pastActionText = font.render("Player 2 has critical attacked for {0} damage".format(dmgDealt), True, BLACK)
                else:
                    dmgDealt = classes[player2Class].special
                    classes[player1Class].subtractHealth(dmgDealt)
                    pastActionText = font.render("Player 2 has attacked for {0} damage".format(dmgDealt), True, BLACK)
                classes[player2Class].lastSpecial = 0
                classes[player2Class].update()
                state = 3
        if classes[player2Class].potionsUsed < 3:
            if key[pygame.K_p]:
                classes[player2Class].usePotion()
                pastActionText = font.render("Player 1 has used a potion and healed to {0} health".format(classes[player2Class].health), True, BLACK)
            
                classes[player2Class].update()
                state = 3
            
    # --------- reset -----------
    #if key[pygame.K_ESCAPE]:
    #    state = 0
            
    mage.updateFrame()
    rogue.updateFrame()
    warrior.updateFrame()
 
# --------------------------------------------------------------
    screen.fill(WHITE)
 
# ----------- Drawing ----------------------------
    spriteList.empty()
    if state == -2:
        #p2 won
        #trophy.image = pygame.transform.scale(trophy, (240, 240))
        trophy.rect.x = 20
        trophy.rect.y = 100

        font = pygame.font.SysFont('Calibri', 30, True, False)
        text = font.render("Player 2 has won the match!", True, BLACK)
        screen.blit(text, [300, 200])
        spriteList.add(trophy)

        spriteList.draw(screen)
        
    if state == -1:
        #p1 won
        #trophy = pygame.transform.scale(trophy, (240, 240))
        trophy.rect.x = 20
        trophy.rect.y = 100
        
        font = pygame.font.SysFont('Calibri', 30, True, False)
        text = font.render("Player 1 has won the match!", True, BLACK)
        screen.blit(text, [300, 200])
        spriteList.add(trophy)

        spriteList.draw(screen)
        
    if state == 0:
        #                           font, size, bold, italics
        font = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("VERY FANCY TITLE SCREEN!!!", True, BLACK)
        font = pygame.font.SysFont('Calibri', 30, False, False)
        text2 = font.render("press enter to continue", True, BLACK)
        #text coordinates are NOT centered
        screen.blit(text, [80, 150])
        screen.blit(text2, [200, 250])

        spriteList.draw(screen)

    # ------- player 1 class select ---------
    if state == 1:        
        spriteList.add(mage)
        mage.rect.x = CLASS_SELECT_X[0]
        mage.rect.y = CLASS_SELECT_Y[0]
        spriteList.add(warrior)
        warrior.rect.x = CLASS_SELECT_X[1]
        warrior.rect.y = CLASS_SELECT_Y[1]
        spriteList.add(rogue)
        rogue.rect.x = CLASS_SELECT_X[2]
        rogue.rect.y = CLASS_SELECT_Y[2]
        #spriteList.add(ball)

        spriteList.draw(screen)

        # drawing UI        
        pygame.draw.rect(screen, BLACK, [0, 350, 700, 500])
        pygame.draw.rect(screen, WHITE, [5, 355, 690, 140])
        font = pygame.font.SysFont('Calibri', 22, False, False)
        mageSelect = font.render("1 for Mage", True, BLACK)
        warriorSelect = font.render("2 for Warrior", True, BLACK)
        rogueSelect = font.render("3 for rogue", True, BLACK)
        screen.blit(mageSelect, [CLASS_SELECT_X[0], TEXT_YPOS[0]])
        screen.blit(warriorSelect, [CLASS_SELECT_X[1], TEXT_YPOS[0]])
        screen.blit(rogueSelect, [CLASS_SELECT_X[2], TEXT_YPOS[0]])
        #text1 = font.render("1 for Mage               2 for Warrior               3 for Rogue", True, BLACK)
        #screen.blit(text1, [TEXT_XPOS, TEXT_YPOS[0]])
        font = pygame.font.SysFont('Calibri', 30, False, False)
        text2 = font.render("Player 1, select your class", True, BLACK)
        screen.blit(text2, [TEXT_XPOS, TEXT_YPOS[1]])
        #text2 = font.render("Player 1, select your class", True, BLACK)
        #screen.blit(text2, [TEXT_XPOS, TEXT_YPOS[2]])

    # ------- player 2 class select ----------
    if state == 2:
        spriteList.add(mage)
        mage.rect.x = CLASS_SELECT_X[0]
        mage.rect.y = CLASS_SELECT_Y[0]
        spriteList.add(warrior)
        warrior.rect.x = CLASS_SELECT_X[1]
        warrior.rect.y = CLASS_SELECT_Y[1]
        spriteList.add(rogue)
        rogue.rect.x = CLASS_SELECT_X[2]
        rogue.rect.y = CLASS_SELECT_Y[2]
        #spriteList.add(ball)

        font = pygame.font.SysFont('Calibri', 22, False, False)
        mageSelect = font.render("1 for Mage", True, BLACK)
        warriorSelect = font.render("2 for Warrior", True, BLACK)
        rogueSelect = font.render("3 for rogue", True, BLACK)
        spriteList.remove(classes[player1Class])
                  
        spriteList.draw(screen)
        
        # drawing UI
        pygame.draw.rect(screen, BLACK, [0, 350, 700, 500])
        pygame.draw.rect(screen, WHITE, [5, 355, 690, 140])
        if player1Class == 0:
            screen.blit(warriorSelect, [CLASS_SELECT_X[1], TEXT_YPOS[0]])
            screen.blit(rogueSelect, [CLASS_SELECT_X[2], TEXT_YPOS[0]])
        if player1Class == 1:       
            screen.blit(mageSelect, [CLASS_SELECT_X[0], TEXT_YPOS[0]])
            screen.blit(rogueSelect, [CLASS_SELECT_X[2], TEXT_YPOS[0]])
        if player1Class == 2:
            screen.blit(mageSelect, [CLASS_SELECT_X[0], TEXT_YPOS[0]])
            screen.blit(warriorSelect, [CLASS_SELECT_X[1], TEXT_YPOS[0]])
        #screen.blit(text1, [TEXT_XPOS, TEXT_YPOS[0]])
        font = pygame.font.SysFont('Calibri', 30, False, False)
        text2 = font.render("Player 2, select your class", True, BLACK)
        screen.blit(text2, [TEXT_XPOS, TEXT_YPOS[1]])
        #text2 = font.render("Player 1, select your class", True, BLACK)
        #screen.blit(text2, [TEXT_XPOS, TEXT_YPOS[2]])

    # ----------- player 1 turn ----------        
    if state == 3:
        p1 = classes[player1Class]
        p2 = classes[player2Class]
        p1.rect.x = CLASS_SELECT_X[0]
        p1.rect.y = CLASS_SELECT_Y[1]
        #p1.image = pygame.transform.flip(p1.image, True, False)
        if p1 == mage:
            p1.rect.y -= 50
        spriteList.add(p1)
        p2.rect.x = CLASS_SELECT_X[2]
        p2.rect.y = CLASS_SELECT_Y[1]
        if p2 == mage:
            p2.rect.y -= 50
        spriteList.add(p2)

        classes[player1Class].image = pygame.transform.flip(classes[player1Class].image, True, False)
        spriteList.draw(screen)

        # UI
        player1Health = font.render("Health: {0}".format(classes[player1Class].health), True, BLACK)
        player2Health = font.render("Health: {0}".format(classes[player2Class].health), True, BLACK)
        screen.blit(player1Health, [HEALTH_TEXT_X[0], HEALTH_TEXT_Y])
        screen.blit(player2Health, [HEALTH_TEXT_X[1], HEALTH_TEXT_Y])
        
        pygame.draw.rect(screen, BLACK, [0, 350, 700, 500])
        pygame.draw.rect(screen, WHITE, [5, 355, 690, 140])
        font = pygame.font.SysFont('Calibri', 22, False, False)
        attackText = font.render("'Q' for  Attack", True, BLACK)
        if p1.lastSpecial > p1.cooldown:
            specialText = font.render("'W' for Special", True, BLACK)
        else:
            specialText = font.render("'W' for Special ({0})".format(p1.cooldown - p1.lastSpecial + 1), True, GRAY)
        if p1.potionsUsed >= 3:
            potionText = font.render("'E' for Potion ({0})".format(3 - p1.potionsUsed), True, GRAY)
        else:
            potionText = font.render("'E' for Potion ({0})".format(3 - p1.potionsUsed), True, BLACK)
        screen.blit(attackText, [ACTION_CHOICE_X[0], TEXT_YPOS[0]])
        screen.blit(specialText, [ACTION_CHOICE_X[1], TEXT_YPOS[0]])
        screen.blit(potionText, [ACTION_CHOICE_X[2], TEXT_YPOS[0]])
        font = pygame.font.SysFont('Calibri', 30, False, False)
        text2 = font.render("Player 1, select your action", True, BLACK)
        screen.blit(text2, [TEXT_XPOS, TEXT_YPOS[1]])
        screen.blit(pastActionText, [TEXT_XPOS, TEXT_YPOS[2]])

    # ----------- player 2 turn ----------    
    if state == 4:
        p1 = classes[player1Class]
        p2 = classes[player2Class]
        p1.rect.x = CLASS_SELECT_X[0]
        p1.rect.y = CLASS_SELECT_Y[1]
        if p1 == mage:
            p1.rect.y -= 50
        spriteList.add(p1)
        p2.rect.x = CLASS_SELECT_X[2]
        p2.rect.y = CLASS_SELECT_Y[1]
        if p2 == mage:
            p2.rect.y -= 50
        spriteList.add(p2)

        classes[player1Class].image = pygame.transform.flip(classes[player1Class].image, True, False)
        spriteList.draw(screen)

        # UI
        player1Health = font.render("Health: {0}".format(classes[player1Class].health), True, BLACK)
        player2Health = font.render("Health: {0}".format(classes[player2Class].health), True, BLACK)
        screen.blit(player1Health, [HEALTH_TEXT_X[0], HEALTH_TEXT_Y])
        screen.blit(player2Health, [HEALTH_TEXT_X[1], HEALTH_TEXT_Y])
        
        pygame.draw.rect(screen, BLACK, [0, 350, 700, 500])
        pygame.draw.rect(screen, WHITE, [5, 355, 690, 140])
        font = pygame.font.SysFont('Calibri', 22, False, False)
        attackText = font.render("'I' for  Attack", True, BLACK)
        if p2.lastSpecial > p2.cooldown:
            specialText = font.render("'O' for Special", True, BLACK)
        else:
            specialText = font.render("'O' for Special ({0})".format(p2.cooldown - p2.lastSpecial + 1), True, GRAY)
        if p2.potionsUsed >= 3:
            potionText = font.render("'P' for Potion ({0})".format(3 - p2.potionsUsed), True, GRAY)
        else:
            potionText = font.render("'P' for Potion ({0})".format(3 - p2.potionsUsed), True, BLACK)
        screen.blit(attackText, [ACTION_CHOICE_X[0], TEXT_YPOS[0]])
        screen.blit(specialText, [ACTION_CHOICE_X[1], TEXT_YPOS[0]])
        screen.blit(potionText, [ACTION_CHOICE_X[2], TEXT_YPOS[0]])
        font = pygame.font.SysFont('Calibri', 30, False, False)
        text2 = font.render("Player 2, select your action", True, BLACK)
        screen.blit(text2, [TEXT_XPOS, TEXT_YPOS[1]])
        screen.blit(pastActionText, [TEXT_XPOS, TEXT_YPOS[2]])
        

    #stateText = font.render("State {0}".format(state), True, GRAY)
    #screen.blit(stateText, [0,0])
    
    # --------------- check for winner ---------------------
    if not classes[player1Class].alive:
        state = -2
    if not classes[player2Class].alive:
        state = -1
 
# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    clock.tick(60)

 
# Close the window and quit.
pygame.quit()
