import media
from fresh_tomatoes import open_movies_page

# define instances for movies
'''
Movie format:
    Title
    Storyline
    Poster Image URL
    Trailer URL from YouTube
'''

# Dead Poets Society movie instance
deadPoet = media.Movie(
        "Dead Poets Society",
        "Story about an English teacher, who uses unorthodox methods of " +
        "reaching out to students and inspiring them" +
        " to love poems and seize life..",
        "http://www.samandscout.com/wp-content/uploads/2014/08/" +
        "large_hCPvO18vdEntYPH05sZnfUBAIid.jpg",
        "https://www.youtube.com/watch?v=wrBk780aOis",
        ["Robin Williams", "Ethan Hawke", "Josh Chalres", "Gale Hansen"])

# The Dark Knight movie instance
darkKnight = media.Movie(
        "The Dark Knight",
        "Story of a superhero Batman and the master mind criminal joker..",
        "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v7_aa"
        ".jpg",
        "https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
        ["Christian Bale", "Heath Ledger", "Gary Oldman", "Morgan Freeman"])

# Conjuring movie instance
conjuring = media.Movie(
        "The Conjuring",
        "Based on a true-story, a couple who are paranormal investigator and "
        + "demonologists, investigate on Perron Family..",
        "http://resizing.flixster.com/9L9x-cvmFJF_K14OlJyEu9frubU=/800x1200"
        "/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/39/11173945_ori.jpg",
        "https://www.youtube.com/watch?v=k10ETZ41q5o",
        ["Vera Farmiga", "Patrick Wilson", "Lilli Taylor", "Ron Livingston"])

# The Shawshank Redemption movie instance
theShawshank = media.Movie(
        "The Shawshank Redemption",
        "Story about a man who is imprisoned for crimes he claimed to not "
        "commit",
        "http://i.jeded.com/i/the-shawshank-redemption.18663.jpg",
        "https://www.youtube.com/watch?v=6hB3S9bIaco",
        ["Morgan Freeman", "Tim Robbins", "William Sadler", "Bob Gunton"])

# 12 Angry Men movie instance
twelveAngry = media.Movie(
        "12 Angry Men",
        "Following the closing arguments in a murder trial, " +
        "the 12 members of the jury must deliberate, with" +
        " a guilty verdict meaning death for the accused, an inner-city teen..",
        "http://d1zlh37f1ep3tj.cloudfront.net/wp/wblob/54592E651337D2/14FB/" +
        "2258BB/VhKL4g5oOWGtY05rs4NFJA/12angrymen.gif",
        "https://www.youtube.com/watch?v=A7CBKT0PWFA",
        ["Henry Fonda", "Lee Cobb", "Martin Balsam", "Jack Klugman"])

# Harry Potter movie instance
harryPotter = media.Movie(
        "Harry Potter",
        "About a young wizard whose parents were murdered by evil black " +
        "magic..",
        "http://www.harrypottermovieposters.com/wp-content/uploads/2013/08/" +
        "harry-potter-and-the-order-of-the-phoenix-movie-poster-style-h.jpg",
        "https://www.youtube.com/watch?v=K1KPcXRMMo4",
        ["Emma Watson", "Daniel Radcliffe", "Gary Oldman", "Rupert Grint"])

# List all the movie instances
movies = [deadPoet,
          darkKnight,
          conjuring,
          theShawshank,
          twelveAngry,
          harryPotter]

# Create/Recreate web content with the list of movies
open_movies_page(movies)
