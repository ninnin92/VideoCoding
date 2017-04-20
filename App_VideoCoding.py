#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import datetime as dt
import ui_videocoding  # designerで作ったUIを変換してソースとして読み込み
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, ui_videocoding.Ui_VideoCoding):
    # 関数設定
    switch = False         # on = True, off = Falseで設定　初期設定はOFF
    durations_list = []    # 複数回ボタンが押された時のdurationの仮置き場
    press_time = 0         # 時間の計測用
    release_time = 0       # 時間の計測用
    pressing = False       # コーディングが始まってからボタンを押したかどうか
    ID = None              # 動画情報入力
    Trial = None           # 動画情報入力
    fp = None              # 出力用csvファイル

    # 初期設定
    def __init__(self):
        super(MainWindow, self).__init__()
        # setupUi というメソッドが定義されているので実行する
        # これで設置したウィジェットなどがインスタンス化される
        self.setupUi(self)
        # 継承したので self.名前 でアクセスできる
        self.setWindowTitle("VideoCoding v1.0")  # ウィンドウタイトル
        # ボタンを押す操作と関数のひも付け
        self.pushButton_Start.clicked.connect(self.start_switch)
        self.pushButton_Stop.clicked.connect(self.stop_switch)
        # 最初はoffを押せないようにしておく
        self.pushButton_Stop.setEnabled(False)
        # textBrowserにindexを追加
        self.textBrowser.append("[  ID  ] [  Trial  ] [  Duration  ]")

        # 出力用のcsvファイルを作成
        app_time = "{0:%y-%m-%d_%H-%M-%S}".format(dt.datetime.now())  # formatを使うと一行で済んで便利
        self.fp = open("VideoCoding_" + app_time + ".csv", "w")       # csvファイルを起動時刻で作成

        # csvファイルにindexを書き込む
        index = ["Name_ID", "Trial", "Duration"]
        for i in index:
            self.fp.write("%s," % i)  # リストから1つずつ書き込み
        self.fp.write("\n")
        self.fp.flush()

    # Qwidgetの組み込みの関数：ボタンを押した時
    def keyPressEvent(self, event):
        # コーディングを開始しているときだけ反応
        if self.switch:
            # ボタンを押したことを明示的に表現
            self.pressing = True
            self.label_Now.setText("Press")
            # 長押しのリピートを解除
            if event.isAutoRepeat():
                return
            # ctrlキーを押した瞬間の時間を計測
            if event.key() == Qt.Key_Control:
                self.press_time = time.time()  # keyを押した時点での時刻
                # print('Ctrl Pressed')
            else:
                pass
        else:
            pass

    # Qwidgetの組み込みの関数：ボタンを離した時
    def keyReleaseEvent(self, event):
        # コーディングを開始しているときだけ反応
        if self.switch and self.pressing:
            # ボタン押しの状態
            self.label_Now.setText("Release")
            # 長押しのリピートを解除
            if event.isAutoRepeat():
                return
            # ctrlキーを押した瞬間の時間を計測
            if event.key() == Qt.Key_Control:
                self.release_time = time.time()  # keyを離した時点での時刻
                self.time_count()                # keyを押していた間の時間を計算
                # print(self.press_time)
                # print(self.release_time)
                # print('Ctrl Released' + str(self.time_count()))
            else:
                pass
        else:
            pass

    # ボタンを離した時刻からボタンを押した時の時刻を引き算、リストに追加
    def time_count(self):
        duration = self.release_time - self.press_time
        self.durations_list.append(duration)
        return duration

    # コーディングを開始する
    def start_switch(self):
        # on/off の切り替え
        self.switch = True
        # onのときはボタンの色を変える、連続では押せないようにする
        self.pushButton_Start.setStyleSheet('background-color: #FFD25A')
        self.pushButton_Start.setEnabled(False)
        # Stopを押せるようにする
        self.pushButton_Stop.setEnabled(True)
        # onのときは入力できないようにしておく
        self.lineEdit_ID.setEnabled(False)
        self.lineEdit_Trial.setEnabled(False)

        # Name,Trialに入力があるかチェック（なければNoneを追加）
        if len(self.lineEdit_ID.text()) > 0:
            self.ID = self.lineEdit_ID.text()
        else:
            self.ID = "None"

        if len(self.lineEdit_Trial.text()) > 0:
            self.Trial = self.lineEdit_Trial.text()
        else:
            self.Trial = "None"

        # print(self.switch)
        # print(self.press_time)
        # print(self.release_time)

    # コーディングを終了する
    def stop_switch(self):
        # on/off の切り替え
        self.switch = False
        # offになったらボタンの色を戻す,　また押せるように
        self.pushButton_Start.setStyleSheet('background-color: None')
        self.pushButton_Start.setEnabled(True)
        # Stopを押せないようにする
        self.pushButton_Stop.setEnabled(False)
        # offのときは入力できるようにしておく
        self.lineEdit_ID.setEnabled(True)
        self.lineEdit_Trial.setEnabled(True)

        # 合計の時間を計算
        total_duration = sum(self.durations_list)
        # TextBrowserに動画情報と計測時間を追加する
        self.textBrowser.append(self.ID + ",  " + self.Trial + ",  " + str(total_duration))

        # csvファイルに解析結果を書き込み
        for x in [str(self.ID), str(self.Trial), str(total_duration)]:
            self.fp.write("%s," % x)  # リストから1つずつ書き込み
        self.fp.write("\n")
        self.fp.flush()

        # print(self.switch)
        # print(self.durations_list)
        # print(total_duration)

        # 初期化
        self.press_time = 0
        self.release_time = 0
        self.durations_list = []


if __name__ == '__main__':
    app = QApplication(sys.argv)  # キー入力やイベント発生などのリソース管理
    main_window = MainWindow()    # ウィンドウインスタンスの作成
    main_window.show()            # ウィンドウの描画
    sys.exit(app.exec_())         # アプリのイベントループが終わったらプログラムを修了
