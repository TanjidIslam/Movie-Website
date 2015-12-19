import media
from fresh_tomatoes import open_movies_page

# define instances for movies

# Dead Poets Society
DeadPoet = media.Movie(
        "Dead Poets Society",
        "Story about an English teacher, who uses unorthodox methods of reaching out to students and inspiring them" +
        " to love poems and seize life..",
        "http://www.samandscout.com/wp-content/uploads/2014/08/large_hCPvO18vdEntYPH05sZnfUBAIid.jpg",
        "https://www.youtube.com/watch?v=wrBk780aOis")

# The Dark Knight
DarkKnight = media.Movie(
        "The Dark Knight",
        "Story of a superhero Batman and the master mind criminal joker..",
        "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v7_aa.jpg",
        "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

# List all the movie instances
movies = [DeadPoet,
          DarkKnight]

# Create/Recreate web content with the list of movies
open_movies_page(movies)
