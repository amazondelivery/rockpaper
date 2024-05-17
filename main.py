import pygame as pg

#skeleton code is taken from pygame documentation

pg.init()
introFont = pg.font.SysFont("Comic Sans MS", 30)
miniIntroFont = pg.font.SysFont("Comic Sans MS", 12)
rock = pg.image.load("rock.png")
screen_width = 500
screen_height = 500
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

def introSequence():
    font = introFont
    minifont = miniIntroFont
    screen.fill("White")
    title = font.render("Press play to play Rock Paper!", True, "Black")
    playButton = font.render('play', True, 'Black')
    audio = minifont.render("audio: ", True, 'Black')

    screen.blit(title, (50,50))
    screen.blit(playButton, (200, 250))
    screen.blit(audio, (5, 0))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
    introSequence()
    clock.tick(60)
    pg.display.flip()


