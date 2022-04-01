class Movie:
    
    def __init__(self, title, genre, rating, hosts):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.hosts = hosts

    def update_rating(self, new_rating):
        self.rating = new_rating