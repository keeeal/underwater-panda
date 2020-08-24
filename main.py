
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

config_dir = 'config'
loadPrcFile(os.path.join(config_dir, 'config.prc'))

class Game(ShowBase):
    def __init__(self):
        super().__init__()

        self.keys_pressed = {}
        controls = os.path.join(config_dir, 'controls.json')
        self.load_controls(controls)

        self.taskMgr.add(self.loop, 'loop')

    def set_key(self, key, value):
        self.keys_pressed[key] = value

    def load_controls(self, controls):
        with open(controls) as f:
            controls = json.load(f)

        for key, action in controls.items():
            self.accept(key, self.set_key, [key, True])
            self.accept(key + '-up', self.set_key, [key, False])

    def loop(self, task):

        return task.cont

if __name__ == '__main__':
    game = Game()
    game.run()
