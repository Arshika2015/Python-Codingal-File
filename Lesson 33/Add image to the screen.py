import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Background Penguin Game")
background = pygame.transform.scale(pygame.image.load(r"/Users/mittu/Documents/Python Codingal File/Lesson 33/background.png").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
penguin = pygame.transform.scale(pygame.image.load(r"/Users/mittu/Documents/Python Codingal File/Lesson 33/penguin.png").convert_alpha(),(200,200))
penguin_rect = penguin.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2-30))
text = pygame.font.Font(None,36).render("Hello I am penguin",True,pygame.Color("black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))
def game_loop():
    clock = pygame.time.Clock()
    running  =True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(background,(0,0))
        screen.blit(penguin,penguin_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()

