

import os
import sys
from PyQt4 import QtGui
from pyqtauto.widgets import ExceptionMessageBox

from extract import Extract



class Logic(object):

    @staticmethod
    def open_path(path):
        """Open a file or directory via its parent process.

        Parameters
        ----------
        path : str
            Absolute path to file or directory.

        Raises
        ------
        OSError
            `path` was not found. This could be 1) a network issue, or 2) a
            reference to a file or directory that does not exist.
        TypeError
            `path` was not of type ``str``.

        Examples
        --------
        >>> Logic.open_path('f')
        Traceback (most recent call last):
            ...
        WindowsError: [Error 2] The system cannot find the file specified: 'f'

        >>> Logic.open_path(None)
        Traceback (most recent call last):
            ...
        TypeError: coercing to Unicode: need string or buffer, NoneType found

        """
        os.startfile(path)


class Sos(object):

    @staticmethod
    def open_path(path):
        """Open a file or directory via its parent process.
        
        Parameters
        ----------
        path : str
            Absolute path to file or directory.
        """
        try:
            Logic.open_path(path)
        except (OSError, TypeError) as error:
            ExceptionMessageBox(error).exec_()


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=2)
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
    Sos.open_path('c')


  
