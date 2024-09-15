import pygame
pygame.init()
pygame.display.set_caption("Rocket In Space 2")

#set the height and width of screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))

#define the player sprite
#player starts at (0,0) by default

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()

    #Move the spire based on keypressed events
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        #keep p layer on the screen
        if self.rect.left<0:
            self.rect.left = 0

        elif self.rect.right>screen_width:
            self.rect.right = screen_width
        
        if self.rect.top<=0:
            self.rect.top = 0
        elif self.rect.bottom >=screen_height:
            self.rect.bottom = screen_height

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect()

    #Move the spire based on keypressed events
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(5,0)

        #keep player on the screen
        if self.rect.left<0:
            self.rect.left = 0

        elif self.rect.right>screen_width:
            self.rect.right = screen_width
        
        if self.rect.top<=0:
            self.rect.top = 0
        elif self.rect.bottom >=screen_height:
            self.rect.bottom = screen_height

#end of the class
#make a group of all the spirtes
sprites = pygame.sprite.Group()

def startgame():
    player = Player()
    player2 = Player2()
    sprites.add(player)
    sprites.add(player2)

    #start the game loop
    while True:
        #look at every event
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                #if it is quit the game
                pygame.quit()
                exit(0)
        #get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        #add background image
        screen.blit(pygame.image.load("space.png"),(0,0))

        #draw the spirtes
        sprites.draw(screen)
        pygame.display.update()
    

startgame()

#        def update(self, pressed_keys):
#        if pressed_keys[pygame.K_w]:
#            self.rect.move_ip(0,-5)
#        if pressed_keys[pygame.K_s]:
#            self.rect.move_ip(0,5)
#        if pressed_keys[pygame.K_a]:
#            self.rect.move_ip(-5,0)
#        if pressed_keys[pygame.K_d]:
#            self.rect.move_ip(5,0)