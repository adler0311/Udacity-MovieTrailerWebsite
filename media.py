import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    valid_ratings = ["G", "PG", "PG-13", "R"]
    #initialize Movie class
    def __init__(self, title="noname", duration="00:00", storyline="Storyline",
                poster_image="www.wikimedia.com", trailer_youtube="www.youtube.com"):

        #define class variables
        self.title = title
        self.duration = duration
        self.storyline=  storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #define class method show_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)