class player:
  def play(self):
    print("The player is playing cricket.")
class Batsman(player):
  def play(self):
    print("The batsman is playing")
class Bowler(player):
  def play(self):
    print("The bowler is playing")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()