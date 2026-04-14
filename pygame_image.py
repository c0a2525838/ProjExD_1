import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_flip = pg.transform.flip(bg_img, True, False)  

    k_img = pg.image.load("fig/3.png")
    k_img = pg.transform.flip(k_img, True, False)
    k_rect=k_img.get_rect()
    tmr = 0  
    k_rect = k_img.get_rect()
    k_rect.center = 300, 200
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        x= tmr % 3200 

        screen.blit(bg_img, (-x, 0))
        screen.blit(bg_flip,(-x+1600,0))
        screen.blit(bg_img,(-x+3200,0))
        screen.blit(k_img,k_rect )
        

        key_states = pg.key.get_pressed()

        
        if key_states[pg.K_UP]:
            k_rect.move_ip(0, -1)
        if key_states[pg.K_DOWN]:
            k_rect.move_ip(0, 1)
        if key_states[pg.K_LEFT]:
            k_rect.move_ip(-1, 0)
        if key_states[pg.K_RIGHT]:
            k_rect.move_ip(1, 0)
       
        pg.display.update()
        tmr+=1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()