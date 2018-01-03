#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import (QLabel, QGridLayout, QLineEdit, QWidget, QToolTip,
                             QPushButton, QApplication, QDesktopWidget)
from PyQt5 import QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        distance = QLabel('Distance(1-9,0.5):')
        distance_edit = QLineEdit('1')
        # distance_edit.setText('1')
        grid.addWidget(distance, 1, 0)
        grid.addWidget(distance_edit, 1, 1)

        btn = QPushButton('Jump!', self)
        btn.clicked.connect(self.do_msk)
        # self.connect(btn, QtCore.SIGNAL('clicked()'), self.do_msk)

        grid.addWidget(btn, 2, 1)

        self.setLayout(grid)

        # QToolTip.setFont(QFont('SansSerif', 10))
        #
        # self.setToolTip('This is a <b>QWidget</b> widget')
        #
        # btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # #
        # btn.resize(btn.sizeHint())
        # btn.move(10, 10)

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Jump to 999')
        # self.resize(250, 150)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def do_msk(self):
        k = self.distance_edit.text()
        os.system("adb shell monkey -f sdcard/Documents/m7 1")
        os.system(k)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
