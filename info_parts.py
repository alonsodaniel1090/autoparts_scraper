class InfoParts:
    '''
    The purpose of this class is to create
    objects with all the needed information
    to create a database to keep
    track of all the objects and its information.
    '''

    def __init__(self, title, price, href):
        self.title = title
        self.price = price
        self.href = href
    
    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_link(self):
        return self.href 
