import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
   pygame.init()
   screen = pygame.display.set_mode((700,800))
   pygame.display.set_caption("My game")
   bg_color = (0, 0, 0)
   gun = Gun(screen)
   bullets = Group()
   inos = Group()
   controls.create_army(screen, inos)
   stats = Stats()
   sc = Scores(screen, stats)

   while True:
      font = pygame.font.SysFont(None, 36)
      nadpis1 = font.render("SCORE:", 1, (250, 0, 0), (0, 0, 0))
      nadpis2 = font.render("HIGH SCORE:", 1, (250, 0, 0), (0, 0, 0))
      screen.blit(nadpis1, (520, 20))
      screen.blit(nadpis2, (160, 20))
      pygame.display.update()
      controls.events(screen, gun, bullets)
      if stats.run_game:
         gun.update_gun()
         controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
         controls.update_bullets(screen, stats, sc, inos, bullets)
         controls.update_inos(stats, screen, sc, gun, inos, bullets)



run()

