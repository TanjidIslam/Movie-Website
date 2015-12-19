import media
from fresh_tomatoes import open_movies_page
# define instances for movies

# Dead Poets Society
title1 = "Dead Poets Society"
storyline1 = "Story about an English teacher, who uses unorthodox methods of reaching out to students and " \
             "inspiring them to discover their love to poetry and seize the day.."
image_url1 = "http://www.samandscout.com/wp-content/uploads/2014/08/large_hCPvO18vdEntYPH05sZnfUBAIid.jpg"
trailer_url1 = "https://www.youtube.com/watch?v=wrBk780aOis"
DeadPoet = media.Movie(title1, storyline1, image_url1, trailer_url1)

# Dead Poets Society
title2 = "The Dark Knight"
storyline2 = "Story of a superhero Batman and the master mind criminal joker.."
image_url2 = "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v7_aa.jpg"
trailer_url2 = "https://www.youtube.com/watch?v=_PZpmTj1Q8Q"
DarkKnight = media.Movie(title2, storyline2, image_url2, trailer_url2)

movies = [DeadPoet,
          DarkKnight]

open_movies_page(movies)
