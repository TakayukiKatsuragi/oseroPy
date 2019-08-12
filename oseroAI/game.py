import Board
import player
import random

#テストコード
test1=Board.Board()
test1.print_board()
test2=player.player()
passnum=0

while 1:
    if test1.putnum(test2.turn)==0:
        print("PASS!!")
        test2.change()
        passnum+=1
        if passnum==2:break
        continue
    else: passnum=0

    print("turn->",end="")
    test2.print_player()
    while 1:
        x=random.randint(1,8)
        y=random.randint(1,8)
        if test1.reverse(test2.turn,y,x,False)>0:break
    print("x?",end="")
    print(x)
    print("y?",end="")
    print(y)
    n=test1.reverse(test2.turn,y,x,True)
    print("reverse="+str(n))
    if n>0:
        test2.change()
        test1.print_board()
    else:
        print("No put!!")

numb=test1.stonenum(test1.black)
numw=test1.stonenum(test1.white)
print ("B="+str(numb)+"VS"+str(numw)+"=W")
if numb>numw:print("Win!! Black")
elif numb==numw:print("Draw")
else :print("Win!! White")
