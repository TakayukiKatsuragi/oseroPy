import Board

#手番を格納するクラスを作成
class player:
    #初期化
    def __init__(self):
        #手番の色に変数を定義
        tmpBoard=Board.Board()
        self.black=tmpBoard.black
        self.white=tmpBoard.white
        #初手は黒から
        self.turn=self.black

    #手番を変更する
    def change(self):
        if self.turn==self.black:self.turn=self.white
        else :self.turn=self.black

    #手番を出力する
    def print_player(self):
        if self.turn==self.black:print("Black")
        else :print("White")
