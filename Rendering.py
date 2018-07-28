from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QMessageBox,QDesktopWidget,QMainWindow)
from PyQt5.QtGui import QFont


class Board(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #Features
        self.AddButton('boton','This is a <b>QPushButton</b> widget')
        self.AddToolTip('This is a <b>QWidget</b> widget')

        #Properties
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.center()
        self.statusBar().showMessage('Ready')

        #Showing
        self.show()

    def AddToolTip(self,text):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip(text)

    def AddButton(self,ButtonText,ToolTipText):
        btn = QPushButton(ButtonText, self)
        btn.setToolTip(ToolTipText)
        btn.resize(btn.sizeHint())
        btn.move(50,50)

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())