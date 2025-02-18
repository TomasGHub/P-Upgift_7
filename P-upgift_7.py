import os

class Train:
    def __init__(self, row, column):
        self.plats_info = [{"seatnumber":n+1, "status":False, "name":None } for n in range(row * column)]
        self.row = row
        self.column = column
        
    def printwagon(self):
        for row in range(self.row):
            print("|", end=" ")
            
            for column in range(self.column):
                plats = row * self.column + column * 1
                
                if plats > len(self.plats_info):
                    print("   ", end=" ")
                
                else:
                    print(f"{plats:02d}", end="  ")
            print("|")
            
            # lägger en gång_väg i mellan rad index 1 som är på rad 2
            if row == 1:
                gångväg_bredd = self.column * 4 + 1
                print("|" + "-" * gångväg_bredd + "|")
                print("|" + "TYST AVD".center(gångväg_bredd) + "|")
                print("|" + "-" * gångväg_bredd + "|")
    

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