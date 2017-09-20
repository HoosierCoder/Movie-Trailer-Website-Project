#FILE   : entertainment_center.py
#CREATOR: Dennis Johns
#CLASS  : Full Stack Web Developer
#PROJECT: Movie Trailer Website

#Fresh Tomatoes import contains display capabilities for the webpage
import fresh_tomatoes

#Media import contains the Movie class
import media

#Create Movie objects for each movie to be displayed
#Each movie object is created with a title, Synopsis, movie poster link,
#and youtube link for the movie trailer
the_natural = media.Movie("The Natural",
                          "Roy Hobbs:  The greatest there ever was",
                          "https://upload.wikimedia.org/wikipedia/en/8/8c/The_Natural_%281984_film%29_poster.jpg", # NOQA
                          "https://www.youtube.com/watch?v=LMnwlNm6xWs",
                          "Robert Redford, Glenn Close"
                          )
bull_durham = media.Movie("Bull Durham",
                          "A major league love story in a minor league town",
                          "https://upload.wikimedia.org/wikipedia/en/e/ef/Bull_Durham_film_poster.jpg", # NOQA
                          "https://www.youtube.com/watch?v=dnJFndf-Krg",
                          "Kevin Costner, Susan Sarandon"
                          )

elf = media.Movie("Elf", "The elf who saved Christmas",
                  "https://upload.wikimedia.org/wikipedia/en/d/df/Elf_movie.jpg", # NOQA
                  "https://www.youtube.com/watch?v=gW9wRNqQ_P8",
                  "Will Ferrell, Zooey Deschanel"
                  )

avengers = media.Movie("The Avengers",
                       "Earth's Mightest Hero's",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", # NOQA
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                       "Robert Downey, Jr, Chris Evans"
                       )

justice_league = media.Movie("Justice League",
                             "Gods Among Us",
                             "https://upload.wikimedia.org/wikipedia/en/3/31/Justice_League_film_poster.jpg", # NOQA
                             "https://www.youtube.com/watch?v=h-Nzxn9qiSg",
                             "Ben Affleck, Gal Gadot"
                             )
                             

die_hard = media.Movie("Die Hard",
                             "Twelve Terrorists. One Cop",
                             "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg", # NOQA
                             "https://www.youtube.com/watch?v=2TQ-pOvI6Xo",
                             "Bruce Willis, Alan Rickman"
                             )

#This would be the main section of the program.
#first we create a list of the movies created that will be displayed.
#Then fresh_tomatoes is utilized to display the movies and to give the
#user the chance to view each movies trailer

movies = [the_natural,
          bull_durham,
          elf,
          avengers,
          justice_league,
          die_hard]

fresh_tomatoes.open_movies_page(movies)
