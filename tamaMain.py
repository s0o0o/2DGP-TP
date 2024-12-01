# main.py
import pygame
from pygame import *
import os
import sys
from scene import scene_tick, draw_start_scene, draw_first_scene, scene_speeds, draw_second_scene  # scene.py에서 함수 가져오기

# 초기화 및 기본 설정
pygame.init()
screen_width, screen_height = 1000, 600
target_width, target_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("HELLO MY TAMAGOCHI")
clock = pygame.time.Clock()
original_surface = pygame.Surface((screen_width, screen_height))

frame_counter = 0
update_interval = 1  # 3

os.environ['SDL_VIDEO_CENTERED'] = '1'

# 색상, 텍스트 및 글꼴 설정
WHITE = (255, 255, 255)
font = pygame.font.Font('NeoDunggeunmoPro-Regular.ttf', 25)
fontSmall = pygame.font.Font('NeoDunggeunmoPro-Regular.ttf', 22)
text1 = "당신의 다마고치를 선택해주세요!"
text_displayed = ""
index = 0
text_color = (0, 0, 0)

# 상태 변수
running = True
shrinking = False
startScene = True
firstScene = False
first_context = False
smallSize =0.97
shrink_speed = 10

selectEggNum = 99
secondScene = False

# 배경 및 버튼 이미지 불러오기
backGround = pygame.image.load('배경1.png')
backGround2 = pygame.image.load('배경3.png')
backGround3 = pygame.image.load('배경4.png')
backGround4 = pygame.image.load('배경5.png')
backG_1 = pygame.image.load('도트배경.png')
button1image = pygame.transform.scale(pygame.image.load('시작버튼.png'), (293 / 1.5, 91 / 1.5))
button1Loc = button1image.get_rect(center=(screen_width // 2, 450))
button2image = pygame.transform.scale(pygame.image.load('게임종료.png'), (293 / 1.5, 91 / 1.5))
button2Loc = button2image.get_rect(center=(screen_width // 2, 500))
titleImage = pygame.transform.scale(pygame.image.load('제목.png'), (450, 300))
titleLoc = titleImage.get_rect(center=(screen_width // 2, 150))

# 첫 번째 장면의 선택 이미지 및 알 이미지 불러오기
firstChoice1 = pygame.transform.scale(pygame.image.load('1.png'), (598 / smallSize, 736 / smallSize))
firstChoice1Loc = firstChoice1.get_rect(center=(target_width // 2, 300))
firstChoice2 = pygame.transform.scale(pygame.image.load('3.png'), (598 / smallSize, 736 / smallSize))
firstChoice2Loc = firstChoice2.get_rect(center=(target_width // 2, 300))

egg_imgs = ["알1.png","알2.png","알3.png"]

egg1 = pygame.image.load('알1.png')
egg1Loc = egg1.get_rect(center=(target_width // 2 - 150, 300))
egg2 = pygame.image.load('알2.png')
egg2Loc = egg2.get_rect(center=(target_width // 2, 300))
egg3 = pygame.image.load('알3.png')
egg3Loc = egg3.get_rect(center=(target_width // 2 + 150, 300))
selecFinalEggLoc = egg2.get_rect(center=(target_width // 2, 400))

changeEffect = image.load('페이드인아웃.png')
changeEffect2 = image.load('페이드아웃.png')
changeEffectCurFrame = 0
changeEffectCurFrame2 = 0
changeEffectFrame = 13
changeEffectLoc = changeEffect.get_rect(center=(target_width // 2, 0))
selecEgg = False
 # 검은색 페이드
isFade = False

# 두번째 씬 (알 깨지고..~ 아기 태어나는 부분)
room_BGimg = pygame.transform.smoothscale(pygame.image.load("배경방1.png"), (313, 313))
eggBrake = False
isTextAni1 = False

afterEggBrake_text = ["짠!!","당신의 다마고치가 태어났습니다!", "열심히 잘 키워보도록 하세요!"]
isEggBrake_text = [False,False,False]
breakegg_text_displayed = ""
eggBrakeindex = 0
EggBrakeTextNum = 0

buttonEat = image.load('밥주기버튼.png')
buttonEatLoc = buttonEat.get_rect(center=(110,60))
buttonPlay = image.load('놀아주기버튼.png')
buttonPlayLoc = buttonEat.get_rect(center=(450,60))

# 성장별 모습
baby_growth_imgs= ["아기1_idle.png", "아기2_idle.png"]
frist_growth_imgs=["반항기_여1.png","반항기_여2.png","반항기_남1.png","반항기_남2.png"]
second_growth_imgs=["사춘기_여1.png","사춘기_남1.png"]
final_growth_imgs=["성인_여1.png","성인_여2.png","성인_여3.png",
                       "성인_남1.png","성인_남2.png","성인_남3.png"]


# 대사들..
dialog1 = pygame.image.load('알깨주세요.png')
dialog1Loc = dialog1.get_rect(center=(target_width // 2, 470))
checkdig1 = True

def set_frame_rate(speed):
    scene_tick(clock, speed)

def fadeIn():
    global changeEffectCurFrame, isFade
    x = changeEffectCurFrame * 600
    rect = pygame.Rect(x, 0, 600, 600)
    screen.blit(changeEffect, (0, 0), rect)
    if changeEffectCurFrame < 12:
        changeEffectCurFrame = (changeEffectCurFrame + 1)
    if changeEffectCurFrame == 12:
        isFade = True


def fadeOut():
    global changeEffectCurFrame2,isFade
    x = changeEffectCurFrame2 * 600
    rect = pygame.Rect(x, 0, 600, 600)
    screen.blit(changeEffect2, (0, 0), rect)

    if changeEffectCurFrame2 < 12:
        changeEffectCurFrame2 = (changeEffectCurFrame2 + 1)
    if changeEffectCurFrame == 12:
        isFade = True


def reStart():
    pass



# 애니메이션 루프
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if button1Loc.collidepoint(event.pos):
                shrinking = True
                startScene = False
                firstScene = True
            elif button2Loc.collidepoint(event.pos):
                running = False
            elif firstScene and egg1Loc.collidepoint(event.pos):
                selectEggNum = 1
                selecEgg = True
            elif firstScene and egg2Loc.collidepoint(event.pos):
                selectEggNum = 2
                selecEgg = True
            elif firstScene and egg3Loc.collidepoint(event.pos):
                selectEggNum = 3
                selecEgg = True
            elif secondScene and selecFinalEggLoc.collidepoint(event.pos):
                eggBrake = True
                isTextAni1 = True
                checkdig1 = False
            elif secondScene and buttonEatLoc.collidepoint(event.pos):
                print("밥주기")
                pass
            elif secondScene and buttonPlayLoc.collidepoint(event.pos):
                print("놀아주기")
                pass




    original_surface.blit(backGround, (0, 0))
    original_surface.blit(button1image, button1Loc)
    original_surface.blit(button2image, button2Loc)
    original_surface.blit(titleImage, titleLoc)
    # 화면 크기 애니메이션 줄이는
    if shrinking:
        frame_counter += 1
        if frame_counter % update_interval == 0:
            screen_width = max(target_width, screen_width - shrink_speed)
            screen_height = max(target_height, screen_height - shrink_speed)
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE | pygame.DOUBLEBUF)
            frame_counter = 0  # 카운터 초기화
        if screen_width == target_width and screen_height == target_height:
            shrinking = False
            first_context = True
            scene_speeds["firstScene"] = 15
            set_frame_rate("firstScene")


    # 화면 그리기
    screen.fill(WHITE)
    if startScene:
        draw_start_scene(screen, firstChoice2Loc, firstChoice2, backGround, button1image, button1Loc, button2image, button2Loc, titleImage, titleLoc)
        scene_tick(clock, "startScene")




    elif firstScene:
        if first_context and index < len(text1):
            text_displayed += text1[index]
            index += 1
        draw_first_scene(screen, backG_1, firstChoice1, firstChoice1Loc, firstChoice2, firstChoice2Loc, egg1, egg1Loc, egg2, egg2Loc, egg3, egg3Loc, text_displayed, font, text_color)
        scene_tick(clock, "firstScene")

        if (selecEgg):
            fadeIn()
            if(isFade):
                firstScene = False
                secondScene = True
                isFade = False
            clock.tick(1000)
            pass

    elif secondScene :
        #print(selectEggNum)

        draw_second_scene(screen, firstChoice2, firstChoice2Loc, selectEggNum, egg1, egg2, egg3,
                          selecFinalEggLoc, room_BGimg, baby_growth_imgs, eggBrake, text_displayed, fontSmall
                          ,breakegg_text_displayed,buttonEat,buttonPlay,buttonEatLoc,buttonPlayLoc,backGround3
                          ,dialog1,dialog1Loc,checkdig1)
        fadeOut()
        if (isFade):
            isFade = False
            scene_speeds["secondScene"] = 10

        if eggBrake == True:
            if isTextAni1 == True:
                if eggBrakeindex < len(afterEggBrake_text[EggBrakeTextNum]) and EggBrakeTextNum < 3:
                    #print("hello")
                    breakegg_text_displayed += afterEggBrake_text[EggBrakeTextNum][eggBrakeindex]
                    eggBrakeindex += 1
                    if eggBrakeindex >= len(afterEggBrake_text[EggBrakeTextNum])and EggBrakeTextNum < 2:
                        breakegg_text_displayed = ""
                        EggBrakeTextNum += 1
                        eggBrakeindex = 0

                if EggBrakeTextNum >= 3:
                    isTextAni1 = False

            if isTextAni1 == False:
                EggBrakeTextNum = 2
                eggBrakeindex= 18










        #print('selectEggNum =' , selectEggNum)
        scene_tick(clock, "secondScene")
        pass




    pygame.display.flip()

pygame.quit()
sys.exit()