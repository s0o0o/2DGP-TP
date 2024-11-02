import pygame
from pico2d import load_image, get_events
from pygame import *
import random

import sys
import os

from pygame.examples.cursors import image_name

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

#폰트
font = font.Font('NeoDunggeunmoPro-Regular.ttf', 25)
text = "당신의 다마고치를 선택해주세요!"
text_color = (0,0,0)  # 글자 색상
text_displayed = ""  # 표시할 부분 문자열
index = 0  # 현재 글자 위치

# 각 씬들 출력될지말지
startScene = True
firstScene = False
first_context=False
smallSize = 1.3

#  게임 시작/종료 버튼 위치+ 크기
backGround = image.load('배경1.png')
backG_1 = image.load('도트배경.png')


button1image = image.load('시작버튼.png')
button1image = pygame.transform.scale(button1image, (293 / 1.5, 91 / 1.5))
button1Loc = button1image.get_rect(center=(screen_width // 2, 450))

button2image = image.load('게임종료.png')
button2image = pygame.transform.scale(button2image, (293 / 1.5, 91 / 1.5))
button2Loc = button2image.get_rect(center=(screen_width // 2, 500))

titleImage = image.load('제목.png')
titleImage = pygame.transform.scale(titleImage, (450, 300))
titleLoc = titleImage.get_rect(center=(screen_width // 2, 150))

firstChoice1 = pygame.image.load('1.png')
firstChoice1 = pygame.transform.scale(firstChoice1, (598 / smallSize, 736 / smallSize))
firstChoice1Loc = firstChoice1.get_rect(center=((target_width // 2), 300))
firstChoice2 = pygame.image.load('2.png')
firstChoice2 = pygame.transform.scale(firstChoice2, (598 / smallSize, 736 / smallSize))
firstChoice2Loc = firstChoice2.get_rect(center=((target_width // 2), 300))

# 그 처음 선택할 때 위치들.+사진 로드

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1Loc.collidepoint(event.pos):
                shrinking = True  # 클릭 시 축소 시작
                startScene = False
                firstScene = True

            if button2Loc.collidepoint(event.pos):
                running = False

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
            first_context = True


    # 화면 그리기
    screen.fill(WHITE)
    if(startScene):
        screen.blit(backGround,(0,0))
        screen.blit(button1image, button1Loc)
        screen.blit(button2image, button2Loc)
        screen.blit(titleImage, titleLoc)
    if(firstScene):
        screen.blit(backG_1, (0, 0))
        screen.blit(firstChoice1, firstChoice1Loc)
        screen.blit(firstChoice2, firstChoice2Loc)

            # 텍스트 렌더링 및 그리기
        if first_context:
            if index < len(text):
                text_displayed += text[index]
                index += 1
            rendered_text = font.render(text_displayed, True, text_color)
            text_rect = rendered_text.get_rect(center=(screen_width // 2, 200 ))
            screen.blit(rendered_text, text_rect)


    pygame.display.flip()
    clock.tick(60)


quit()
sys.exit()
