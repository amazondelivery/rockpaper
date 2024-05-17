import pygame as pg

#skeleton code is taken from pygame documentation

pg.init()
font = pg.font.SysFont("Comic Sans MS", 30)
minifont = pg.font.SysFont()
screen_width = 500
screen_height = 500
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

def introSequence():
    screen.fill("White")
    title = font.render("Press play to play Rock Paper!", True, "Black")
    playButton = font.render('play', True, 'Black')
    audio = font.render()

    screen.blit(title, (50,50))
    screen.blit(playButton, (200, 250))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
    introSequence()
    clock.tick(60)
    pg.display.flip()


