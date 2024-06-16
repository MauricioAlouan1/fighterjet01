def setup_controls(app):
    keys = {
        "left": False,
        "right": False,
        "up": False,
        "down": False,
        "forward": False,
        "backward": False,
        "increase_speed": False,
        "decrease_speed": False,
        "camera_up": False,
        "camera_down": False,
        "camera_left": False,
        "camera_right": False,
        "zoom_in": False,
        "zoom_out": False,
    }

    def set_key(key, value):
        keys[key] = value

    app.accept("arrow_left", set_key, ["left", True])
    app.accept("arrow_right", set_key, ["right", True])
    app.accept("arrow_up", set_key, ["up", True])
    app.accept("arrow_down", set_key, ["down", True])
    app.accept("'", set_key, ["forward", True])
    app.accept("/", set_key, ["backward", True])
    app.accept(";", set_key, ["increase_speed", True])
    app.accept("p", set_key, ["decrease_speed", True])
    app.accept("w", set_key, ["camera_up", True])
    app.accept("s", set_key, ["camera_down", True])
    app.accept("a", set_key, ["camera_left", True])
    app.accept("d", set_key, ["camera_right", True])
    app.accept("q", set_key, ["zoom_out", True])
    app.accept("e", set_key, ["zoom_in", True])
    app.accept("arrow_left-up", set_key, ["left", False])
    app.accept("arrow_right-up", set_key, ["right", False])
    app.accept("arrow_up-up", set_key, ["up", False])
    app.accept("arrow_down-up", set_key, ["down", False])
    app.accept("'-up", set_key, ["forward", False])
    app.accept("/-up", set_key, ["backward", False])
    app.accept(";up", set_key, ["increase_speed", False])
    app.accept("p-up", set_key, ["decrease_speed", False])
    app.accept("w-up", set_key, ["camera_up", False])
    app.accept("s-up", set_key, ["camera_down", False])
    app.accept("a-up", set_key, ["camera_left", False])
    app.accept("d-up", set_key, ["camera_right", False])
    app.accept("q-up", set_key, ["zoom_out", False])
    app.accept("e-up", set_key, ["zoom_in", False])

    return keys
