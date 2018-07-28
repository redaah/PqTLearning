import sys
import Rendering


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rendering.Example()
    sys.exit(app.exec_())