import pygame
import random
pygame.init()
#There should be Npcs that tell you what to do, so you have motivaitoin. There should be bosses and a storyline, and you can collect coins and hearts, because you can take damage. You will only have 
# one life, and if all your hearts go down, you lose.
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
StrawberryWidth = 45
StrawberryHeight = 45
Gravity = 1
Max_Platforms = 10
FPS = 60
clock = pygame.time.Clock()
scroll_thresh = 200
scroll = 0
bg_scroll = 0

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Strawberry climbing")

Bg_Image = pygame.image.load("pexels-photo-281260.jpg").convert_alpha()
Charecter = pygame.image.load("Strawberry (1).png").convert_alpha()
Small_platform = pygame.image.load("SMALL PLATFORM.png").convert_alpha()
Large_platform = pygame.image.load("LARGE PLATFORM.png").convert_alpha()

sky = Background(0, 0)


class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(Charecter, (60, 90))
        self.width = StrawberryWidth
        self.height = StrawberryHeight
        self.rect = pygame.Rect(45, 45, self.width, self.height)
        self.rect.center = (x, y)
        self.velocity_y = 0
        self.flip = False
    def move(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -=5
            self.flip = True
        if key[pygame.K_d]:
            dx +=5
            self.flip = False
        self.velocity_y += Gravity
        if self.rect.left + dx <0:
            dx = -self.rect.left

        if self.rect.right + dx >400:
            dx = SCREEN_WIDTH - self.rect.right
        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height()):
                if self.rect.bottom <platform.rect.centery:
                    if self.velocity_y>0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.velocity_y = -20
        if self.rect.bottom +dy > 600:
            dy = 0
            self.velocity_y = -20

        if self.rect.top <= SCROLL_THRESH:
            if self.vel_y < 0:
                scroll = -dy
                
        self.rect.x += dx
        self.rect.y += dy

        return scroll
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
        screen.blit(self.image, (self.rect.x-12, self.rect.y-5))
        
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(x, y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        self.rect.y += scroll
        if (self.rect.top > SCREEN_HEIGHT):
            self.kill()
Strawberry = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT - 150)
platform_group = pygame.sprite.Group()

for p in range(Max_Platforms):
    p_w = random.randint(40, 60)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = p * random.randint(80, 120)
    platform = Platform(p_x, p_y, P_w)
    platofrm_group.add(platform)

#class Background():
    #def __init__(self, x, y):
        #self.image = pygame.transform.scale(Bg_Image, (400, 600))
        #self.width = 400
        #self.height = 600
    #def drawbg(self):
        #screen.blit(self.image,(0,0))

run = True
while run:
    clock.tick(FPS)
    scroll = Strawberry.move()
    bg_scroll += scroll
    if (bg_scroll >= 600):
        bg_scroll = 0
    sky.drawbg(bg_scroll)
    
    pygame.draw.line(screen, WHITE, (0, scroll_thresh), (SCREEN_WIDTH, scroll-thresh)) 

    platform_group.update(scroll)

    platform_group.draw(screen)
    
    Strawberry.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()
