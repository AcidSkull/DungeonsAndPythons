class TileMap:
    def __init__(self, file, size = (64, 64)):
        self.file = file
        self.size = size
        self.tiles = []
        self._load()

    def _load(self):
        pass
        # for x in range(10):
        #     self.tile[x] = []
        #     for y in range(10):
        #         self.tile[x].append()
    
    def render(self, surface):
        for x in range(0, 1920, self.size[0]):
            for y in range(0, 1080, self.size[1]):
                surface.blit(self.file, (x, y))