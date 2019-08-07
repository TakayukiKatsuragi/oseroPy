import Board

test=Board.Board()
test.print_board()
player=test.black
while 1:
  print("x?")
  x=input()
  x=int(x)
  print("y?")
  y=input()
  y=int(y)
  n=test.reverse(player,y,x,False)
  print("reverse="+str(n))
  if n>0:
    if player==test.black:player=test.white
    else :player=test.black
    test.print_board()

  else:
    print("No put!!")
