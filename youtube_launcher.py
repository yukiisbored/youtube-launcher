#!/usr/bin/env python

from urllib.parse import urlparse

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QProcess


app = QApplication([])


class Youtube(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.textbox = QLineEdit('https://www.youtube.com/watch?v=fjuJgqrZSIk')
        layout.addWidget(self.textbox)

        button = QPushButton('Watch')
        button.clicked.connect(self.__watch)
        layout.addWidget(button)

        self.setLayout(layout)

        self.setWindowTitle("YouTube Launcher");
        self.resize(512, 100)

        self.show()

    def __watch(self):
        url = urlparse(self.textbox.text())

        if (url.netloc.lower() in ('www.youtube.com', 'youtube.com') and
            url.path == '/watch' and url.query.startswith('v=') and
            len(url.query) > 2):
            QProcess().startDetached('mpv', [url.geturl()])
            app.exit()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("The URL is not a valid YouTube video URL")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()


def main():
    window = Youtube()
    app.exec()


if __name__ == '__main__':
    main()
