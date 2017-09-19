#FILE   : media.py
#CREATOR: Dennis Johns
#CLASS  : Full Stack Web Developer
#PROJECT: Movie Trailer Website

import webbrowser

#Class definition for Movie()
#Contains the title of the movie, a movie storyline,
#a link to the movie poster, and a line to the movie trailer
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_lead_actors):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.lead_actors = movie_lead_actors
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
