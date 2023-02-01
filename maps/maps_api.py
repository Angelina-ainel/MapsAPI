import pygame as pg
import requests
import yandex_api_library
from io import BytesIO


class MapApp:
    def __init__(self, size):
        pg.init()
        self.screen = pg.display.set_mode(size)
        self.running = True
        self.map = None
        self.update_map()

    def update_map(self):
        bytes_image = yandex_api_library.get_static(l='map', ll='60.153078,55.147551', z=15, size='650,450')
        self.map = pg.image.load(BytesIO(bytes_image))

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.screen.fill('black')
            self.screen.blit(self.map, (0, 0))
            pg.display.flip()


size = 650, 450
app = MapApp(size)
app.run()
