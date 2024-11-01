import pygame
from pico2d import load_image, get_events
from pygame import *

import sys
import os

# 초기 설정
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'  # 화면을 초기 중심에 위치시킴

# 초기 화면 크기 설정
screen_width, screen_height = 1000, 600
target_width, target_height = 600, 600  # 최종 목표 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("HELLO MY TAMAGOCHI")

WHITE = (255, 255, 255)
clock = pygame.time.Clock()
running = True
shrinking = False  # 화면 사이즈 바뀌는거
shrink_speed = 10  # 줄어드는 속도

#  게임 시작/종료 버튼 위치+ 크기
button1image = image.load('시작버튼.png')
button2image = image.load('게임종료.png')
button1Loc = button1image.get_rect(center=(screen_width // 2, screen_height // 2))
button2Loc = button2image.get_rect(center=(screen_width // 2, screen_height // 2))


smallSize = 1.8

firstChoice1 = pygame.image.load('1.png')
firstChoice1 = pygame.transform.scale(firstChoice1, (598/smallSize, 736/smallSize))
firstChoice1Loc = firstChoice1.get_rect(center=(250,300))
firstChoice2 = pygame.image.load('2.png')
firstChoice2 = pygame.transform.scale(firstChoice2, (598/smallSize, 736/smallSize))
firstChoice2Loc = firstChoice2.get_rect(center=(750,300))
# 그 처음 선택할 때 위치들.+사진 로드

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if firstChoice1Loc.collidepoint(event.pos):
                shrinking = True  # 클릭 시 축소 시작
            elif firstChoice2Loc.collidepoint(event.pos):
                shrinking = True  # 클릭 시 축소 시작

    # 화면사이즈 애니메이션 로직
    if shrinking:
        # 화면 크기 조정
        screen_width = max(target_width, screen_width - shrink_speed)
        screen_height = max(target_height, screen_height - shrink_speed)

        # 창을 중앙에 맞추기 위해 새로운 위치 계산
        new_x = (1000 - screen_width) // 2
        new_y = (600 - screen_height) // 2
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{new_x},{new_y}"

        # 새 크기로 화면 설정
        screen = pygame.display.set_mode((screen_width, screen_height))

        # 목표 크기에 도달 시 애니메이션 종료
        if screen_width == target_width and screen_height == target_height:
            shrinking = False

    # 화면 그리기
    screen.fill(WHITE)
    screen.blit(firstChoice1, firstChoice1Loc)
    screen.blit(firstChoice2, firstChoice2Loc)
    pygame.display.flip()
    clock.tick(60)


quit()
sys.exit()