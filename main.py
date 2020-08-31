
import os, sys, json

from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

from utils.procgen import *
from utils.light import *

config_dir = 'config'
config = os.path.join(config_dir, 'config.prc')
controls = os.path.join(config_dir, 'controls.json')
loadPrcFile(config)


class Game(ShowBase):
    def __init__(self):
        super().__init__()

        node = cube((1, 2, 3))

        node_path = self.render.attach_new_node(node)

        # TODO: Orient triangles correctly and render one side
        node_path.set_two_sided(True)

        self.camera.set_pos(8, 8, 8)
        self.camera.look_at(0, 0, 0)

        # TODO: How do the default camera controls work?
        self.disable_mouse()

        # create some lights
        ambient = ambient_light((.3, .3, .3, 1))
        ambient = self.render.attach_new_node(ambient)
        self.render.set_light(ambient)

        directional = directional_light((1, 1, 1, 1), (-1, -2, -3))
        directional = self.render.attach_new_node(directional)
        self.render.set_light(directional)

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
