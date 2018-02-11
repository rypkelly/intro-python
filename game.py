# Ryan Kelly (rpk2kn) and Christopher Geier (cpg3rb)

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

game_on = False
player1_score = 0
player2_score = 0
player1_timer = 0
player2_timer = 0

# Walls:
walls = [
    gamebox.from_color(800 / 2, 0, "green", 1000, 50),
    gamebox.from_color(800 / 2, 600, "green", 1000, 50),
    gamebox.from_color(800, 600 / 2, "green", 50, 1000),
    gamebox.from_color(0, 600 / 2, "green", 50, 1000)
]

statics = [

]

start_music = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/4/43/Blip.ogg")
game_music = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/a/a9/Bubble_01_nevit.ogg")
score1_sound_fx = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/f/fa/B-major.ogg")
score2_sound_fx = gamebox.load_sound("https://upload.wikimedia.org/wikipedia/commons/4/4b/D-major.ogg")

# Sprites
player1 = gamebox.from_image(350, 300, "http://imgur.com/BwkKz79.png")
player2 = gamebox.from_image(550, 300, "http://imgur.com/w4cXn38.png")
cube = gamebox.from_color(450, 300, 'cyan', 10, 10)
background = gamebox.from_image(400, 300, "http://imgur.com/GLS4MyZ.png")


# Speed initialization

def tick(keys):
    # Global Vars
    global game_on
    global player1_score
    global player1_timer
    global player2_score
    global player2_timer

    # screen.fill((255, 255, 255))
    if pygame.K_SPACE in keys:
        if not game_on:
            start_sound = start_music.play(1)
        game_on = True


    # Game Logic

    if not player1.touches(walls[0]):
        if pygame.K_UP in keys:
            player1.move(0, -16)
    if not player1.touches(walls[1]):
        if pygame.K_DOWN in keys:
            player1.move(0, 16)
    if not player1.touches(walls[2]):
        if pygame.K_RIGHT in keys:
            player1.move(16, 0)
    if not player1.touches(walls[3]):
        if pygame.K_LEFT in keys:
            player1.move(-16, 0)

    if not player2.touches(walls[0]):
        if pygame.K_w in keys:
            player2.move(0, -16)
    if not player2.touches(walls[1]):
        if pygame.K_s in keys:
            player2.move(0, 16)
    if not player2.touches(walls[2]):
        if pygame.K_d in keys:
            player2.move(16, 0)
    if not player2.touches(walls[3]):
        if pygame.K_a in keys:
            player2.move(-16, 0)

    if player1.touches(cube):
        player1_score += 1
        if player1_timer < 30:
            player1_score += 1
        player1_timer = 0
        cube.x = random.randint(75, 475)
        cube.y = random.randint(75, 575)
        score1_sound = score1_sound_fx.play()
    if player2.touches(cube):
        player2_score += 1
        if player2_timer < 30:
            player2_score += 1
        player2_timer = 0
        cube.x = random.randint(75, 475)
        cube.y = random.randint(75, 575)
        score2_sound = score2_sound_fx.play()

    # Render objects
    if game_on:
        camera.clear('black')
        for wall in walls:
            camera.draw(wall)
        camera.draw(background)
        camera.draw(player1)
        camera.draw(player2)
        camera.draw(cube)
        camera.draw(gamebox.from_text(300, 50, str(player1_score), "Arial", 50, "Brown", True))
        camera.draw(gamebox.from_text(500, 50, str(player2_score), "Arial", 50, "Brown", True))
        camera.draw(gamebox.from_text(300, 100, str(player1_timer // 30), "Arial", 25, "Purple", True))
        camera.draw(gamebox.from_text(500, 100, str(player2_timer // 30), "Arial", 25, "Purple", True))
        player1_timer += 1
        player2_timer += 1

    # End screen
    if player1_score >= 15:
        camera.draw(gamebox.from_text(400, 100, "Red Wins!", "Arial", 40, "Red", True))
        game_sound = game_music.play()
        gamebox.pause()
    if player2_score >= 15:
        camera.draw(gamebox.from_text(400, 100, "Yellow Wins!", "Arial", 40, "Yellow", True))
        game_sound = game_music.play()
        gamebox.pause()
    # Start screen
    if not game_on:
        camera.draw(gamebox.from_text(400, 200, 'The Race', 'Arial', 70, "Yellow", True))
        camera.draw(gamebox.from_text(400, 100, 'Created by Ryan Kelly (rpk2kn) and Christopher Geier (cpg3rb)'
                                                '', 'Arial', 20, "Green", True))
        camera.draw(gamebox.from_text(400, 300, 'Race your opponent to collect the dots as they pop up!', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 335, 'Collecting a dot while your timer is below 1', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 370, 'gives you a bonus point!', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 405, 'The first player to 15 points wins.', 'Arial', 28,
                              "Blue", True))
        camera.draw(gamebox.from_text(400, 440, 'Player 1 (RYAN THE RED) moves with the arrow keys.', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 475, 'Player 2 (CHRAZY CHRIS) moves with WASD.', 'Arial', 28,
                                      "Blue", True))
        camera.draw(gamebox.from_text(400, 550, 'Press SPACE to begin', 'Arial', 30, "Blue", True))

    camera.display()


gamebox.timer_loop(30, tick)