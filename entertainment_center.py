import media, fresh_tomatoes

#making movies objects
suicide_squad = media.Movie("Suicide Squad","160", "Storyline",
                        "http://www.suicidesquad.com/assets/images/cast/downloads/harley_quinn.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=CmRih_VtVAs")
seoul_station = media.Movie("Seoul Station","180", "Storyline",
                     "http://movie.phinf.naver.net/20160801_91/1470018364274qGN2m_JPEG/movie_image.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=cid6GoEvY0o")
Before_sunset = media.Movie("Before Sunset","100", "Storyline",
                             "http://www.impawards.com/2004/posters/before_sunset.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=oI3UuneLcyU")
doctor_strange = media.Movie("Doctor Strange","120", "Storyline",
                          "http://static.srcdn.com/slir/w691-h1023-q90-c691:1023/wp-content/uploads/Doctor-Strange-Comic-Con-Poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=HSzx-zryEgM")
resident_evil = media.Movie("Resident Evil Final Chapter","90", "Storyline",
                                "https://www.trailers.tube/wp-content/uploads/2016/08/RESIDENT-EVIL-THE-FINAL-CHAPTER-movie-poster-480x720.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=jbtmW3ydOkU")
fast_and_furious = media.Movie("Fast and Furious 8","80", "Storyline",
                           "http://i3.mirror.co.uk/incoming/article7189885.ece/ALTERNATES/s615b/Vin-Diesel-Releases-First-Fast-8-Picture.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=tuHTt_QVDu0")

# gather the objects and put into a movies list to use as variables of the open_movies_page method.
movies = [suicide_squad, seoul_station, Before_sunset, doctor_strange, resident_evil, fast_and_furious]
fresh_tomatoes.open_movies_page(movies)
