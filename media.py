class Movie(object):
    '''
    A movie object that contains movie title, movie trailer
    '''
    
    def __init__(self, title, poster_img, trailer_url, storyline, review):
        '''
        Movie initialization
        '''
        self.title = title
        self.poster_image_url = poster_img
        self.trailer_youtube_id = trailer_url
        self.storyline = storyline
        self.review = review

