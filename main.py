import raylib.defines
from settings import *
from engine import Engine
import cProfile


class App:
    ray.set_trace_log_level(ray.LOG_ERROR)
    ray.set_config_flags(ray.FLAG_MSAA_4X_HINT)
    #
    ray.init_window(WIN_WIDTH, WIN_HEIGHT, 'Quake Level Engine')
    # ray.set_target_fps(600)
    #
    ray.hide_cursor()
    ray.disable_cursor()

    def __init__(self):
        self.dt = 0.0
        self.engine = Engine(app=self)

    def run(self):
        while not ray.window_should_close():
            self.dt = ray.get_frame_time()
            self.engine.update()
            self.engine.draw()
        #
        ray.close_window()


if __name__ == '__main__':
    app = App()
    app.run()
