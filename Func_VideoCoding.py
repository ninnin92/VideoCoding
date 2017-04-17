#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import ui_videocoding  # designerで作ったUIを変換してソースとして読み込み
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox


class MainWindow(QMainWindow, ui_videocoding.Ui_MainWindow):
    # 初期設定
    def __init__(self):
        super(MainWindow, self).__init__()
        # setupUi というメソッドが定義されているので実行する
        # これで設置したウィジェットなどがインスタンス化される
        self.setupUi(self)
        # 継承したので self.名前 でアクセスできる
        self.setWindowTitle("VideoCoding v0.1") # ウィンドウタイトル

    def keyPressEvent(self, Event):
        print(Event.key())
        if Event.key() == Qt.Key_Space:
            print('Space pressed')
        else:
            super().keyPressEvent(Event)

    def keyReleaseEvent(self, Event):
        print(Event.key())
        if Event.key() == Qt.Key_Space:
            print('Space Released')
        else:
            super().keyReleaseEvent(Event)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # キー入力やイベント発生などのリソース管理
    main_window = MainWindow()    # ウィンドウインスタンスの作成
    main_window.show()            # ウィンドウの描画
    sys.exit(app.exec_())         # アプリのイベントループが終わったらプログラムを修了
