# -*- coding: utf-8 -*-
"""
Testing non Pygame modules


"""

import pyglet as pyg
import os

#%% Variables
#%%% Path
path_home = "C:"
path_user = "Users"
path_name = "mrkno"
path_project = "Autochess"
path_image = "images"

path_user = os.path.join(path_home,path_user)
path_name = os.path.join(path_user, path_name)
path_project = os.path.join(path_name, path_project)
path_image = os.path.join(path_project, path_image)

print(path_image)

#%% Initialize

window = pyg.window.Window()

image = pyg.resource.image(os.path.join(path_image, "bb1.jpg"))
# DOESNT WORK FOR SOME REASON????

# label = pyg.text.Label("Hello world",
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    # label.draw()
    image.blit(0, 0)

pyg.app.run()

#%% Playground
