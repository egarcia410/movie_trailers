import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poser_image, 
				trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poser_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
