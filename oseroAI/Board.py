#オセロのボードを定義する
class Board:

    #初期化関数
    #ボードが作られたときに呼ばれる
    def __init__(self):
        #ボードの各マスの状態を定義
        #空き
        self.none='.'
        #白駒
        self.white='W'
        #黒駒
        self.black='B'
        #10*10盤面を定義
        #※中1~8だけを使う。0,9は常にnoneにする(配列外参照を簡単に防ぐため)
        self.stone=[[self.none for i in range(10)] for j in range(10)]
        #初期配置
        self.stone[4][4]=self.white
        self.stone[5][5]=self.white
        self.stone[4][5]=self.black
        self.stone[5][4]=self.black

    #ボードの中身を表示する
    def print_board(self):
        for i in range(1,9,1):
            for j in range(1,8,1):
                #end==""で改行しなくなるらしい
                print(self.stone[i][j],end="")
            print(self.stone[i][8])

    #反転処理をする
    #flagがtrueのときは反転するが、falseの時は反転せずにひっくり返せる個数だけ返す
    def reverse(self,player,y,x,flag):
        #numにはそこに石をおいたときにひっくり返る個数が入る
        num=0
        #敵の駒(自分の駒=playerではない色)
        enemy=""
        #置こうとしている場所が空き地でないなら0を返す
        if self.stone[y][x]!=self.none:return 0
        if player==self.black:enemy=self.white
        else: enemy=self.black
        #置こうとしている場所から八方向で1マス以内に敵の駒があるか調べる
        for yt in range(-1,2,1):
            for xt in range(-1,2,1):
                #敵の駒があった!!
                if self.stone[y+yt][x+xt]==enemy:
                    #自分の駒か、空き地にぶつかるまで探索
                    for i in range(1,20,1):
                        #空き地ならひっくり返せない
                        if self.stone[y+yt*i][x+xt*i]==self.none:break
                        #自分の駒ならひっくり返せる
                        if self.stone[y+yt*i][x+xt*i]==player:
                            #反転処理のフラグが立っているなら、置こうとしてた場所に駒を置く
                            if flag==True:self.stone[y][x]=player
                            #もう一度、ループを回して反転処理と個数カウントする
                            for j in range(1,20,1):
                                if self.stone[y+yt*j][x+xt*j]==player: break
                                if flag==True:self.stone[y+yt*j][x+xt*j]=player
                                num+=1
        #1個でもひっくり返せる=置こうとしていた場所に石が置ける
        #なので、カウントを増やす
        if num>=1:num+=1
        return num

    #着手可能数の検索
    def putnum(self,player):
        num=0
        for y in range(1,9,1):
            for x in range(1,9,1):
                #一個でもひっくり返せるならカウントする
                if self.reverse(player,y,x,False)>=1:num+=1
        return num

    #石の数を数える
    def stonenum(self,player):
        num=0
        for y in range(1,9,1):
            for x in range(1,9,1):
                if self.stone[y][x]==player:num+=1
        return num
