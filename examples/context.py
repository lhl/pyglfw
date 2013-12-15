# coding=utf-8

from pyglfw import *

if __name__ == '__main__':
    init()

    for vermaj, vermin, iscore in [ (3,3,True), (3,2,True), (3,1,False), (3,0,False) ]:
        try:
            Window.hint()
            Window.hint(context_version=(vermaj,vermin))
            if iscore:
                Window.hint(forward_compat=True)
                Window.hint(opengl_profile=Window.CORE_PROFILE)
            w = Window(800, 600, "Тест: %s" % api_version_string())
            break
        except (PlatformError, VersionUnavailableError, ValueError) as e:
            print("%s.%s %s: %s" % (vermaj, vermin, 'CORE' if iscore else '', e))
    else:
        raise SystemExit("Proper OpenGL 3.x context not found")

    print(w.context_version)

    w.make_current()

    k = w.keys

    while not w.should_close:
        w.swap_buffers()
        poll_events()

        if k.escape:
            w.should_close = True

    terminate()
