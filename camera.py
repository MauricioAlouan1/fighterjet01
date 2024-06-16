from panda3d.core import LVector3

def setup_camera(app):
    initial_offset = LVector3(0, -10, 10)
    app.camera.setPos(app.jet.getX(), app.jet.getY() + initial_offset.getY(), app.jet.getZ() + initial_offset.getZ())
    app.camera.lookAt(app.jet)
    return initial_offset

def update_camera(app):
    if app.keys["camera_up"]:
        app.camera_offset.setZ(app.camera_offset.getZ() + app.camera_step)
    if app.keys["camera_down"]:
        app.camera_offset.setZ(app.camera_offset.getZ() - app.camera_step)
    if app.keys["camera_left"]:
        app.camera_offset.setX(app.camera_offset.getX() - app.camera_step)
    if app.keys["camera_right"]:
        app.camera_offset.setX(app.camera_offset.getX() + app.camera_step)
    if app.keys["zoom_in"]:
        app.camera_offset.setY(app.camera_offset.getY() + app.zoom_step)
    if app.keys["zoom_out"]:
        app.camera_offset.setY(app.camera_offset.getY() - app.zoom_step)

    app.camera.setPos(app.jet.getPos() + app.camera_offset)
    app.camera.lookAt(app.jet)
