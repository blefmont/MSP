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
        self.shiplength = 1
        self.part_list = []
        self.follow_list = []
        self.open_part = []
    def add_simple(self,part,follow):
        self.shiplength = len(self.ship)
        if part == "tank" or part == "engine":
            part_class = Part(part)
            self.ship.append((part_class,follow))
        elif part == "splitter":
            for i in range (0,3):
                name = "split_"+str(i+1)
                part_class = Splitter(name)
                self.ship.append((part_class,follow))
        elif part == "sideL" or part == "sideR":
            side = part[-1]
            part_class_1 = Side(side,1)
            self.ship.append((part_class_1,follow))
            part_class_2 = Side(side,2)
            self.ship.append((part_class_2,part_class_1))
        self.shiplength = len(self.ship)       
                
        
    def add (self, part):#function for adding parts to the ship
            

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
                self.shiplength += 1
            elif part == "splitter":
                follow_num = len(self.ship) -1
                for j in range (0,3):
                    name = "split_"+str(j+1)
                    part_class = Splitter(name)
                    part_info = part_class,self.open_part[i]
                    self.ship.append(part_info)
                    follow = ship.ship[follow_num][0]
                    self.open_part.append(part_info)
                    self.shiplength += 1
            else:
                print ("part not regognized")
            self.open_part.append(self.ship[-1])

    def delete(self, instance):
        
        print ("ship.delete")
        print (self.shiplength)
        temp_index_list = []
        self.follow_list.clear()
        print (self.follow_list)
        self.part_list.clear()
        for i in range (self.shiplength):
            self.follow_list.append(self.ship[i][1])
            self.part_list.append(self.ship[i][0])
        print (self.follow_list)
        print (self.part_list)
        temp_instance = instance
        
        to_delete_list = []
        
        while self.follow_list.count(temp_instance)!=0:
            
            print ("self.follow_list.count(temp_instance)",self.follow_list.count(temp_instance))
            to_delete_list.append(temp_instance)
            followed_index = self.follow_list.index(temp_instance)
            print ("followed_index",followed_index)
            temp_instance = self.ship[followed_index][0]
            print ("self.follow_list.count(temp_instance)",self.follow_list.count(temp_instance))
            print ("len(to_delete_list)",len(to_delete_list))
            print ("temp_instance",temp_instance)
        to_delete_list.append(temp_instance)
        print (to_delete_list)
        print (len(to_delete_list))
        for i in range (len(to_delete_list)):
            
            temp_index_list.append ( self.part_list.index(to_delete_list[i]))
            
        sorted (temp_index_list)
        print (temp_index_list)
        for i in range (1,(len(temp_index_list)+1)):
            print("delete ship")
            print (temp_index_list[-i])
            del self.ship[temp_index_list[-i]]
        
        to_delete_list.clear()
        self.shiplength = (len(self.ship))
        
    def draw(self): #Gathers all ship parts and tells them to draw themsleves
        

        for i in range (self.shiplength):   #Finding all ship parts
            temp_part_info = self.ship[i]
            temp_part = temp_part_info[0]
            temp_follow = temp_part_info[1]
            temp_part.draw(temp_follow)

    def update(self):
        self.x_list = []
        self.y_list = []
        for i in range (self.shiplength): #finds the furthest points of the ship
            temp_part = self.ship[i][0]
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
        self.mass = 100
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
            self.mass = 500
            self.third = "3"
        if part == "engine":
            self.image = pygame.image.load("MSP_engine.png")
            self.mass= 150
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

        #changing image sean was here
        imageafter = pygame.transform.rotate (self.image,angle)
        imageafter = pygame.transform.scale (imageafter,(scale,scale))

        self.imagerect = imageafter.get_rect()
        self.imagerect = self.imagerect.move(self.x,self.y)
        
        #blit the image
        screen.blit(imageafter,self.imagerect)

        

class Splitter():
    def __init__(self,part):
        self.mass = 50
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
             
        div_scale = scalemin/50 #changes scale for calculations and here too

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

        new_a_1= bottom_left_x + b_1
        new_a_2= bottom_left_x + b_2
        new_a_3= bottom_right_x + b_2

        new_d_1= bottom_left_y + e_1
        new_d_2= bottom_left_y + e_2
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
class Side():
    def __init__(self,side,part):
        self.side = side
        self.part = part
        if part == 1:
            self.image = pygame.image.load("MSP_split_2.png")
            self.third = 2
        if part == 2:
            if side == "L":
                self.image = pygame.image.load("MSP_split_1.png")
                self.third = 1
            if side == "R":
                self.image = pygame.image.load("MSP_split_3.png")
                self.third = 2
    def draw(self,follow):
        follow_x = follow.x
        follow_y = follow.y

        div_scale = scalemin/50

        a = follow_x + math.fabs(10*div_scale*math.sin(2*anglerad))+(25*div_scale) 
        d = follow_y + math.fabs(10*div_scale*math.sin(2*anglerad))+(25*div_scale)

        if self.side == "L":
            b_1 = math.sin(anglerad+(math.pi*7/4))*(35*div_scale)
            e_1 = math.cos(anglerad+(math.pi*7/4))*(35*div_scale)
            
            bottom_left_x = a+ b_1
            bottom_left_y = d+ e_1
            new_e = math.cos(anglerad+(math.pi*5/4))*(35*div_scale)
            new_b = math.sin(anglerad+(math.pi*5/4))*(35*div_scale)

            new_a = bottom_left_x + new_b
            new_d = bottom_left_y + new_e

        elif self.side == "R":
            b_2 = math.sin(anglerad+(math.pi*1/4))*(35*div_scale)
            e_2 = math.cos(anglerad+(math.pi*1/4))*(35*div_scale)
        
            bottom_right_x= a + b_2
            bottom_right_y= d+e_2
            
            new_e = math.cos(anglerad+(math.pi*3/4))*(35*div_scale)
            new_b = math.sin(anglerad+(math.pi*3/4))*(35*div_scale)

            new_a = bottom_right_x + new_b
            new_d = bottom_right_y + new_e
            
        
            
        self.x = new_a -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)
        self.y = new_d -math.fabs(10*div_scale*math.sin(2*anglerad)) -(25*div_scale)  

        #changing image
        imageafter = pygame.transform.rotate (self.image,angle)
        imageafter = pygame.transform.scale (imageafter,(scale,scale))

        self.imagerect = imageafter.get_rect()
        self.imagerect = self.imagerect.move(self.x,self.y)
        
        #blit the image
        screen.blit(imageafter,self.imagerect)
        

class Start():
    def __init__(self):
        
        self.tank = pygame.image.load("MSP_fuel.png")
        self.engine =  pygame.image.load("MSP_engine.png")
        self.split_1 = pygame.image.load("MSP_split_1.png")
        self.split_2 = pygame.image.load("MSP_split_2.png")
        self.split_3 = pygame.image.load("MSP_split_3.png")
        self.side_L1 = pygame.image.load("MSP_split_2.png")
        self.side_L2 = pygame.image.load("MSP_split_3.png")
        self.side_R1 = pygame.image.load("MSP_split_2.png")
        self.side_R2 = pygame.image.load("MSP_split_1.png")
        self.symmetry_img = pygame.image.load("MSP_symmetry.png")
        self.start_img = pygame.image.load("MSP_start.png")
        
        self.tank_rect = self.tank.get_rect()
        self.engine_rect = self.engine.get_rect()
        self.split_1_rect = self.split_1.get_rect()
        self.split_2_rect = self.split_2.get_rect()
        self.split_3_rect = self.split_3.get_rect()
        self.side_L1_rect = self.side_L1.get_rect()
        self.side_L2_rect = self.side_L2.get_rect()
        self.side_R1_rect = self.side_R1.get_rect()
        self.side_R2_rect = self.side_R2.get_rect()
        self.symmetry_img_rect = self.symmetry_img.get_rect()
        self.start_img_rect = self.start_img.get_rect()

        self.symmetry_img_rect = self.symmetry_img_rect.move(50,25)
        self.tank_rect = self.tank_rect.move(75,100)
        self.engine_rect = self.engine_rect.move(75,175)
        self.split_1_rect = self.split_1_rect.move(25,250)
        self.split_2_rect = self.split_2_rect.move(75,250)
        self.split_3_rect = self.split_3_rect.move(125,250)
        self.side_L1_rect = self.side_L1_rect.move(75,325)
        self.side_L2_rect = self.side_L2_rect.move(125,325)
        self.side_R1_rect = self.side_R1_rect.move(75,400)
        self.side_R2_rect = self.side_R2_rect.move(25,400)
        self.start_img_rect = self.start_img_rect.move(50,475)

        self.picked_list = ["tank","engine", "splitter","splitter","splitter","sideR","sideR","sideL","sideL","symmetry","start"]
    def draw(self):

        screen.blit(self.symmetry_img,self.symmetry_img_rect)
        screen.blit(self.tank,self.tank_rect)
        screen.blit(self.engine,self.engine_rect)
        screen.blit(self.split_1,self.split_1_rect)
        screen.blit(self.split_2,self.split_2_rect)
        screen.blit(self.split_3,self.split_3_rect)
        screen.blit(self.side_L1,self.side_L1_rect)
        screen.blit(self.side_L2,self.side_L2_rect)
        screen.blit(self.side_R1,self.side_R1_rect)
        screen.blit(self.side_R2,self.side_R2_rect)
        screen.blit(self.start_img,self.start_img_rect)
        pygame.display.update(0,0,200,550)
    def rects(self):
        self.rect_list = []
        self.rect_list.append(self.tank_rect)
        self.rect_list.append(self.engine_rect)
        self.rect_list.append(self.split_1_rect)
        self.rect_list.append(self.split_2_rect)
        self.rect_list.append(self.split_3_rect)
        self.rect_list.append(self.side_L1_rect)
        self.rect_list.append(self.side_L2_rect)
        self.rect_list.append(self.side_R1_rect)
        self.rect_list.append(self.side_R2_rect)
        self.rect_list.append(self.symmetry_img_rect)
        self.rect_list.append(self.start_img_rect)
        

def ship_creation(WHITE): # Building the image
    done = False
    pygame.display.flip()
    symmetry = True
    
    while done == False:
        ship.re_white()#blanks area affected
        ship.draw()# draws and updates the ship
        ship.update()
        start.draw()
        start.rects()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: #scales the craft up and down with the 
                if event.button == 1:
                    collide,rect_list = test_mouse_collision()
                    try:
                        clicked_on = rect_list[collide]
                   
                        if collide >= len(rect_list)-11:
                            if collide== len(rect_list)-2:
                                print("symmetry")
                                symmetry = not symmetry
                            elif collide== len(rect_list)-1:
                                print("start")
                                done = True
                    
                            else:
                                print ("new part")
                                picked = start.picked_list[collide-(len(rect_list)-11)]
                                if symmetry == True:
                                    ship.add(picked)
                                
                        else:
                            if symmetry == False:
                                follow = ship.ship[collide][0]
                                ship.add_simple (picked,follow)
                            else:
                                print ("existing part")
                    except IndexError: pass
    screen.fill(WHITE)                  
    pygame.display.flip()
    
                        
                    
                   

def rotate(left,right,angle):
    if left == True:
        angle -=.5
    if right == True:
        angle += .5
    return (angle)

def test_mouse_collision():
    mouse_rect = pygame.Rect(pygame.mouse.get_pos(),(1,1))
    rect_list = []
    for i in range (len(ship.ship)):
        rect_list.append((ship.ship[i][0]).imagerect)
    try:    
        for i in range (len(start.rect_list)):
            rect_list.append((start.rect_list[i]))
    except NameError: pass

    try: collide_index = mouse_rect.collidelistall(rect_list)[-1]
    except IndexError: collide_index = len(rect_list)+1
    return (collide_index,rect_list)

def find_if_engine(collide):
        #try:
            print (type(ship.ship[collide][0]))
            if str(type(ship.ship[collide][0])) == "<class '__main__.Part'>" and ship.ship[collide][0].third == "0":
                print ("its an engine!")
                ship.delete(ship.ship[collide][0])
            
            
         #print("not an engine")
        
    
  
#Initial order of making stuff
scale = int(scalemin*(math.fabs(0.4*math.sin(2*anglerad))+1)) 
capsule = Capsule()
center_of_mass = Center_of_mass()
ship = Ship()
screen.fill(WHITE)
ship.draw()
start = Start()

ship_creation(WHITE)
del start

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
            if event.button == 1:
                local_collide, local_list = test_mouse_collision()

                find_if_engine(local_collide)
                
                
        if event.type == pygame.KEYDOWN:
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
    angle = rotate(rotateleft,rotateright,angle)
    ship.re_white()#blanks area affected
    ship.draw()# draws and updates the ship
    ship.update()
    
    
    
    
    
    
