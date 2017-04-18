#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import ui_videocoding  # designerで作ったUIを変換してソースとして読み込み
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
        self.setWindowTitle("VideoCoding v0.1")  # ウィンドウタイトル

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            print('Ctrl pressed!')
        else:
            pass

    def keyReleaseEvent(self, event):
        # 長押しのリピートを解除
        if event.isAutoRepeat():
            return

        if event.key() == Qt.Key_Control:
            print('Ctrl Released')
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)  # キー入力やイベント発生などのリソース管理
    main_window = MainWindow()    # ウィンドウインスタンスの作成
    main_window.show()            # ウィンドウの描画
    sys.exit(app.exec_())         # アプリのイベントループが終わったらプログラムを修了
