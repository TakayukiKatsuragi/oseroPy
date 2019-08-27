import os

class testAI:
    def __init__(self):
        #ボードの点数データ
        self.boardScore=[[0 for i in range(10)] for j in range(10)]

        #trueなら読み込んだファイル情報を出力する
        self.fileWriteMode=True

        #ボードのマスごとの点数を記載したファイルのパス
        boardValueName="./data/boardValue.dat"

        #ファイルがなければerrorflagをfalseにする
        self.errorflag=os.path.exists(boardValueName)
        #ファイルがないなら処理終了
        if not self.errorflag:
            print(boardValueName+"が存在しない")
            return

        #ファイルを開いて読み込む
        fileopen = open(boardValueName, "r")
        filedata = fileopen.read()
        #閉じる
        fileopen.close()

        #いい感じに数字ごとに区切る
        filedataSp=filedata.split()
        #10*10=100のデータ数でなければエラー
        if len(filedataSp)!=100:
            print(boardValueName+"は100データから成り立つ("+str(len(filedataSp))+")")
            self.errorflag=False
            return

        #読み込んだデータを格納する
        for i in range(0,10,1):
            for j in range(0,10,1):
                self.boardScore[i][j]=filedataSp[j+i*10]

        if self.fileWriteMode:
            #ボード点数の中身を表示する
            for i in range(1,9,1):
                for j in range(1,8,1):
                    print(self.boardScore[i][j],end="")
                print(self.boardScore[i][8])
