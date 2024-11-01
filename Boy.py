import pygame
import sys

# 화면 설정
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("HELLO MY TAMAGOCHI")

# 색상 정의
WHITE = (255, 255, 255)

running = True
clock = pygame.time.Clock()

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 그리기
    screen.fill(WHITE)

    pygame.display.flip()  # 화면 업데이트
    clock.tick(60)  # 60 프레임 설정

pygame.quit()
sys.exit()
