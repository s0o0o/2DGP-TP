# scene.py
import pygame
from pygame import *

# 각 장면별 고유 속도 설정
scene_speeds = {
    "startScene": 100,
    "firstScene": 50000,
    "secondScene" : 13
}

babyIdleFrame = 6
frame = 0

# 각 장면의 프레임 속도 조절 함수
def scene_tick(clock, scene_name):
    """현재 장면에 맞는 프레임 속도로 tick을 조절"""
    speed = scene_speeds.get(scene_name, 60)  # 기본값 60 프레임
    clock.tick(speed)


# 장면별 화면 그리기 함수
def draw_start_scene(screen, firstChoice2Loc, firstChoice2, backGround, button1image, button1Loc, button2image, button2Loc, titleImage, titleLoc):
    screen.blit(backGround, (0, 0))
    screen.blit(button1image, button1Loc)
    screen.blit(button2image, button2Loc)

    screen.blit(titleImage, titleLoc)


# 이거 알 선택 후
def draw_first_scene(screen, backG_1, firstChoice1, firstChoice1Loc, firstChoice2, firstChoice2Loc, egg1, egg1Loc, egg2,
                     egg2Loc, egg3, egg3Loc, text_displayed, font, text_color):
    screen.blit(backG_1, (0, 0))
    #screen.blit(firstChoice1, firstChoice1Loc)

    screen.blit(egg1, egg1Loc)
    screen.blit(egg2, egg2Loc)
    screen.blit(egg3, egg3Loc)

    # 텍스트 렌더링 및 그리기
    rendered_text = font.render(text_displayed, True, text_color)
    text_rect = rendered_text.get_rect(center=(screen.get_width() // 2, 200))
    screen.blit(rendered_text, text_rect)

# 이건 알선택후  -> 첫 화면..넘어가서.. 부터
def draw_second_scene(screen,firstChoice2, firstChoice2Loc,selectEggNum,egg1,egg2,egg3,
                      selecFinalEggLoc,room_BGimg,baby_growth_imgs):
    global character, frame
    screen.blit(room_BGimg, (145, 175))
    screen.blit(firstChoice2, firstChoice2Loc)

    if selectEggNum == 1:
        screen.blit(egg1, selecFinalEggLoc)

        baby_idle = image.load("아기1_idle.png")
        pass
    elif selectEggNum == 2:
        screen.blit(egg2, selecFinalEggLoc)

        baby_idle = image.load("아기1_idle.png")
        pass
    elif selectEggNum == 3:
        screen.blit(egg3, selecFinalEggLoc)

        baby_idle = image.load("아기2_idle.png")
        pass


    character_image =  transform.scale(baby_idle, (204*2, 54*2))
    frame_width = 34*2
    frame_height = 54*2
    frame_x = frame * frame_width  # 프레임의 x 좌표 계산
    frame_y = 0
    character_frame = character_image.subsurface((frame_x, frame_y, frame_width, frame_height))
    screen.blit(character_frame, (270, 350))

    frame = (frame + 1) % babyIdleFrame