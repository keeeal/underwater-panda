
import os, sys, json

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

config_dir = 'config'
config = os.path.join(config_dir, 'config.prc')
controls = os.path.join(config_dir, 'controls.json')
loadPrcFile(config)

class Game(ShowBase):
    def __init__(self):
        super().__init__()

        self.load_controls(controls)

        self.taskMgr.add(self.loop, 'loop')

    def load_controls(self, controls: str):
        with open(controls) as f:
            controls = json.load(f)

        self.actions = {a: False for a in controls.values()}

        def set_action(action: str, value: bool):
            self.actions[action] = value

        for key, action in controls.items():
            self.accept(key, set_action, [action, True])
            self.accept(key + '-up', set_action, [action, False])

    def loop(self, task):
        for action, value in self.actions.items():
            if value:
                print(action)

        if self.actions['exit']:
            sys.exit()

        return task.cont

if __name__ == '__main__':
    game = Game()
    game.run()
