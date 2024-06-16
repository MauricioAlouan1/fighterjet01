from panda3d.core import CardMaker, TextureStage

def load_terrain(app):
    terrain_texture = app.loader.loadTexture("models/desert_sand_dunes_rocks.dds")

    cm = CardMaker("terrain")
    cm.setFrame(-50, 50, -50, 50)
    terrain = app.render.attachNewNode(cm.generate())
    terrain.setPos(0, 0, 1)
    terrain.setHpr(0, -90, 0)
    terrain.setTexture(terrain_texture, 1)
    terrain.setTexScale(TextureStage.getDefault(), 10, 10)

    return terrain
