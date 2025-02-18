import os

class Train:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
    def printwagon(self):
        for x in range(self.row):
            for y in range(self.column):
                print(1, end=" ")
            print()
    

class BookingSystem:
    FILENAME = "bokings.txt" #Filen där vi sparar sparade platser
    KVITTO_FILE = "kvitto.txt" #Filen där vi sparar kvitto
    
    def __init__(self):
        self.user_bokings = set() #Håller kåll på bokade platser atomatiskt undviker dubleter
        self.senaste_bokningar = [] # Håller kåll på bokningar under aktuel körning
        self.ladda_bokningar() #Ladda tidigare bokningar vid start
        

    
class Meny:
    pass
    
        
#Skapa objekt
train = Train( 4, 8)
train.printwagon()