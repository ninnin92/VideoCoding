#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import ui_ageindays # designerで作ったUIを変換してソースとして読み込み
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox


class MainWindow(QMainWindow, ui_ageindays.Ui_AgeInDays):

    # 初期設定
    def __init__(self):
        super(MainWindow, self).__init__()
        # setupUi というメソッドが定義されているので実行する
        # これで設置したウィジェットなどがインスタンス化される
        self.setupUi(self)
        # 継承したので self.名前 でアクセスできる
        self.setWindowTitle("VideoCoding v1.0") # ウィンドウタイトル


if __name__ == '__main__':
    app = QApplication(sys.argv) # キー入力やイベント発生などのリソース管理
    main_window = MainWindow()   # ウィンドウインスタンスの作成
    main_window.show()           # ウィンドウの描画
    sys.exit(app.exec_())        # アプリのイベントループが終わったらプログラムを修了