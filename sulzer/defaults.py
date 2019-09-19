

from os.path import join as osjoin
from os.path import dirname


class Path:
    ROOT = dirname(__file__)
    DATA = osjoin(ROOT, 'data')
    IMAGES = osjoin(DATA, 'images')
    VAULT = 'C:\\Vault Workspace\\Draft\\OEM'
    PROJECTS_FOLDER = 'L:\\Division2\\PROJECTS FOLDER'
    AX_PICS = 'T:\\pictures\\Axapta'
    REVERSE_ENGINEERING = 'Q:\\DRAFT\\_REVERSE ENGINEERING'
    CAD_FORMS = 'L:\\Division2\\DCC\\1-CAD-FORMS\\Balance'
    QC_MODELS = 'Q:\\Quality Control\\quality_controller\\data\\cad models'
    DXF_GEN = 'L:\\Division2\\MACHINE\\Mazak Programs\\DXFs'
    DXF_TOOL = 'L:\\Division2\\MACHINE\\Mazak Programs\\DXFs Root Tools'


class Icon:
    ROOT = Path.IMAGES
    SULZER = osjoin(ROOT, 'sulzer.png')
    OPEN = osjoin(ROOT, 'open.png')
    SAVE = osjoin(ROOT, 'save.png')
    REFRESH = osjoin(ROOT, 'refresh.png')
    USERS = osjoin(ROOT, 'users.png')



