import webbrowser

class Movie(object):
    '''
    A movie object that contains movie title, movie trailer, storyline and poster
    '''

    def __init__(self, title, storyline, poster_img, trailer_url):
        '''
        Initialize instances for Movie object
        Args:
            title (str): Movie title
            storyline (str): Movie storyline
            poster_img (str): URL of the Movie poster
            trailer_url (str): URL of the Movie trailer
        '''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        '''
        Open a browser with the trailer URL associated
        with the instances of the Movie object
        '''
        webbrowser.open(self.trailer_youtube_url)
