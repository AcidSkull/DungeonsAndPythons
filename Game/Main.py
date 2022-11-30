from Mechanics.Engine import Engine

class Main():

    def __init__(self, width: int, height: int):
        self.engine = Engine(width=width, height=height)

    def run(self):
        self.engine.start()
        


if __name__ == '__main__':

    m = Main(1920, 1080)
    m.run()