import pygame as pg

#skeleton code is taken from pygame documentation

pg.init()
introFont = pg.font.SysFont("Comic Sans MS", 30)
miniIntroFont = pg.font.SysFont("Comic Sans MS", 12)
rock = pg.image.load("rock.png")
Xrock, Yrock = rock.get_size()
screen_width = 500
screen_height = 500
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

def wrapRect(obj, color='Black'):
    rect = obj.get_rect()
    pg.draw.rect(obj, color, rect, 1)
    return obj

def introSequence():
    font = introFont
    minifont = miniIntroFont
    screen.fill("White")
    title = font.render("Press play to play Rock Paper!", True, "Black")
    playButton = wrapRect(font.render('Play', True, 'Black'))
    settingsButton = font.render("Settings", True, 'Black')
    audio = minifont.render("audio: ", True, 'Black')

    screen.blit(title, (50,50))
    screen.blit(playButton, (200, 170))
    screen.blit(audio, (5, 0)) #audio text
    screen.blit(settingsButton, (200, 200))

def introStory():
    rockScaleFactor = 0.45
    rockText = "hello! i'm rock, and i need YOUR help to defeat my nemisis, paper!"
    screen.blit(pg.transform.smoothscale(rock,
                (Xrock * rockScaleFactor, Yrock * rockScaleFactor)),
                (0, 320)) #rock image

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
    introSequence()
    clock.tick(60)
    pg.display.flip()


