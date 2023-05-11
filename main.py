import pygame
from pygame.locals import *

pygame.init()


size = width, height = 800, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ball_pos = [width // 2, height // 2]  
ball_vel = [5, 5]  
paddle_width = 10
paddle_height = 60
paddle_vel = 5  
paddle1_pos = paddle2_pos = height // 2 - paddle_height // 2  
score1 = score2 = 0  
font = pygame.font.Font(None, 36)


running = True
clock = pygame.time.Clock()

def reset_ball():
    global ball_pos, ball_vel
    ball_pos = [width // 2, height // 2]
    ball_vel = [5, 5]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == KEYDOWN:
            if event.key == K_w:
                paddle1_pos -= paddle_vel
            elif event.key == K_s:
                paddle1_pos += paddle_vel
            elif event.key == K_UP:
                paddle2_pos -= paddle_vel
            elif event.key == K_DOWN:
                paddle2_pos += paddle_vel

    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    
    if ball_pos[1] <= 0 or ball_pos[1] >= height - 20:
        ball_vel[1] = -ball_vel[1]

    
    if (
        ball_pos[0] <= paddle_width
        and paddle1_pos <= ball_pos[1] <= paddle1_pos + paddle_height
    ) or (
        ball_pos[0] >= width - paddle_width - 20
        and paddle2_pos <= ball_pos[1] <= paddle2_pos + paddle_height
    ):
        ball_vel[0] = -ball_vel[0]

   
    if ball_pos[0] <= 0:
        score2 += 1
        reset_ball()
    elif ball_pos[0] >= width - 20:
        score1 += 1
        reset_ball()

    
    screen.fill(BLACK)

    
    pygame.draw.rect(screen, WHITE, (0, paddle1_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen,WHITE,(width - paddle_width, paddle2_pos, paddle_width, paddle_height),)
    pygame.draw.circle(screen, WHITE, ball_pos, 10)

  
    score_text = font.render(
        str(score1) + " : " + str(score2), True, WHITE
    )
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

   
    pygame.display.flip()

    
    clock.tick(60)

