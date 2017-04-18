#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import ui_videocoding  # designerで作ったUIを変換してソースとして読み込み
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox


class MainWindow(QMainWindow, ui_videocoding.Ui_VideoCoding):
    # 初期設定
    switch = -1

    def __init__(self):
        super(MainWindow, self).__init__()
        # setupUi というメソッドが定義されているので実行する
        # これで設置したウィジェットなどがインスタンス化される
        self.setupUi(self)
        # 継承したので self.名前 でアクセスできる
        self.setWindowTitle("VideoCoding v0.1")  # ウィンドウタイトル
        # 操作と関数のひも付け
        self.pushButton_start.clicked.connect(self.start_switch)
        self.pushButton_stop.clicked.connect(self.stop_switch)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            global press_time         # 関数外で使うのでグローバルに
            press_time = time.time()  # keyを押した時点での時刻
            print('Ctrl pressed!')
        else:
            pass

    def keyReleaseEvent(self, event):
        # 長押しのリピートを解除
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_Control:
            global release_time         # 関数外で使うのでグローバルに
            release_time = time.time()  # keyを離した時点での時刻
            print('Ctrl Released' + str(self.time_count()))
        else:
            pass

    def time_count(self):
        duration = release_time - press_time
        return duration

    def start_switch(self):
        self.switch = self.switch * -1
        print(self.switch)

    def stop_switch(self):
        self.switch = self.switch * -1
        print(self.switch)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # キー入力やイベント発生などのリソース管理
    main_window = MainWindow()    # ウィンドウインスタンスの作成
    main_window.show()            # ウィンドウの描画
    sys.exit(app.exec_())         # アプリのイベントループが終わったらプログラムを修了
