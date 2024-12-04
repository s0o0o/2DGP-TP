# main.py
import pygame
from pygame import *

#import pico2d
from pico2d import load_image
import os
import sys

from sdl2 import SDL_KEYDOWN, SDLK_a, SDLK_d, SDLK_w, SDLK_s

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
smallSize = 1.1
shrink_speed = 10

selectEggNum = 99
secondScene = False

# 배경 및 버튼 이미지 불러오기
backGround = pygame.image.load('배경1.png')
morningTime = pygame.image.load('아침배경.png')
eveningTime = pygame.image.load('저녁배경.png')
nightTime = pygame.image.load('밤배경.png')
presentTime = morningTime

timeCount = 0

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
mainRoom_back = pygame.transform.smoothscale(pygame.image.load("배경방1.png"), (313, 313))
restRoom_back = pygame.transform.smoothscale(pygame.image.load('화장실.png'), (313, 313))

nowRoom = mainRoom_back

eggBrake = False
isTextAni1 = False

showEggBrakeDia = True
afterEggBrake_text = [" 짠!!  ","  당신의 다마고치가 태어났습니다!!  ", "   열심히 잘 키워보도록 하세요!!!!     "]
breakegg_text_displayed = ""
eggBrakeindex = 0
EggBrakeTextNum = 0
isShowTextAni = True

buttonEat = image.load('밥주기버튼.png')
buttonEatLoc = buttonEat.get_rect(center=(target_width//2 - 70,80))
buttonPlay = image.load('놀아주기버튼.png')
buttonPlayLoc = buttonEat.get_rect(center=(target_width//2 + 70,80))

# 성장별 모습
baby_growth_imgs_idle= ["아기1_idle.png", "아기2_idle.png"]
frist_growth_imgs=["반항기_여1_idle.png","반항기_여2_idle.png","반항기_남1_idle.png","반항기_남2_idle.png"]
second_growth_imgs=["사춘기_여1.png","사춘기_남1.png"]
final_growth_imgs=["성인_여1.png","성인_여2.png","성인_여3.png",
                       "성인_남1.png","성인_남2.png","성인_남3.png"]


# 대사들..
dialog1 = pygame.image.load('알깨주세요.png')
dialog1Loc = dialog1.get_rect(center=(target_width // 2, 470))
checkdig1 = True


#여러 이미지들...
ddong =pygame.image.load('똥.png')
ddongImo = pygame.image.load('똥이모지.png')
loveImo = pygame.image.load('하트이모지.png')
sleepImo = pygame.image.load('잠이모지.png')
sleepButton = pygame.image.load('잠자기버튼.png')
sofa = pygame.image.load('소파.png')
arrowleft = pygame.image.load('화살표1.png')
arrowleftLoc = arrowleft.get_rect(center=(target_width//2 - 200,350))
arrowright = pygame.image.load('화살표2.png')
arrowrightLoc = arrowright.get_rect(center=(target_width//2 + 200,350))
showImos = None
isImo = False
imoCount = 0

staminaImg = pygame.image.load('체력바_스테미너.png')
staminaImgX = 0

hpImg = pygame.image.load('체력바_체력.png')
hpImgX = 0

interestingImg = pygame.image.load('체력바_흥미.png')
interestingImgX = 0

dayImg = pygame.image.load('날짜디데이.png')
dayImgX = 0

cha_x = 270
cha_y = 350
cha_speed = 3

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

def update():

    pass

def event_machine():
    global running, shrinking, startScene, \
        secondScene,firstScene, selectEggNum, selecEgg,eggBrake, isTextAni1,checkdig1,\
        showImos, cha_x,cha_y,isImo,imoCount,nowRoom,staminaImgX,interestingImgX,hpImgX

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1Loc.collidepoint(event.pos):
                shrinking = True
                startScene = False
                firstScene = True
            elif button2Loc.collidepoint(event.pos):
                running = False

            if firstScene:
                if egg1Loc.collidepoint(event.pos):
                    selectEggNum = 1
                    selecEgg = True
                elif egg2Loc.collidepoint(event.pos):
                    selectEggNum = 2
                    selecEgg = True
                elif  egg3Loc.collidepoint(event.pos):
                    selectEggNum = 3
                    selecEgg = True

            if secondScene:

                if selecFinalEggLoc.collidepoint(event.pos):
                    eggBrake = True
                    isTextAni1 = True
                    checkdig1 = False
                elif buttonEatLoc.collidepoint(event.pos):
                    imoCount=0
                    print("밥주기")
                    showImos = pygame.transform.smoothscale(loveImo, (30,30))

                    if(staminaImgX>0 and staminaImgX < 500):
                        staminaImgX -= 100
                        isImo = True
                    elif(staminaImgX== 0):
                        print('배불러.. 스트레스!')

                    pass
                elif buttonPlayLoc.collidepoint(event.pos):
                    imoCount=0
                    print("놀아주기")
                    showImos = pygame.transform.smoothscale(loveImo, (30, 30))


                    if(staminaImgX<500):
                        staminaImgX += 100
                        isImo = True
                        if (interestingImgX > 0 and interestingImgX < 500):
                            interestingImgX -= 100
                        elif(interestingImgX == 0):
                            print('더 안놀거임..스트레스!')


                    pass
                elif arrowrightLoc.collidepoint(event.pos):
                    if(nowRoom == mainRoom_back):
                        nowRoom = restRoom_back
                    elif(nowRoom == restRoom_back):
                        nowRoom = mainRoom_back
                    print('오른쪽')
                elif arrowleftLoc.collidepoint(event.pos):
                    if (nowRoom == mainRoom_back):
                        nowRoom = restRoom_back
                    elif (nowRoom == restRoom_back):
                        nowRoom = mainRoom_back
                    print('왼쪽')

        if event.type == SDL_KEYDOWN:
            if secondScene:
                if event.key == SDLK_a:
                    print('a')
                    cha_x -= cha_speed
                if event.key == SDLK_d:
                    print('d')
                    cha_x += cha_speed
                if event.key == SDLK_w:
                    print('w')
                    # cha_y += cha_speed
                if event.key == SDLK_s:
                    print('s')


# 애니메이션 루프
while running:

    print(timeCount)
    event_machine()

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
                          selecFinalEggLoc, mainRoom_back, restRoom_back,nowRoom, baby_growth_imgs_idle, eggBrake, text_displayed, fontSmall
                          ,breakegg_text_displayed,buttonEat,buttonPlay,buttonEatLoc,buttonPlayLoc,morningTime,eveningTime,nightTime
                          ,dialog1,dialog1Loc,checkdig1,cha_x,cha_y,isImo, showImos, imoCount,presentTime
                          ,arrowleft,arrowleftLoc,arrowright,arrowrightLoc,staminaImg,staminaImgX
                          ,isTextAni1,isShowTextAni,hpImgX,interestingImgX,interestingImg,hpImg,dayImg,dayImgX)
        timeCount += 1
        if (timeCount>0 and timeCount < 100):
            presentTime = morningTime
        elif(timeCount >= 100 and timeCount <250) :
            presentTime = eveningTime
        elif(timeCount >250 and timeCount < 350) :
            presentTime = nightTime
        elif(timeCount>350):
            presentTime = morningTime
            timeCount = 0

            if(dayImgX<=702-78):
                dayImgX += 78
            if(dayImgX == 702):
                dayImgX = 702
                print('10번째날이 되었습니다~!')

        if eggBrake:
            if (timeCount % 100 == 0):
                if(staminaImgX<600):
                    staminaImgX += 100
                if (interestingImgX < 600):
                    interestingImgX += 100
                if (hpImgX < 600):
                    hpImgX += 100


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

                if EggBrakeTextNum == 2 and eggBrakeindex == 24:
                    isShowTextAni = False
                    isTextAni1 = False
            #print(eggBrakeindex)

            if isImo == True:
                imoCount += 1
                if imoCount > 10:
                    isImo = False
                    imoCount = 0

        #print('selectEggNum =' , selectEggNum)
        scene_tick(clock, "secondScene")
        pass




    pygame.display.flip()

pygame.quit()
sys.exit()