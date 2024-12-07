# scene.py
import random

import pygame
from pygame import *



# 각 장면별 고유 속도 설정
scene_speeds = {
    "startScene": 3,
    "firstScene": 50000,
    "secondScene" : 10,
    "thirdScene" : 10,
    "fourthScene" : 10
}

babyIdleFrame = 6
frame = 0

wk_frame = 0


# 각 장면의 프레임 속도 조절 함수
def scene_tick(clock, scene_name):
    """현재 장면에 맞는 프레임 속도로 tick을 조절"""
    speed = scene_speeds.get(scene_name, 60)  # 기본값 60 프레임
    clock.tick(speed)

backOverlay1 = image.load('./resource/배경오버레이1.png')
backOverlay2 = image.load('./resource/배경오버레이2.png')
gameRule = image.load('./resource/게임방법.png')
tempStartSceneCount = 0
# 장면별 화면 그리기 함수
def draw_start_scene(screen, firstChoice2Loc, firstChoice2, backGround, button1image, button1Loc,
                     button2image, button2Loc, titleImage, titleLoc,button3Loc,button3image,show_gameRule):
    global tempStartSceneCount
    screen.blit(backGround, (0, 0))
    if(tempStartSceneCount == 0):
        screen.blit(backOverlay1, (0, 0))
        tempStartSceneCount =1
    elif (tempStartSceneCount == 1):
        screen.blit(backOverlay2, (0, 0))
        tempStartSceneCount = 0
    screen.blit(button1image, button1Loc)
    screen.blit(button2image, button2Loc)
    screen.blit(button3image, button3Loc)
    screen.blit(titleImage, titleLoc)

    if(show_gameRule):
        screen.blit(gameRule, (10,10))

eggframe_x = 0

staminaFrame = 0
staminaIndex=0
timeImgFrame = 0

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


howFood = 0
howPlay = 0
howFeel = 0
howLevel = 0
randFace = 0

sc_frame = 0
showScreenChange = False

baby = 99
CGtext_frame = 0
frame_width = 0
frame_x=0
frame_y = 0

# 이건 알선택후  -> 첫 화면..넘어가서.. 부터!
def draw_second_scene(screen, firstChoice2, firstChoice2Loc, selectEggNum, egg1, egg2, egg3,
                      selecFinalEggLoc, mainRoom_back, restRoom_back,nowRoom, baby_growth_imgs_idle, eggBrake, text_displayed,fontSmall
                      ,breakegg_text_displayed,buttonEat,buttonPlay,buttonEatLoc,buttonPlayLoc,morningTime,eveningTime,nightTime
                      ,dialog1,dialog1Loc,checkdig1,cha_x,cha_y,isImo, showImos, imoCount,presentTime,
                      arrowleft,arrowleftLoc,arrowright,arrowrightLoc,staminaImg,staminaImgX
                      ,isTextAni1,isShowTextAni,hpImgX,interestingImgX,interestingImg,hpImg,dayImg,dayImgX,
                      ddong,ddonglist,chaImage,frist_growth_imgs,second_growth_imgs,final_growth_imgs,chaImageX, chaImageY
                      ,dayNum,chaState,growChaY,timeImg,buglist,bug,show_emotion,thirdScene,
                      buttonWalk,buttonWalkLoc,isWalking,walk_cha_x,dustlist,dustImg,isDead):

    global character, frame,eggframe_x,index,EggBrakeTextNum,staminaFrame,staminaIndex,\
        timeImgFrame,sc_frame,showScreenChange,baby,wk_frame,frame_width,frame_x,frame_y
    screen.blit(presentTime, (0, 0))

    if(isWalking):
        screen.blit(nowRoom, (145, 175))

    else:
        screen.blit(nowRoom, (145, 175))

    if selectEggNum == 1:
        egg1 = image.load("./resource/알1_깨짐.png")
        baby_idle = image.load("./resource/아기1_idle.png")
        baby = 1
        pass
    elif selectEggNum == 2:
        egg1 = image.load("./resource/알2_깨짐.png")
        baby_idle = image.load("./resource/아기1_idle.png")
        baby = 1
        pass
    elif selectEggNum == 3:
        egg1 = image.load("./resource/알3_깨짐.png")
        baby_idle = image.load("./resource/아기2_idle.png")
        baby = 2
        pass



    if eggBrake == False:
        egg1 = egg1.subsurface(((eggframe_x * 75), 0, 75, 75))
        screen.blit(egg1, selecFinalEggLoc)
        eggframe_x = (eggframe_x + 1) % 5


    if eggBrake == True:

        timeImgX = timeImgFrame * 100
        timeImg_frame = timeImg.subsurface((timeImgX, 0, 100, 100))
        screen.blit(timeImg_frame, (10, 10))
        timeImgFrame= (timeImgFrame+1)%2

        if(not isWalking):
            for draw_ddong in ddonglist:
                screen.blit(ddong, draw_ddong["pos"])

                #pygame.draw.rect(screen, (100,0,0), (cha_x + 10, cha_y + 20, 50, 50))
            for bugs in buglist:
                bugs["pos"][1] += 6
                screen.blit(bug, bugs["pos"])
                #pygame.draw.rect(screen, (200, 40, 0), (bugs["pos"][0], bugs["pos"][1] + 50, 50, 50))

            for draw_dusts in dustlist:
                print(draw_dusts["pos"])
                screen.blit(dustImg, draw_dusts["pos"])

        if(chaState == 1):
            if presentTime == nightTime :
                if(baby == 1):
                    character_image = transform.scale(image.load('./resource/아기1_sleep.png'), (204 * 2, 54 * 2))
                elif(baby == 2):
                    character_image = transform.scale(image.load('./resource/아기2_sleep.png'), (204 * 2, 54 * 2))
            else:
                character_image = transform.scale(baby_idle, (204 * 2, 54 * 2))
            frame_width = 34 * 2
            frame_height = 54 * 2
            frame_x = frame * frame_width

            character_frame = character_image.subsurface((frame_x, 0, frame_width, frame_height))
            screen.blit(character_frame, (cha_x, cha_y))
            frame = (frame + 1) % babyIdleFrame

        elif(chaState == 2):
            if presentTime == nightTime:
                character_image = transform.scale(image.load('./resource/SLEEP반항기.png'), (144 * 2, 144 * 2))
            else:
                character_image = transform.scale(image.load('./resource/IDLE반항기.png'), (144 * 2, 144 * 2))

            if (growChaY[0] == -1):
                frame = 0
                growChaY[0] = random.randint(0, 3)
                print('growCha[0] : ', growChaY[0])

            frame_width = 36 * 2
            frame_height = 36 * 2
            print('frame_x',frame_x)
            print('frame_y:',frame_y)
            frame_x = frame * frame_width
            frame_y = growChaY[0] * frame_height
            character_frame = character_image.subsurface((frame_x, frame_y, frame_width, frame_height))
            screen.blit(character_frame, (cha_x, cha_y))
            frame = (frame + 1) % 4

        elif (chaState == 3):
            if(not isWalking):
                if presentTime == nightTime:
                    character_image = transform.scale(image.load('./resource/SLEEP사춘기.png'), (144 * 2.2, 144 * 2.2))
                else:
                    character_image = transform.scale(chaImage, (144 * 2.2, 144 * 2.2))

                if (growChaY[1] == -1):
                    frame = 0
                    growChaY[1] = random.randint(0, 3)
                    print('growCha[1] : ', growChaY[1])



                frame_width = 36 * 2.2
                frame_height = 36 * 2.2

                frame_x = frame * frame_width
                frame_y = growChaY[1] * frame_height
                character_frame = character_image.subsurface((frame_x, frame_y, frame_width, frame_height))
                screen.blit(character_frame, (cha_x, cha_y))
                frame = (frame + 1) % 4
            elif (isWalking):
                character_image = transform.scale(image.load('./resource/WALK사춘기.png'), (144 * 2, 144 * 2))
                wk_frame_width = 36 * 2
                wk_frame_height = 36 * 2

                wk_frame_x = wk_frame * wk_frame_width
                wk_frame_y = growChaY[1] * wk_frame_height
                wk_character_frame = character_image.subsurface((wk_frame_x, wk_frame_y, wk_frame_width, wk_frame_height))
                screen.blit(wk_character_frame, (walk_cha_x, cha_y))
                wk_frame = (wk_frame + 1) % 4


        elif (chaState == 4):
            if (not isWalking):
                if presentTime == nightTime:
                    character_image = transform.scale(image.load('./resource/SLEEP성인.png'), (144 * 2.3, 144 * 2.3))
                else:
                    character_image = transform.scale(chaImage, (144 * 2.3, 144 * 2.3))

                if (growChaY[2] == -1):
                    frame = 0
                    if(growChaY[1] == 3):
                        growChaY[2] = 3
                    else:
                        growChaY[2] = random.randint(0, 3)
                    print('growCha[2] : ', growChaY[2])

                frame_width = 36 * 2.3
                frame_height = 36 * 2.3

                frame_x = frame * frame_width
                frame_y = growChaY[2] * frame_height
                character_frame = character_image.subsurface((frame_x, frame_y, frame_width, frame_height))
                screen.blit(character_frame, (cha_x, cha_y))
                frame = (frame + 1) % 4
            elif (isWalking):
                character_image = transform.scale(image.load('./resource/WALK성인.png'), (144 * 2, 144 * 2))
                wk_frame_width = 36 * 2
                wk_frame_height = 36 * 2

                wk_frame_x = wk_frame * wk_frame_width
                wk_frame_y = growChaY[2] * wk_frame_height
                wk_character_frame = character_image.subsurface(
                    (wk_frame_x, wk_frame_y, wk_frame_width, wk_frame_height))
                screen.blit(wk_character_frame, (walk_cha_x, cha_y))
                wk_frame = (wk_frame + 1) % 4









    screen.blit(firstChoice2, firstChoice2Loc)
    screen.blit(arrowleft, arrowleftLoc)
    screen.blit(arrowright, arrowrightLoc)

    screen.blit(show_emotion, (300 - 70, 520))

    if (checkdig1 == True):
        screen.blit(dialog1, dialog1Loc)
    screen.blit(buttonEat, buttonEatLoc)
    screen.blit(buttonPlay, buttonPlayLoc)

    if(chaState>=3):
        screen.blit(buttonWalk, buttonWalkLoc)






    if (isShowTextAni == True):
        rendered_text = fontSmall.render(breakegg_text_displayed, True, (254, 254, 254))
        text_rect = rendered_text.get_rect(center=(screen.get_width() // 2, 580))
        screen.blit(rendered_text, text_rect)

    if isImo == True:

        screen.blit(showImos, (cha_x + 19 , cha_y - 20))

    if (hpImgX == 600):
        staminaImgX = 600
        interestingImgX = 600
        isDead = True

        # 공통 스테미너들...
    staminaImgFrameImg = staminaImg.subsurface((staminaImgX, 0, 100, 30))
    screen.blit(staminaImgFrameImg, (145, 470))

    hpImgFrame = hpImg.subsurface((hpImgX, 0, 100, 30))
    screen.blit(hpImgFrame, (255, 470))
    interestingImgFrame = interestingImg.subsurface((interestingImgX, 0, 100, 30))
    screen.blit(interestingImgFrame, (365, 470))
    dayImgFrame = dayImg.subsurface((dayImgX, 0, 78, 22))
    screen.blit(dayImgFrame, (265, 150))

frame3 = 0
def draw_third_scene(screen, thirdScene,backG_1,growChaY,chaImage,cha_x,cha_y,button2Loc,button2image):
    global CGtext_frame,frame3
    screen.blit(backG_1, (0, 0))

    clearGameTextImg = pygame.image.load('./resource/성장완료.png')

    cg_textframe_x = CGtext_frame * 400

    clearGameTextImg_frame = clearGameTextImg.subsurface((cg_textframe_x, 0, 400, 100))
    screen.blit(clearGameTextImg_frame, (100, 200))
    CGtext_frame = (CGtext_frame + 1) % 2

    character_image = transform.scale(chaImage, (144 * 2, 144 * 2))
    frame_width = 36 * 2
    frame_height = 36 * 2
    frame_x = frame3 * frame_width
    frame_y = growChaY[2] * frame_height
    character_frame = character_image.subsurface((frame_x, frame_y, frame_width, frame_height))
    screen.blit(character_frame, (cha_x, cha_y-50))
    frame3 = (frame3 + 1) % 4

    button2Loc = button2image.get_rect(center=(285, 500))
    screen.blit(button2image, button2Loc)
    #print('3번째 신 시작!')

def draw_fourth_scene(screen,backG_1,button2image,button2Loc):
    global CGtext_frame,frame
    #print('죽음!')
    screen.blit(backG_1, (0, 0))

    clearGameTextImg = pygame.image.load('./resource/사망문구.png')

    cg_textframe_x = CGtext_frame * 500

    clearGameTextImg_frame = clearGameTextImg.subsurface((cg_textframe_x, 0, 500, 100))
    screen.blit(clearGameTextImg_frame, (50, 200))
    CGtext_frame = (CGtext_frame + 1) % 2

    button2Loc = button2image.get_rect(center=(285, 500))
    screen.blit(button2image, button2Loc)