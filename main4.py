class player:
  def play(self):
    print("The Player is Playing Cricket. ")
class Batsman(player):
  def play(self):
    print("The Bats man is Batting. ")
class Bowler(player):
  def play(self):
    print("The Bowler is Bowling. ")
batsman =Batsman()
bowler = Bowler()
batsman.play()
bowler.play()