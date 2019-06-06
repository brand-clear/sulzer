

from os.path import join as osjoin
from os.path import dirname


class Path:
    ROOT = dirname(__file__)
    DATA = osjoin(ROOT, 'data')
    IMAGES = osjoin(DATA, 'images')
    PROJECTS_FOLDER = 'L:\\Division2\\PROJECTS FOLDER'


class Icon:
    ROOT = Path.IMAGES
    SULZER = osjoin(ROOT, 'sulzer.png')
    OPEN = osjoin(ROOT, 'open.png')
    SAVE = osjoin(ROOT, 'save.png')
    REFRESH = osjoin(ROOT, 'refresh.png')
    USERS = osjoin(ROOT, 'users.png')



