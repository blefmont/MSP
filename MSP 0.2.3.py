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
scalemin = 30
rotateleft = False
rotateright = False

class Ship(): #Overall Ship data and actions
    def __init__(self): 
        self.capsule_info = capsule,center_of_mass #adds capsule and center of mass
        self.ship = [self.capsule_info]
        self.first = True
        self.shiplength = (len(self.ship))
        self.part_list = []
        self.follow_list = []
        self.open_part = []
        
    def add (self, part):   #function for adding parts to the ship
        print("ship.add")
        self.open_part.clear()
        self.part_list.clear()
        self.follow_list.clear()
        self.shiplength = len(self.ship)
        for i in range (self.shiplength): #generate a list of only the parts and the followed parts
            temp_part = self.ship[i][0]
            temp_follow = self.ship[i][1]
            self.part_list.append(temp_part)
            self.follow_list.append(temp_follow)
        for i in range (self.shiplength):
            if self.follow_list.count(self.part_list[i]) == 0:
                if self.part_list[i].third != "2":
                    
                    self.open_part.append (self.part_list[i])
        print (self.open_part)
        for i in range (len(self.open_part)):  
            if part == "tank" or part == "engine":
                part_class = Part(part)
                part_info = part_class, self.open_part[i]
                self.ship.append (part_info)
            elif part == "splitter":
                follow_num = len(self.ship) -1
                for j in range (0,3):
                    name = "split_"+str(j+1)
                    part_class = Splitter(name)
                    part_info = part_class,self.open_part[i]
                    self.ship.append(part_info)
                    follow = ship.ship[follow_num][0]
                    self.open_part.append(part_info)
            else:
                print ("part not regognized")
            self.open_part.append(self.ship[-1])
        
    def draw(self): #Gathers all ship parts and tells them to draw themsleves
        
        self.shiplength = (len(self.ship))

        for i in range (self.shiplength):   #Finding all ship parts
            temp_part_info = self.ship[i]
            temp_part = temp_part_info[0]
            temp_follow = temp_part_info[1]
            temp_part.draw(temp_follow)

    def update(self):
        self.x_list = []
        self.y_list = []
        for i in range (self.shiplength): #finds the furthest points of the ship
            temp_part_info = self.ship[i]
            temp_part = temp_part_info[0]
            self.x_list.append(temp_part.imagerect.left)
            self.x_list.append(temp_part.imagerect.right)
            self.y_list.append(temp_part.imagerect.top)
            self.y_list.append(temp_part.imagerect.bottom)
        pygame.display.update(min(self.x_list)-25,
            min(self.y_list)-25,(max(self.x_list)-min(self.x_list)+50),
            (max(self.y_list)-min(self.y_list)+50))

    def re_white(self): #blanks the area that the ship is in after every draw
        if self.first == True:
            self.x_list = [1]
            self.y_list = [1]
            print(self.first)
            self.first = False
        screen.fill(WHITE,(min(self.x_list),
            min(self.y_list),(max(self.x_list)-min(self.x_list)),
            (max(self.y_list)-min(self.y_list))))
        
        
class Capsule():    #Capsule class
    
    def __init__(self):
        self.image = pygame.image.load("MSP_capsule.png").convert()
        self.speed = [1,1]
        self.third = "0"
    def draw(self,x):
        self.x = x.x
        self.y = x.y
        
        imageafter = pygame.transform.rotate (self.image,angle)
        imageafter = pygame.transform.scale (imageafter,(scale,scale))
        
        self.imagerect = imageafter.get_rect()
        self.imagerect = self.imagerect.move(self.x,self.y)
        
        screen.blit(imageafter,self.imagerect)

    
class Center_of_mass(): #Center of mass, currently stagnent
    def __init__(self):
        self.x = 500
        self.y = 300
        
class Part(): #Class for a part attached to botom

    def __init__(self,part):
        if part == "tank":
            self.image = pygame.image.load("MSP_fuel.png")
        if part == "engine":
            self.image = pygame.image.load("MSP_engine.png")
        self.third = "0"
        
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

class Splitter():
    def __init__(self,part):
        self.third = part[-1]
        if part == "split_1":
            self.image = pygame.image.load("MSP_split_1.png")
        if part == "split_2":
            self.image = pygame.image.load("MSP_split_2.png")
        if part == "split_3":
            self.image = pygame.image.load("MSP_split_3.png")
        print(part, "initialized")
        print (self.third)
    def draw(self, follow):
        follow_x = follow.x
        follow_y = follow.y
             
        div_scale = scalemin/50 #changes scale for calculations

        a = follow_x + math.fabs(10*div_scale*math.sin(2*anglerad))+(25*div_scale) 
        d = follow_y + math.fabs(10*div_scale*math.sin(2*anglerad))+(25*div_scale)
        
        b_1 = math.sin(anglerad+(math.pi*7/4))*(35*div_scale)
        b_2 = math.sin(anglerad+(math.pi*1/4))*(35*div_scale)

        e_1 = math.cos(anglerad+(math.pi*7/4))*(35*div_scale)
        e_2 = math.cos(anglerad+(math.pi*1/4))*(35*div_scale)

        bottom_left_x= a+b_1
        bottom_right_x= a + b_2
        

        bottom_left_y= d+e_1
        bottom_right_y= d+e_2
        
        
        new_e_1 = math.cos(anglerad+(math.pi*1/4))*(35*div_scale)
        new_e_2 = math.cos(anglerad+(math.pi*7/4))*(35*div_scale)

        new_b_1 = math.sin(anglerad+(math.pi*1/4))*(35*div_scale)
        new_b_2 = math.sin(anglerad+(math.pi*7/4))*(35*div_scale)

        new_a_1= bottom_left_x + b_1
        new_a_2= bottom_left_x + new_b_1
        new_a_3= bottom_right_x + b_2

        new_d_1= bottom_left_y + e_1
        new_d_2= bottom_left_y + new_e_1
        new_d_3= bottom_right_y + e_2
        
        if self.third == "1":
            self.x = new_a_1 -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
            self.y = new_d_1 -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
        if self.third == "2":
            self.x = new_a_2 -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
            self.y = new_d_2 -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
        if self.third == "3":
            self.x = new_a_3 -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
            self.y = new_d_3 -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
        

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
            choice = input ("What peice would you like to add?(only have engine, splitter and tank rn)")
            ship.add (choice)
        elif choice == "no": done = True
        else: print("please say yes or no")
        
  
#Initial order of making stuff
capsule = Capsule()
center_of_mass = Center_of_mass()
ship = Ship()
ship_creation()

scale = int(scalemin*(math.fabs(0.4*math.sin(2*anglerad))+1)) 
screen.fill(WHITE)
ship.draw()

while True: #MAIN GAME LOOP
    
    #angle = angle +.05 #temp angle changing to test visuals
    
    anglerad = math.radians(angle)
    if angle == 360:
        angle = 0
    #changes the scale for rotating images 
    scale = int(scalemin*(math.fabs(0.4*math.sin(2*anglerad))+1))
    
    for event in pygame.event.get():    #im not completly sure what it does
        if event.type == pygame.QUIT: pygame.quit()#but i think it makes it easier to quit

        if event.type == pygame.MOUSEBUTTONDOWN: #scales the craft up and down with the 
            if event.button == 4:               #scoll wheel
                scalemin += 1
            if event.button == 5:
                scalemin -=1
        if event.type == pygame.KEYDOWN:
            print (event.key)
            if event.key == "a" and event.key == "d":
                pass
            elif event.key == 100:
                rotateleft = True
            elif event.key == 97:
                rotateright = True
        if event.type == pygame.KEYUP:
            if event.key == 100:
                rotateleft = False
            if event.key == 97:
                rotateright = False
    
    if rotateleft == True:
        angle -=.5
    if rotateright == True:
        angle += .5
    ship.re_white()#blanks area affected
    ship.draw()# draws and updates the ship
    ship.update()
    
    
    
    
    
    
