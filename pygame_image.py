import pygame as pg
import sys
import random
def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("./ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    koka_img = pg.image.load("./ex01/fig/3.png")
    koka_img = pg.transform.flip(koka_img,True,False)
    koka_imgs = []
    r=50
    for i in range(r):
        l=i
        p=10/(r/2)
        if i>=r/2:
            koka_imgs.append(pg.transform.rotozoom(koka_img,p*l,1.0))
        else:
            l=l-(r/2)
            koka_imgs.append(pg.transform.rotozoom(koka_img,10-p*l,1.0))
    tmr = 0
    x=1
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x=tmr%(3200/3)
        screen.blit(bg_img, [-3*x, 0])
        screen.blit(bg_img2,[1600-3*x,0])
        screen.blit(bg_img,[3200-3*x,0])
        screen.blit(koka_imgs[tmr%r], [300,200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()