#Michael's space program
#Feb 4th 2016
#Rev 0.2.3
#Author: Michael Olson

import math, pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280,720))

#RGB Color values
BLACK =   0,   0,   0
WHITE = 255, 255, 255
BLUE =    0,   0, 255
GREEN =   0, 255,   0
RED =   255,   0,   0

#Value definitions
angle = 0
anglerad = math.radians(angle)
scalemin = 20


class Ship(): #Overall Ship data and actions
    def __init__(self): 
        self.capsule_info = capsule,center_of_mass #adds capsule and center of mass
        self.ship = [self.capsule_info]
        
    def add (self, part, follow):   #function for adding parts to the ship
        print("ship.add")
        if part == "tank" or part == "engine":
            part = Part(part)
            part_info = part, follow
            self.ship.append (part_info)
        else:
            print ("part not regognized") 
        
    def draw(self): #Gathers all ship parts and tells them to draw themsleves
        self.shiplength = (len(self.ship))
        x_list = []
        y_list = []
        for i in range (self.shiplength):   #Finding all ship parts
            temp_part_info = self.ship[i]
            temp_part = temp_part_info[0]
            temp_follow = temp_part_info[1]
            temp_part.draw(temp_follow)
        for i in range (self.shiplength): #finds the furthest points of the ship
            temp_part_info = self.ship[i]
            temp_part = temp_part_info[0]
            x_list.append(temp_part.imagerect.left)
            x_list.append(temp_part.imagerect.right)
            y_list.append(temp_part.imagerect.top)
            y_list.append(temp_part.imagerect.bottom)
        pygame.display.update(min(x_list),      #updates only the ship
            min(y_list),max(x_list),max(y_list))
        
class Capsule():    #Capsule class
    
    def __init__(self):
        self.x = 200
        self.y = 200
        self.image = pygame.image.load("MSP_capsule.png").convert()
        self.speed = [1,1]
    def draw(self,x):
        self.x = x.x
        self.y = x.y
        
        imageafter = pygame.transform.rotate (self.image,angle)
        imageafter = pygame.transform.scale (imageafter,(scale,scale))
        
        self.imagerect = imageafter.get_rect()
        self.imagerect = self.imagerect.move(self.x,self.y)
        
        screen.blit(imageafter,self.imagerect)

        print("SLOW DOWN")
    
class Center_of_mass(): #Center of mass, currently stagnent
    def __init__(self):
        self.x = 200
        self.y = 200
        
class Part(): #Class for a part attached to botom

    def __init__(self,part):
        if part == "tank":
            self.image = pygame.image.load("MSP_fuel.png")
        if part == "engine":
            self.image = pygame.image.load("MSP_engine.png")
        
    def draw(self,follow):
        
        follow_x = follow.x
        follow_y = follow.y
        
        div_scale = scalemin/50 #changes scale for calculations
        
        #Calculations for putting it below previous peice
        a = follow_x + math.fabs(10*div_scale*math.sin(2*anglerad))+(25*div_scale)
        b = math.sin(anglerad+(math.pi*7/4))*(35*div_scale)
        bottom_left_x = b+a                 

        d = follow_y + math.fabs(10*div_scale*math.sin(2*anglerad))+(25*div_scale)
        e = math.cos(anglerad+(math.pi*7/4))*(35*div_scale)
        bottom_left_y = e + d

        new_e = math.cos(anglerad+(math.pi*1/4))*(35*div_scale)
        new_b = math.sin(anglerad+(math.pi*1/4))*(35*div_scale)

        new_a = bottom_left_x + new_b 
        new_d = bottom_left_y + new_e 

        self.x = new_a -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
        self.y = new_d -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)

        #changing image
        imageafter = pygame.transform.rotate (self.image,angle)
        imageafter = pygame.transform.scale (imageafter,(scale,scale))

        self.imagerect = imageafter.get_rect()
        self.imagerect = self.imagerect.move(self.x,self.y)
        
        #blit the image
        screen.blit(imageafter,self.imagerect)
        
def ship_creation(): # Builing the image
    done = False
    while done == False:
        
        choice = input ("Would you like to add a peice? (yes/no)")
        if choice == "yes":
            i = len(ship.ship)-1
            print (i)
            choice = input ("What peice would you like to add?(only have engine and tank rn)")
            ship.add (choice, ship.ship[i][0])
        elif choice == "no": done = True
        else: print("please say yes or no")
        
def re_white(): #blanks the area that the ship is in after every draw
    x_list = []
    y_list = []
    for i in range (ship.shiplength):   #finds the limits of the ship

        temp_part_info = ship.ship[i]
        temp_part = temp_part_info[0]
        x_list.append(temp_part.imagerect.left)
        x_list.append(temp_part.imagerect.right)
        y_list.append(temp_part.imagerect.top)
        y_list.append(temp_part.imagerect.bottom)
    screen.fill(WHITE,(min(x_list),
            min(y_list),max(x_list),max(y_list)))
   
#Initial order of making stuff
capsule = Capsule()
center_of_mass = Center_of_mass()
ship = Ship()
ship_creation()

scale = int(scalemin*(math.fabs(0.4*math.sin(2*anglerad))+1)) 
screen.fill(WHITE)
ship.draw()

while True: #MAIN GAME LOOP
    
    angle = angle +.5 #temp angle changing to test visuals
    
    anglerad = math.radians(angle)
    if angle == 360: angle = 0
    
    #changes the scale for rotating images 
    scale = int(scalemin*(math.fabs(0.4*math.sin(2*anglerad))+1))
    
    for event in pygame.event.get():    #im not completly sure what it does
        if event.type == pygame.QUIT: sys.exit()#but i think it makes it easier to quit
        
    re_white()#blanks area affected
    ship.draw()# draws and updates the ship
    pygame.display.flip() #idk this one either something about updating screen
    
    
    
    
    
