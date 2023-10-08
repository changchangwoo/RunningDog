import random
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

WIDTH = 1000
HEIGHT = 500


screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Running Dog -python project")

# 이미지 불러오기
imgDog1OG = pygame.image.load('image/dog_run1.png')
imgDog2OG = pygame.image.load('image/dog_run2.png')
imgLowDog1OG = pygame.image.load('image/dog_low_run1.png')
imgLowDog2OG = pygame.image.load('image/dog_low_run2.png')
imgCloudOG = pygame.image.load(('image/cloud.png'))
imgTreeOG = pygame.image.load(('image/tree.png'))
imgTree2OG = pygame.image.load(('image/tree1.png'))
imgTrackOG = pygame.image.load(('image/track.png'))
imgMenu = pygame.image.load(('image/menu.png'))
imgHowtoplay = pygame.image.load(('image/Howtoplay.png'))
imgSelect = pygame.image.load(('image/select.png'))
imgbonusOG = pygame.image.load(('image/bonus.png'))
imgDeath = pygame.image.load(('image/Death.png'))
imgBird1OG = pygame.image.load(('image/bird1.png'))
imgBird2OG = pygame.image.load(('image/bird2.png'))
imgspeedupOG = pygame.image.load(('image/speedup.png'))
imgTimebonusOG = pygame.image.load(('image/watch.png'))
img2ComboOG = pygame.image.load('image/2combo.png')
img3ComboOG = pygame.image.load('image/3combo.png')
img4ComboOG = pygame.image.load('image/4combo.png')


# 사운드 불러오기
Click_sound = pygame.mixer.Sound('sound/Click.wav')
Death_sound = pygame.mixer.Sound('sound/Death.wav')
Get_sound = pygame.mixer.Sound('sound/Get.wav')
Speedup_sound = pygame.mixer.Sound('sound/Speedup.wav')
Timebonus_sound = pygame.mixer.Sound('sound/Watch.wav')
# 사운드 음량 조정
Click_sound.set_volume(0.15)
Death_sound.set_volume(0.1)
Get_sound.set_volume(0.1)

# 이미지의 크기 조정
imgDog1 = pygame.transform.scale(imgDog1OG, (150,130))
imgDog2 = pygame.transform.scale(imgDog2OG, (150,130))
imgBird1 = pygame.transform.scale(imgBird1OG, (150,150))
imgBird2 = pygame.transform.scale(imgBird2OG, (150,150))
imgLowDog1 = pygame.transform.scale(imgLowDog1OG, (150,130))
imgLowDog2 = pygame.transform.scale(imgLowDog2OG, (150,130))
imgCloud = pygame.transform.scale(imgCloudOG, (200,200))
imgTree = pygame.transform.scale(imgTreeOG,(200,130))
imgTree2 = pygame.transform.scale(imgTree2OG,(200,130))
imgTrack = pygame.transform.scale(imgTrackOG,(4000,1000))
imgbonus = pygame.transform.scale(imgbonusOG,(50,50))
imgspeedup = pygame.transform.scale(imgspeedupOG,(300,150))
imgTimebonus = pygame.transform.scale(imgTimebonusOG,(50,50))
img2Combo = pygame.transform.scale(img2ComboOG, (300,150))
img3Combo = pygame.transform.scale(img3ComboOG, (300,150))
img4Combo = pygame.transform.scale(img4ComboOG, (300,150))


# 이미지 고유 프레임 조정
imgcontrol = 0
flyimagecontrol = 0
# 폰트 생성 및 출력할 문자열 지정
font = pygame.font.SysFont('Arial', 50)


if __name__ == '__main__':
    fps = pygame.time.Clock()
    # 플레이어
    dog_height = imgDog1.get_size()[1]
    dog_bottom = HEIGHT - dog_height
    dog_x = 50
    dog_y = dog_bottom
    jump_top = 200
    leg_swap = True
    is_bottom = True
    is_go_up = False
    JumpCheck = False
    LowCheck = False
    # 구름
    cloud_x_pos = WIDTH
    cloud_y_pos = 80
    cldCheck = False
    # 구름2
    cloud_x_pos2 = WIDTH
    cloud_y_pos2 = 80
    cldCheck2 = False
    # 구름3
    cloud_x_pos3 = WIDTH
    cloud_y_pos3 = 80
    cldCheck3 = False
    # 나무1
    tree_x_pos = WIDTH
    tree_y_pos = HEIGHT - imgTree.get_size()[1]
    maketree = 0
    makecount = 0
    treemove = True
    # 나무2
    tree_x_pos2 = WIDTH + 500
    tree_y_pos2 = HEIGHT - imgTree.get_size()[1]
    maketree2 = 0
    makecount2 = 0
    treemove2 = True
    # 보너스
    bonus_x_pos = WIDTH + 1500
    bonus_y_pos = 250
    bonusmove = True
    bonusmakecount = 0
    makebonus = 0
    # 시간보너스
    timebonus_x_pos = WIDTH + 1500
    timebonus_y_pos = 250
    timebonusmove = True
    timebonusmakecount = 0
    timemakebonus = 0
    timebonuscheck = False
    timebonusspeed = 0
    timetime = 0
    # 바닥
    track_x_pos = 0
    track_y_pos = -510
    # 설정 변수
    step = 0
    run = True
    # 새
    birdimage = True
    birdmove = True
    bird_x_pos = WIDTH + 1000
    bird_y_pos = 280
    makebird = 0
    makebirdcount = 0
    # 난이도 조절 변수
    level = 0
    # 포인트 변수
    point = 0
    maxpoint = 0
    checkpoint = 0
    pointcontrol = 0
    speedup = 0
    speedupcheck = False
    # 사운드 변수
    soundcheck = True
    speedupsoundcheck = True
    # 스피드업 출력 변수
    imgspeedupTF = False
    imgspeedupcheck = 0
    # 콤보변수
    combolevel = 0
    combotime = 0
    imgcomboTF = False
    imgcombocheck = 0

    while run:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_UP and is_bottom:
                    is_go_up = True
                    is_bottom = False
                if event.key == pygame.K_DOWN and is_bottom:
                    LowCheck = True
                if (step == 0) :
                    step = 1
                    Click_sound.play()
                elif (step == 1) :
                    step = 4
                    Click_sound.play()
                elif (step == 4) :
                    if event.key == pygame.K_LEFT :
                        level = 0
                        step = 2
                        Click_sound.play()
                    elif event.key == pygame.K_RIGHT :
                        level = 6
                        step = 2
                        Click_sound.play()
                elif (step == 3) :
                    tree_x_pos = WIDTH
                    tree_x_pos2 = WIDTH + 500
                    bonus_x_pos = WIDTH + 1500
                    timebonus_x_pos = WIDTH + 2000
                    bird_x_pos = WIDTH + 1000
                    step = 2
                    point = 0
                    speedup = 0
                    timetime = 0
                    checkpoint = 0
                    combolevel = 0
                    timebonuscheck = False
                    speedupcheck = True
                    soundcheck = True
                    Click_sound.play()
            elif event.type == pygame.KEYUP:
                if LowCheck : LowCheck = False

        if (step == 0) : # 메뉴 실행
            screen.blit(imgMenu,(0,0))
            pygame.display.update()

        if (step == 4) : # 난이도 선택
            screen.blit(imgSelect,(0,0))
            pygame.display.update()

        if (step == 1) : # 게임설명
            screen.blit(imgHowtoplay,(0,0))
            pygame.display.update()

        if (step == 2) : # 게임 실행

        # 점수 생성 및 점수 변화 이미지
            score = font.render(str(point), True, WHITE)
            screen.blit(score,(WIDTH-90, 30))
            pointcontrol = pointcontrol+1
            if(pointcontrol == 70) :
                pointcontrol = 0
                point = point+1
                checkpoint = checkpoint+1
            if(checkpoint // 30 >= 1) :
                if imgspeedupTF == False :
                    screen.blit(imgspeedup,(WIDTH-650, 70))
                    if speedupsoundcheck == True :
                        Speedup_sound.play()
                        speedupsoundcheck = False
                    imgspeedupcheck = imgspeedupcheck+1
                    if imgspeedupcheck >= 150 :
                        speedupsoundcheck = True
                        imgspeedupcheck = 0
                        checkpoint = checkpoint % 30
                        imgspeedupTF = True
                if(speedupcheck == True) :
                    speedup = speedup+2
                    speedupcheck = False
            else : speedupcheck = True
            imgspeedupTF = False

        # 타임보너스 실행
            if(timebonuscheck == True) :
                timetime = timetime + 1
                timebonusspeed = 3
                if timetime >= 1000 :
                    timebonuscheck = False
                    timetime = 0
            else :
                timebonusspeed = 0

        # 트랙 생성
            screen.blit(imgTrack, (track_x_pos, track_y_pos))
        # 나무 생성
            screen.blit(imgTree, (tree_x_pos, tree_y_pos - 10))
            screen.blit(imgTree2, (tree_x_pos2, tree_y_pos - 10))
        # 보너스 생성
            screen.blit(imgbonus, (bonus_x_pos, bonus_y_pos - 10))
            screen.blit(imgTimebonus, (timebonus_x_pos,timebonus_y_pos - 10))
        # 구름 생성
            screen.blit(imgCloud, (cloud_x_pos + 100, cloud_y_pos))
            screen.blit(imgCloud, (cloud_x_pos2 + 300, cloud_y_pos2))
            screen.blit(imgCloud, (cloud_x_pos3 + 500, cloud_y_pos3))

        # 보너스 움직임
            if bonusmove :
                bonus_x_pos -= 10.0
                if bonus_x_pos < - 1000:
                    makebonus = random.randint(500,1000)
                    bonusmove = False
            if not bonusmove :
                if (bonusmakecount >= makebonus) :
                    bonusmakecount = 0
                    bonus_x_pos = WIDTH
                    bonusmove = True
            bonusmakecount = bonusmakecount + 1

            # 타임보너스 움직임
            if timebonusmove:
                timebonus_x_pos -= 15.0
                if timebonus_x_pos < - 1000:
                    timemakebonus = random.randint(500, 1000)
                    timebonusmove = False
            if not timebonusmove:
                if (timebonusmakecount >= timemakebonus):
                    timebonusmakecount = 0
                    timebonus_x_pos = WIDTH
                    timebonusmove = True
                timebonusmakecount = timebonusmakecount + 1

        # 새 움직임
            if birdmove :
                bird_x_pos -= (12.0+level+speedup-timebonusspeed)
                if bird_x_pos < - 400:
                    makebird = random.randint(500,600)
                    birdmove = False
            if not birdmove :
                if (makebirdcount >= makebird) :
                    makebirdcount = 0
                    bird_x_pos = WIDTH
                    birdmove = True
            makebirdcount = makebirdcount + 1

        # 나무 움직임
            if treemove :
                tree_x_pos -= (12.0+level+speedup-timebonusspeed)
                if tree_x_pos < -400:
                    maketree = random.randint(400, 800)
                    treemove = False

            if not treemove :
                if (makecount >= maketree) :
                    makecount = 0
                    tree_x_pos = WIDTH
                    treemove = True
            makecount = makecount + 1

            if treemove2:
                tree_x_pos2 -= (12.0+level+speedup-timebonusspeed)
                if tree_x_pos2 < -850:
                    maketree2 = random.randint(200, 550)
                    treemove2 = False

            if not treemove2:
                if (makecount2 >= maketree2):
                    makecount2 = 0
                    tree_x_pos2 = WIDTH
                    treemove2 = True
            makecount2 = makecount2 + 1

        # 구름 움직임 및 구름 위치 랜덤 생성
            cloud_x_pos -= 6.0
            if cloud_x_pos < -450:
                cloud_x_pos = WIDTH
                cldCheck = True
            if cldCheck :
                cloud_y_pos = random.randint(-50,80)
                cldCheck = False
            cloud_x_pos2 -= 5.0
            if cloud_x_pos2 < -800:
                cloud_x_pos2 = WIDTH
                cldCheck2 = True
            if cldCheck2:
                cloud_y_pos2 = random.randint(-50,80)
                cldCheck2 = False
            cloud_x_pos3 -= 7.0
            if cloud_x_pos3 < -800:
                cloud_x_pos3 = WIDTH
                cldCheck3 = True
            if cldCheck3:
                cloud_y_pos3 = random.randint(-50, 80)
                cldCheck3 = False

            # 플레이어 점프
            if is_go_up:
                dog_y -= 15.0
                JumpCheck = True

            elif not is_go_up and not is_bottom:
                dog_y += 10.0

            # 플레이어 점프 상태 확인
            if is_go_up and dog_y <= jump_top:
                is_go_up = False

            if not is_bottom and dog_y >= dog_bottom:
                is_bottom = True
                JumpCheck = False
                dog_y = dog_bottom

            # 플레이어 움직임
            if leg_swap:
                if JumpCheck : screen.blit(imgDog2, (dog_x, dog_y))
                elif LowCheck : screen.blit(imgLowDog1, (dog_x, dog_y-10))
                else : screen.blit(imgDog1, (dog_x, dog_y-10))
                imgcontrol = imgcontrol + 1
                if(imgcontrol == 10):
                    imgcontrol = 0
                    leg_swap = False
            else :
                if JumpCheck : screen.blit(imgDog2, (dog_x, dog_y))
                elif LowCheck : screen.blit(imgLowDog2, (dog_x, dog_y-10))
                else : screen.blit(imgDog2, (dog_x, dog_y-10))
                imgcontrol = imgcontrol + 1
                if (imgcontrol == 10):
                    imgcontrol = 0
                    leg_swap = True

            # 새 움직임
            if birdimage:
                screen.blit(imgBird1,(bird_x_pos,bird_y_pos))
                flyimagecontrol = flyimagecontrol+1
                if (flyimagecontrol == 15):
                    flyimagecontrol = 0
                    birdimage = False
            else :
                screen.blit(imgBird2, (bird_x_pos, bird_y_pos))
                flyimagecontrol = flyimagecontrol+1
                if (flyimagecontrol == 15) :
                    flyimagecontrol = 0
                    birdimage = True

            # 충돌 (나무 1)
                colidX = abs(tree_x_pos - dog_x)
                colidY = abs(tree_y_pos - dog_y)
                if colidX <= 40 and colidY <= 70 : step = 3
            # 충돌 (나무 2)
                colidX2 = abs(tree_x_pos2 - dog_x)
                colidY2 = abs(tree_y_pos2 - dog_y)
                if colidX2 <= 40 and colidY2 <= 70: step = 3
            # 충돌 (새)
                colidX4 = abs(bird_x_pos - dog_x)
                colidY4 = abs(bird_y_pos - dog_y)
                if colidX4 <= 50 and colidY4 <= 150 and LowCheck == False :
                    step = 3

            # 충돌 (보너스)
                colidX3 = abs(bonus_x_pos - dog_x)
                colidY3 = abs(bonus_y_pos - dog_y)
                if colidX3 <= 50 and colidY3 <= 70:
                    point = point+5
                    checkpoint = checkpoint+5
                    bonus_x_pos = WIDTH + 1000
                    combotime = 0
                    combolevel = combolevel+1
                    imgcomboTF = False
                    Get_sound.play()

            # 콤보타임
                combotime = combotime + 1
                if (combotime >= 200):
                    imgcomboTF = False
                    combolevel = 0
            # 콤보
                if combolevel == 2 :
                    if imgcomboTF == False :
                        screen.blit(img2Combo,(WIDTH-650, 70))
                        imgcombocheck = imgcombocheck+1
                        if(imgcombocheck >= 45) :
                            imgcombocheck = 0
                            imgcomboTF = True

                if combolevel >= 3 :
                    if imgcomboTF == False :
                        screen.blit(img3Combo,(WIDTH-650, 70))
                        imgcombocheck = imgcombocheck+1
                        if(imgcombocheck >= 40) :
                            imgcombocheck = 0
                            imgcomboTF = True



            # 충돌 (타임보너스)
                colidX5 = abs(timebonus_x_pos - dog_x)
                colidY5 = abs(timebonus_y_pos - dog_y)
                if colidX5 <= 50 and colidY5 <= 70:
                    Timebonus_sound.play()
                    timebonus_x_pos = WIDTH + 1000
                    timebonuscheck = True

            pygame.display.update()

            fps.tick(60)

        # 죽었을 때 화면
        if (step == 3) :
            if soundcheck == True :
                Death_sound.play()
                soundcheck = False
            point = point + 0
            if (point >= maxpoint) :
                maxpoint = point
            score = font.render(str(point), True, WHITE)
            maxscore = font.render(str(maxpoint), True, WHITE)
            screen.blit(score, (WIDTH - 100, 100))
            screen.blit(maxscore, (WIDTH - 100, 150))
            screen.blit(imgDeath,(0,0))
            pygame.display.update()

    pygame.quit()
