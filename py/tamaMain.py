# main.py
import random

import pygame
from pygame import *



import os
import sys

from sdl2 import SDL_KEYDOWN, SDLK_a, SDLK_d, SDLK_w, SDLK_s

from scene import (scene_tick, draw_start_scene, draw_first_scene, scene_speeds,
                   draw_second_scene,draw_third_scene,draw_fourth_scene)  # scene.py에서 함수 가져오기

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
font = pygame.font.Font('./resource/NeoDunggeunmoPro-Regular.ttf', 25)
fontSmall = pygame.font.Font('./resource/NeoDunggeunmoPro-Regular.ttf', 22)
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

timeSpeed = 3


selectEggNum = 99
secondScene = False
thirdScene = False
fourthScene = False

# 배경 및 버튼 이미지 불러오기
backGround = pygame.image.load('./resource/배경1.png')
morningTime = pygame.image.load('./resource/아침배경.png')
eveningTime = pygame.image.load('./resource/저녁배경.png')
nightTime = pygame.image.load('./resource/밤배경.png')
presentTime = morningTime

timeCount = 0

backG_1 = pygame.image.load('./resource/도트배경.png')
button1image = pygame.transform.scale(pygame.image.load('./resource/시작버튼.png'), (293 / 1.5, 91 / 1.5))
button1Loc = button1image.get_rect(center=(screen_width // 2, 320))
button2image = pygame.transform.scale(pygame.image.load('./resource/게임종료.png'), (293 / 1.5, 91 / 1.5))
button2Loc = button2image.get_rect(center=(screen_width // 2, 370))
titleImage = pygame.transform.scale(pygame.image.load('./resource/제목.png'), (450, 300))
titleLoc = titleImage.get_rect(center=(screen_width // 2, 150))

button3image = pygame.transform.scale(pygame.image.load('./resource/방법버튼.png'), (293 / 1.5, 91 / 1.5))
button3Loc = button3image.get_rect(center=(screen_width // 2, 420))


# 첫 번째 장면의 선택 이미지 및 알 이미지 불러오기
firstChoice1 = pygame.transform.scale(pygame.image.load('./resource/1.png'), (598 / smallSize, 736 / smallSize))
firstChoice1Loc = firstChoice1.get_rect(center=(target_width // 2, 300))
firstChoice2 = pygame.transform.scale(pygame.image.load('./resource/3.png'), (598 / smallSize, 736 / smallSize))
firstChoice2Loc = firstChoice2.get_rect(center=(target_width // 2, 300))



egg1 = pygame.image.load('./resource/알1.png')
egg1Loc = egg1.get_rect(center=(target_width // 2 - 150, 300))
egg2 = pygame.image.load('./resource/알2.png')
egg2Loc = egg2.get_rect(center=(target_width // 2, 300))
egg3 = pygame.image.load('./resource/알3.png')
egg3Loc = egg3.get_rect(center=(target_width // 2 + 150, 300))
selecFinalEggLoc = egg2.get_rect(center=(target_width // 2, 400))

changeEffect = image.load('./resource/페이드인아웃.png')
changeEffect2 = image.load('./resource/페이드아웃.png')
changeEffectCurFrame = 0
changeEffectCurFrame2 = 0
changeEffectFrame = 13
changeEffectLoc = changeEffect.get_rect(center=(target_width // 2, 0))
selecEgg = False
 # 검은색 페이드
isFadeIn = False

# 두번째 씬 (알 깨지고..~ 아기 태어나는 부분)
mainRoom_back = pygame.transform.smoothscale(pygame.image.load("./resource/배경방1.png"), (313, 313))
restRoom_back = pygame.transform.smoothscale(pygame.image.load('./resource/화장실.png'), (313, 313))

nowRoom = mainRoom_back

eggBrake = False
isTextAni1 = False

showEggBrakeDia = True
afterEggBrake_text = [" 짠!!  ","  당신의 다마고치가 태어났습니다!!  ", "   열심히 잘 키워보도록 하세요!!!!     "]
breakegg_text_displayed = ""
eggBrakeindex = 0
EggBrakeTextNum = 0
isShowTextAni = True

buttonEat = image.load('./resource/밥주기버튼.png')
buttonEatLoc = buttonEat.get_rect(center=(target_width//2 - 70,80))
buttonPlay = image.load('./resource/놀아주기버튼.png')
buttonPlayLoc = buttonEat.get_rect(center=(target_width//2 + 70,80))

# 성장별 모습
baby_growth_imgs_idle= ["./resource/아기1_idle.png", "./resource/아기2_idle.png"]
#IDLE 사이즈 36*36
frist_growth_imgs= image.load("./resource/IDLE반항기.png")
second_growth_imgs= image.load("./resource/IDLE사춘기.png")
final_growth_imgs= image.load("./resource/IDLE성인.png")

chaImage = None
chaImageX, chaImageY = 0,0
chaState = 1
growChaY= [-1,-1,-1]


# 대사들..
dialog1 = pygame.image.load('./resource/알깨주세요.png')
dialog1Loc = dialog1.get_rect(center=(target_width // 2, 300))
checkdig1 = True


#여러 이미지들...
loveImo = pygame.image.load('./resource/하트이모지.png')
sleepImo = pygame.image.load('./resource/잠이모지.png')
sleepButton = pygame.image.load('./resource/잠자기버튼.png')
sofa = pygame.image.load('./resource/소파.png')
arrowleft = pygame.image.load('./resource/화살표1.png')
arrowleftLoc = arrowleft.get_rect(center=(target_width//2 - 200,350))
arrowright = pygame.image.load('./resource/화살표2.png')
arrowrightLoc = arrowright.get_rect(center=(target_width//2 + 200,350))
showImos = None
isImo = False
imoCount = 0

changeScreen = pygame.image.load('./resource/알선택후화면전환1.png')
changSc = 99
isSceenChange = [False,False,False]

staminaImg = pygame.image.load('./resource/체력바_스테미너.png')
staminaImgX = 0

hpImg = pygame.image.load('./resource/체력바_체력.png')
hpImgX = 0

interestingImg = pygame.image.load('./resource/체력바_흥미.png')
interestingImgX = 0

dayImg = pygame.image.load('./resource/날짜디데이.png')
dayImgX = 0
dayNum = 1

timeImg = pygame.image.load('./resource/시간_아침.png')

cha_x = 270
cha_y = 350
cha_speed = 3

#똥 관련

ddong = pygame.transform.scale(pygame.image.load('./resource/똥.png'), (23*1.75,20*1.75))
ddongImo = pygame.image.load('./resource/똥이모지.png')
ddonglist = []

#벌레
bug = pygame.image.load('./resource/벌레.png')
buglist = []

dustImg = pygame.image.load('./resource/먼지.png')
dustlist = []


sc_frame = 0

show_emotion = pygame.image.load('./resource/기분표시_1.png')

walkBackGround = pygame.transform.smoothscale(image.load('./resource/배경_산책1.png'), (130 * 2.4, 130 *2.4))
buttonWalk = image.load('./resource/버튼_산책.png')
buttonWalkLoc = buttonEat.get_rect(center=(target_width//2 ,80))

def set_frame_rate(speed):
    scene_tick(clock, speed)


isFadeInEnd = False
isFadeOut = False
def fadeIn():
    global changeEffectCurFrame, isFadeIn, isFadeOut,isFadeInEnd
    isFadeIn = True
    if(isFadeIn):
        print(changeEffectCurFrame)
        #print('fadein 시작')
        x = changeEffectCurFrame * 600
        rect = pygame.Rect(x, 0, 600, 600)
        screen.blit(changeEffect, (0, 0), rect)
        if changeEffectCurFrame < 11:
            changeEffectCurFrame = (changeEffectCurFrame + 1)
        if changeEffectCurFrame >= 11:
            print(isFadeInEnd)
            changeEffectCurFrame = (changeEffectCurFrame + 1) % 12
            isFadeOut = True
            isFadeInEnd = True
            isFadeIn = False
            changeEffectCurFrame = 0
            #print('fadein 끝')
            print(isFadeInEnd)
            return



def fadeOut():

    global changeEffectCurFrame2,isFadeOut,isFadeIn,isFadeInEnd
    if(isFadeOut):
        #print('fadeout 시작')
        print(changeEffectCurFrame2)
        x = changeEffectCurFrame2 * 600
        rect = pygame.Rect(x, 0, 600, 600)
        screen.blit(changeEffect2, (0, 0), rect)
        if changeEffectCurFrame2 < 12:
            changeEffectCurFrame2 = (changeEffectCurFrame2 + 1)
        if changeEffectCurFrame2 == 12:
            print('fadeout 끝')
            changeEffectCurFrame2 = 0
            isFadeOut = False
            isFadeIn = False
            isFadeInEnd = False
            return


isWalking = False
walk_cha_x = 150
isDead = False
show_gameRule = False

def event_machine():
    global running, shrinking, startScene, \
        secondScene,firstScene, selectEggNum, selecEgg,eggBrake, isTextAni1,checkdig1,\
        showImos, cha_x,cha_y,isImo,imoCount,nowRoom,staminaImgX,interestingImgX,hpImgX,\
        thirdScene,buttonWalkLoc,buttonWalk,isWalking,walk_cha_x,isDead,button2Loc,dust,dustlist,timeCount,show_gameRule

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if startScene :
                if button1Loc.collidepoint(event.pos):
                    shrinking = True
                    startScene = False
                    firstScene = True

                elif button2Loc.collidepoint(event.pos):
                    running = False
                elif button3Loc.collidepoint(event.pos):
                    show_gameRule = True


                else:
                    show_gameRule = False
                    pass

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

                    if(staminaImgX>0 and staminaImgX <= 500):
                        staminaImgX -= 100
                        isImo = True
                        x = random.randint(200, 400)
                        ddonglist.append({"img": ddong, "pos": [x, cha_y + 35], "isShow": True, "ddongLoc" : ddong.get_rect(center=(x, cha_y + 35))})
                    elif(staminaImgX == 0):
                        print('배불러.. 스트레스!')

                    pass
                elif buttonPlayLoc.collidepoint(event.pos):
                    imoCount=0
                    print("놀아주기")
                    showImos = pygame.transform.smoothscale(loveImo, (30, 30))


                    if(staminaImgX<500):
                        staminaImgX += 100
                        isImo = True
                        if (interestingImgX > 0 and interestingImgX <= 500):
                            interestingImgX -= 100
                        elif(interestingImgX == 0):
                            print('더 안놀거임..스트레스!')
                            if (hpImgX < 600):
                                hpImgX += 100

                elif chaState >=3 and buttonWalkLoc.collidepoint(event.pos):
                    isWalking = True
                    print('산책가자')
                    walk_cha_x = 150
                    nowRoom = walkBackGround
                    timeCount = 215
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


                for ddongs in ddonglist:
                    ddongLoc = ddong.get_rect(topleft = (ddongs["pos"][0],ddongs["pos"][1]))
                    if ddongLoc.collidepoint(event.pos):
                        print('똥 클릭!!')
                        ddonglist.remove(ddongs)

                for bugs in buglist:
                    bugLoc = bug.get_rect(topleft = (bugs["pos"][0],bugs["pos"][1]))
                    if bugLoc.collidepoint(event.pos):
                        print('벌레 클릭!!')
                        #print(bugs["pos"][0])
                        #print(bugs["pos"][1])
                        buglist.remove(bugs)
                    if(bugs["pos"][1] > 550):
                        buglist.remove(bugs)

                for dusts in dustlist:
                    dustLoc = dustImg.get_rect(topleft = (dusts["pos"][0],dusts["pos"][1]))
                    if dustLoc.collidepoint(event.pos):
                        print('먼지 클릭!!')
                        dustlist.remove(dusts)

            if thirdScene:
                button2Loc = button2image.get_rect(center=(285, 500))
                if button2Loc.collidepoint(event.pos):
                    running = False

            if fourthScene:
                button2Loc = button2image.get_rect(center=(285, 500))
                if button2Loc.collidepoint(event.pos):
                    running = False






isMusic = [False,False,False,False]

# 애니메이션 루프
while running:
    if(isMusic[0] == False):
        pygame.mixer.music.load("./resource/동물의_숲1.mp3")
        pygame.mixer.music.set_volume(1.0)
        # BGM 재생 (무한 반복: -1)
        pygame.mixer.music.play(-1)
        isMusic[0] = True
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
        draw_start_scene(screen, firstChoice2Loc, firstChoice2, backGround, button1image, button1Loc,
                         button2image, button2Loc, titleImage, titleLoc, button3Loc,button3image,show_gameRule)
        scene_tick(clock, "startScene")
        #thirdScene = True




    elif firstScene:
        if first_context and index < len(text1):
            text_displayed += text1[index]
            index += 1
        draw_first_scene(screen, backG_1, firstChoice1, firstChoice1Loc, firstChoice2, firstChoice2Loc, egg1, egg1Loc, egg2, egg2Loc, egg3, egg3Loc, text_displayed, font, text_color)
        scene_tick(clock, "firstScene")

        if (selecEgg):

            fadeIn()

            if(isFadeInEnd):
                firstScene = False
                secondScene = True
                isFadeInEnd = False

            clock.tick(1000)
            pass

    elif secondScene :
        if (isMusic[1] == False):
            pygame.mixer.music.load("./resource/동물의_숲2.mp3")
            pygame.mixer.music.set_volume(1.0)
            # BGM 재생 (무한 반복: -1)
            pygame.mixer.music.play(-1)
            isMusic[1] = True
        #print(selectEggNum)
        #print(changSc)

        draw_second_scene(screen, firstChoice2, firstChoice2Loc, selectEggNum, egg1, egg2, egg3,
                          selecFinalEggLoc, mainRoom_back, restRoom_back,nowRoom, baby_growth_imgs_idle, eggBrake, text_displayed, fontSmall
                          ,breakegg_text_displayed,buttonEat,buttonPlay,buttonEatLoc,buttonPlayLoc,morningTime,eveningTime,nightTime
                          ,dialog1,dialog1Loc,checkdig1,cha_x,cha_y,isImo, showImos, imoCount,presentTime
                          ,arrowleft,arrowleftLoc,arrowright,arrowrightLoc,staminaImg,staminaImgX
                          ,isTextAni1,isShowTextAni,hpImgX,interestingImgX,interestingImg,hpImg,dayImg,dayImgX
                          ,ddong,ddonglist,chaImage,frist_growth_imgs,second_growth_imgs,final_growth_imgs,chaImageX, chaImageY,
                          dayNum,chaState,growChaY,timeImg,buglist,bug,show_emotion, thirdScene,
                          buttonWalk,buttonWalkLoc,isWalking,walk_cha_x,dustlist,dustImg,isDead)


        if eggBrake:

            if(not isWalking):

                for bugs in buglist:
                    if (bugs["pos"][0] + 50 > cha_x + 10 and
                            bugs["pos"][0] < cha_x + 10 + 50 and
                            bugs["pos"][1] + 50 > cha_y + 20 and
                            bugs["pos"][1] < cha_y + 20 + 50):
                        print('충돌이다다다')
                        show_emotion = pygame.image.load('./resource/기분표시_4.png')
                        #print(bugs["pos"][0])
                        #print(bugs["pos"][1])
                        if (hpImgX < 600):
                            hpImgX += 100
                        if (hpImgX == 600):
                            hpImgX = 600
                            staminaImgX = 600
                            interestingImgX = 600

                        buglist.remove(bugs)

                if (timeCount > 0 and timeCount < 100):
                    presentTime = morningTime
                    timeImg = pygame.image.load('./resource/시간_아침.png')
                    show_emotion = pygame.image.load('./resource/기분표시_1.png')
                elif (timeCount >= 100 and timeCount < 230):
                    presentTime = eveningTime
                    timeImg = pygame.image.load('./resource/시간_저녁.png')
                elif (timeCount >= 230 and timeCount < 350):
                    presentTime = nightTime
                    timeImg = pygame.image.load('./resource/시간_새벽.png')
                    darkImg = pygame.image.load('./resource/밤배경_dark.png')
                    show_emotion = pygame.image.load('./resource/기분표시_3.png')
                    screen.blit(darkImg, (150, 160))
                    # 벌레 추가
                    if (timeCount % (timeSpeed * 6) == 0):
                        bug_x = random.randint(200, 400)
                        bug_y = random.randint(150, 175)
                        buglist.append({"img": bug, "pos": [bug_x, bug_y], "isShow": True})



                elif (timeCount >= 350):

                    presentTime = morningTime
                    timeImg = pygame.image.load('./resource/시간_아침.png')
                    timeCount = 0



                    if (dayImgX <= 702 - (78*3)and dayNum <=8):
                        dayImgX += 78
                        dayNum += 1
                        if (dayNum > 1 and dayNum < 3):
                            print('베이비상태')
                            chaState = 1
                        elif (dayNum >= 3 and dayNum < 5):
                            chaState = 2
                            chaImage = frist_growth_imgs
                            print('반항기상태')

                        elif (dayNum >= 5 and dayNum < 7):
                            chaState = 3
                            chaImage = second_growth_imgs

                            print('사춘기상태')
                        elif (dayNum >= 7):
                            chaState = 4
                            chaImage = final_growth_imgs

                            print('성인상태')

                    if (dayImgX >= (78*7)):
                        dayImgX = (78*7)
                        print('8번째날이 되었습니다~!')
                        print(dayNum)

            if(dayNum < 8 and not isWalking and not isDead):
                timeCount += timeSpeed

            if(timeCount % (timeSpeed * 8) == 0 and staminaImgX == 500):
                hpImgX += 100
                if (hpImgX == 600):
                    hpImgX = 600
                    staminaImgX = 600
                    interestingImgX = 600


            if(isWalking):
                walk_cha_x += 8
                if(walk_cha_x > 420):
                    isWalking = False
                    walk_cha_x = 150
                    nowRoom = mainRoom_back
                    if (interestingImgX > 0 and interestingImgX <= 500):
                        interestingImgX = 0


            if(dayNum == 8):
                #print(dayNum)
                fadeIn()
                if (isFadeInEnd):
                    secondScene = False
                    thirdScene = True
                    isFadeInEnd = False

            # 스테미너 깎이는 것.
            if (timeCount % (timeSpeed * 33) == 0 and not isDead and dayNum < 8):
                if(staminaImgX<=500):
                    if(staminaImgX >= 500):
                        staminaImgX = 500
                    else:
                        staminaImgX += 100
                if (interestingImgX < 500):
                    interestingImgX += 100


            # 체력 깎이는 것..

            # 똥 추가
            if(timeCount % (timeSpeed * 27) == 0  and not isWalking and dayNum < 8):
                x = random.randint(200,400)
                ddonglist.append({"img":ddong, "pos" : [x,cha_y + 35], "isShow": True})

            # 먼지 추가
            if(timeCount % (timeSpeed * 13) == 0 and not isWalking and dayNum < 8):
                dustx = random.randint(150, 400)
                dusty = random.randint(200,400)
                dustlist.append({"img": dustImg, "pos": [dustx, dusty], "isShow": True})

        if(isFadeOut):
            fadeOut()



        if(isDead):
            secondScene = False
            fourthScene = True

        if (hpImgX == 600):
            staminaImgX = 600
            interestingImgX = 600
            isDead = True


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
                    scene_speeds["secondScene"] = 7
            #print(eggBrakeindex)

            if isImo == True:
                imoCount += 1
                if imoCount > 10:
                    isImo = False
                    imoCount = 0

        #print('selectEggNum =' , selectEggNum)
        scene_tick(clock, "secondScene")
        pass

    if thirdScene and not isDead:
        if (isMusic[2] == False):
            pygame.mixer.music.load("./resource/ooh.mp3")
            pygame.mixer.music.set_volume(1.0)
            # BGM 재생 (무한 반복: -1)
            pygame.mixer.music.play(-1)
            isMusic[2] = True
        chaImage = pygame.image.load('./resource/GROW성인.png')
        draw_third_scene(screen, thirdScene,backG_1,growChaY,chaImage,cha_x,cha_y,button2Loc,button2image)

        fadeOut()

        scene_tick(clock, "thirdScene")

    if fourthScene and isDead:
        if (isMusic[3] == False):
            pygame.mixer.music.load("./resource/죽음.mp3")
            pygame.mixer.music.set_volume(1.0)
            # BGM 재생 (무한 반복: -1)
            pygame.mixer.music.play(-1)
            isMusic[3] = True

        draw_fourth_scene(screen, backG_1,button2image,button2Loc)
        scene_tick(clock, "fourthScene")


    pygame.display.flip()

pygame.quit()
sys.exit()