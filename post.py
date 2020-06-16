import uuid
import time

class Post: 

    def __init__(self, user_id, type, quantity, location, price):
        self.user_id = user_id
        self.crop = type
        self.quantity = quantity
        self.location = location
        self.price = price

    def setCrop(self, crop):
        self.crop = crop
        return

    def setQuantity(self, quantity):
        self.quantity = quantity
        return

    def setLocation(self, location):
        self.location = location
        return

    def setPrice(self, price):
        self.price = price
        return 
