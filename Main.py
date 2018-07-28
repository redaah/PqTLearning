import sys
import Rendering
from PyQt5.QtWidgets import  QApplication



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rendering.Board()
    sys.exit(app.exec_())