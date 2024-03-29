import webbrowser

class Movie():
    # class for representing a movie
    __name__ = "Movie House"
    # Attributes:title,storyline,poster_image and trailer

    def __init__(
            self, movie_title, movie_storyline,
            poster_image, trailer_youtube):
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # opens trailer in a web browser
        webbrowser.open(self.trailer_youtube_url)
