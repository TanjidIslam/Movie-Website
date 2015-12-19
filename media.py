import webbrowser

class Movie(object):
    '''
    A movie object that contains movie title, movie trailer
    '''

    def __init__(self, title, storyline, poster_img, trailer_url):
        '''
        Movie initialization
        '''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        '''
        '''
        webbrowser.open(self.trailer_youtube_url)
