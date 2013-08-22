class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy Birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])			

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])				
						
songs = [happy_bday, bulls_on_parade]

print "What song do you want to see?"
print "1. Happy Birthday"
print "2. Bulls on parade."
answer = raw_input(">")
if answer == "1":
	choice = happy_bday
elif answer == "2":
	choice = bulls_on_parade

choice.sing_me_a_song()		