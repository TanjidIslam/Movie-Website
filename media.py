import webbrowser


class Movie():
    '''
    A movie object that contains movie title, movie trailer,
    storyline and poster
    '''

    # Class Variable for rating
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_img, trailer_url, stars):
        '''
        Initialize instances for Movie object
        Args:
            title (str): Movie title
            storyline (str): Movie storyline
            poster_img (str): URL of the Movie poster
            trailer_url (str): URL of the Movie trailer
            stars (list->str): List of stars
        '''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_url
        self.stars = stars

    def show_trailer(self):
        '''
        Open a browser with the trailer URL associated
        with the instances of the Movie object
        '''
        webbrowser.open(self.trailer_youtube_url)
