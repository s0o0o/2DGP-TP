# scene.py
import pygame
from pygame import *



# 각 장면별 고유 속도 설정
scene_speeds = {
    "startScene": 100,
    "firstScene": 50000,
    "secondScene" : 10
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

eggframe_x = 0

staminaFrame = 0
staminaIndex=0


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





# 이건 알선택후  -> 첫 화면..넘어가서.. 부터!
def draw_second_scene(screen, firstChoice2, firstChoice2Loc, selectEggNum, egg1, egg2, egg3,
                      selecFinalEggLoc, mainRoom_back, restRoom_back,nowRoom, baby_growth_imgs_idle, eggBrake, text_displayed,fontSmall
                      ,breakegg_text_displayed,buttonEat,buttonPlay,buttonEatLoc,buttonPlayLoc,morningTime,eveningTime,nightTime
                      ,dialog1,dialog1Loc,checkdig1,cha_x,cha_y,isImo, showImos, imoCount,presentTime,
                      arrowleft,arrowleftLoc,arrowright,arrowrightLoc,staminaImg,staminaImgX
                      ,isTextAni1,isShowTextAni,hpImgX,interestingImgX,interestingImg,hpImg,dayImg,dayImgX):

    global character, frame,eggframe_x,index,EggBrakeTextNum,staminaFrame,staminaIndex
    screen.blit(presentTime, (0, 0))
    screen.blit(nowRoom, (145, 175))
    screen.blit(firstChoice2, firstChoice2Loc)
    screen.blit(arrowleft, arrowleftLoc)
    screen.blit(arrowright, arrowrightLoc)



    if( checkdig1 == True ):
        screen.blit(dialog1, dialog1Loc)
    screen.blit(buttonEat, buttonEatLoc)
    screen.blit(buttonPlay,buttonPlayLoc)


    if selectEggNum == 1:
        egg1 = image.load("알1_깨짐.png")
        baby_idle = image.load("아기1_idle.png")
        pass
    elif selectEggNum == 2:
        egg1 = image.load("알2_깨짐.png")
        baby_idle = image.load("아기1_idle.png")
        pass
    elif selectEggNum == 3:
        egg1 = image.load("알3_깨짐.png")
        baby_idle = image.load("아기2_idle.png")
        pass



    if eggBrake == False:
        egg1 = egg1.subsurface(((eggframe_x * 75), 0, 75, 75))
        screen.blit(egg1, selecFinalEggLoc)
        eggframe_x = (eggframe_x + 1) % 5


    if eggBrake == True:



        character_image = transform.scale(baby_idle, (204 * 2, 54 * 2))
        frame_width = 34 * 2
        frame_height = 54 * 2
        frame_x = frame * frame_width

        character_frame = character_image.subsurface((frame_x, 0, frame_width, frame_height))
        screen.blit(character_frame, (cha_x, cha_y))
        frame = (frame + 1) % babyIdleFrame

        staminaImgFrameImg = staminaImg.subsurface((staminaImgX, 0, 100, 30))
        screen.blit(staminaImgFrameImg, (145,470))

        hpImgFrame = hpImg.subsurface((hpImgX, 0, 100, 30))
        screen.blit(hpImgFrame, (255, 470))

        interestingImgFrame = interestingImg.subsurface((interestingImgX, 0, 100, 30))
        screen.blit(interestingImgFrame, (365, 470))

        dayImgFrame = dayImg.subsurface((dayImgX, 0, 78, 22))
        screen.blit(dayImgFrame, (265, 150))

        if (isShowTextAni == True):
            rendered_text = fontSmall.render(breakegg_text_displayed, True, (254, 254, 254))
            text_rect = rendered_text.get_rect(center=(screen.get_width() // 2, 530))
            screen.blit(rendered_text, text_rect)


        if isImo == True:

            screen.blit(showImos, (cha_x + 19 , cha_y))



