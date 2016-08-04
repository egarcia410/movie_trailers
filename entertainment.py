# Import two files from same folder location
# fresh_tomatoes renders html outlook and creates movie tiles
import fresh_tomatoes
# media imports Movie class
import media

#Below are 6 instances of the Movie class
#Each Movie instance has a Title, Storyline, Poster Image, and Youtube Link
godfather = media.Movie("The Godfather",
						# Storyline is divided onto two lines
						"The aging patriarch of an organized crime dynasty transfers"
						" control of his clandestine empire to his reluctant son",
						"http://i.ebayimg.com/00/s/NTAwWDMzMw==/z/jsgAAOxyBvZTVkHv/$_3.JPG?set_id=2",
						"https://www.youtube.com/watch?v=5DO-nDW43Ik")

shawshank = media.Movie("Shawshank Redemption",
					# Storyline is divided onto two lines
					"Two imprisoned men bond over a number of years,"
					" finding solace and eventual redemption through acts of common decency",
					"https://www.movieposter.com/posters/archive/main/42/MPW-21321",
					"https://www.youtube.com/watch?v=6hB3S9bIaco")

schindler = media.Movie("Schindler's List",
					# Storyline is divided onto two lines
					"In Poland during World War II, Oskar Schindler gradually becomes"
					" concerned for his Jewish workforce after witnessing their persecution by the Nazis",
					"https://i.jeded.com/i/schindlers-list.22323.jpg",
					"https://www.youtube.com/watch?v=JdRGC-w9syA")

raging_bull = media.Movie("Raging Bull",
					# Storyline is divided onto two lines
					"An emotionally self-destructive boxer's journey through life, as the"
					" violence and temper that leads him to the top in the ring destroys his life outside it",
					"https://upload.wikimedia.org/wikipedia/en/5/5f/Raging_Bull_poster.jpg",
					"https://www.youtube.com/watch?v=mHhzOM4gBIA")

casablanca = media.Movie("Casablanca",
					# Storyline is divided onto two lines
					"In Casablanca, Morocco in December 1941, a cynical American"
					" expatriate meets a former lover, with unforeseen complications",
					"https://www.movieposter.com/posters/archive/main/27/MPW-13851",
					"https://www.youtube.com/watch?v=a2MnKebNlRo")

citizen_kane = media.Movie("Citizen Kane",
					# Storyline is divided onto two lines
					"Following the death of a publishing tycoon, news reporters"
					" scramble to discover the meaning of his final utterance",
					"https://67.media.tumblr.com/d2a1fdd5ff50697c6292bdbf6444568a/tumblr_mm43onrWgy1s80h8lo1_500.png",
					"https://www.youtube.com/watch?v=8dxh3lwdOFw")

#The 6 Movies instances are placed inside an array called "movies"
movies = [godfather, shawshank, schindler, raging_bull, casablanca, citizen_kane]

fresh_tomatoes.open_movies_page(movies)
