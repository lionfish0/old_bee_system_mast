import time

class PhotoResult():
    def __init__(self,img,direction,flash):
        print("Creating Photo Result Object")
        print("Flash: ")
        print(flash)
        print("Direction: ")
        print(direction)
        self.img = img
        self.flash = flash
        self.direction = direction
        self.time = time.time()
        print("Time: ")
        print(self.time)
    def as_list(self):
        return [self.flash,self.direction,self.time,self.img]
