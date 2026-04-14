import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0

    
    k_img = pg.image.load("fig/3.png")
    k_img = pg.transform.flip(k_img, True, False)

    
    bg_x = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        
        bg_x -= 2

        
        if bg_x <= -bg_img.get_width():
            bg_x = 0

        
        screen.blit(bg_img, [bg_x, 0])
        screen.blit(bg_img, [bg_x + bg_img.get_width(), 0])

        
        screen.blit(k_img, [300, 200])

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()