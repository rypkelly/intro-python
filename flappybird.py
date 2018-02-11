# Ryan Kelly (rpk2kn)

import pygame
import gamebox
import random
camera = gamebox.Camera(800, 600)

bird = gamebox.from_color(200, 300, "BLUE", 20, 20)
ground = gamebox.from_color(400, 525, "Green", 800, 150)
pillar1_bottom = gamebox.from_color(700, 400, "RED", 75, random.randrange(10, 300))
pillar1_bottom.bottom = 450
pillar1_top = gamebox.from_color(700, 1, "RED", 75, 5000)
pillar1_top.bottom = 340 - pillar1_bottom.height

pillar2_bottom = gamebox.from_color(1400, 400, "RED", 75, random.randrange(10, 300))
pillar2_bottom.bottom = 450
pillar2_top = gamebox.from_color(1400, 1, "RED", 75, 5000)
pillar2_top.bottom = 340 - pillar2_bottom.height
score = 0

def tick(keys):
    global score
    score += 1

    if pygame.K_SPACE in keys:
        bird.speedy = -11
    bird.speedy += 1
    bird.move_speed()

    pillar1_bottom.speedx = -10
    pillar1_top.speedx = -10
    pillar2_bottom.speedx = -10
    pillar2_top.speedx = -10
    pillar1_bottom.move_speed()
    pillar1_top.move_speed()
    pillar2_bottom.move_speed()
    pillar2_top.move_speed()

    if pillar1_bottom.right < 1:
        pillar1_bottom.left = pillar2_bottom.left + 700
        pillar1_top.left = pillar2_bottom.left + 700
        pillar1_bottom.size = 75, random.randrange(10, 300)
        pillar1_bottom.bottom = 450
        pillar1_top.bottom = 340 - pillar1_bottom.height
    if pillar2_bottom.right < 1:
        pillar2_bottom.left = pillar1_bottom.left + 700
        pillar2_top.left = pillar1_bottom.left + 700
        pillar2_bottom.size = 75, random.randrange(10, 300)
        pillar2_bottom.bottom = 450
        pillar2_top.bottom = 340 - pillar2_bottom.height

    camera.clear("black")
    camera.draw(bird)
    camera.draw(ground)
    camera.draw(pillar1_bottom)
    camera.draw(pillar1_top)
    camera.draw(pillar2_bottom)
    camera.draw(pillar2_top)
    keys.clear()
    if bird.touches(ground) or bird.touches(pillar1_bottom) or bird.touches(pillar1_top) \
            or bird.touches(pillar2_bottom) or bird.touches(pillar2_top):
        camera.clear("BLACK")
        score_box = gamebox.from_text(camera.x, camera.y, "Score: " + str(score // 30), "arial", 24, "white")
        camera.draw(score_box)
        gamebox.pause()
    camera.display()

gamebox.timer_loop(40, tick)
