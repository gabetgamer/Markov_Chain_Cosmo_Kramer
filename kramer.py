from random import randint as r
from time import sleep

defaut_img = "kramer_markov.jpg"

class kramer:
    def __init__(self):
        # Goes to:       Kramer, Jerry, Newman, LandLord, Elaine   # From:
        self.matrix =  [[0.3,    0.6,   0.09,   .01,      0     ], # Kramer
                        [0.5,    0.1,   0.2,    0,        0.2   ], # Jerry
                        [0,      0.8,   0.2,    0,        0     ], # Newman
                        [1,      0,     0,      0,        0     ], # LandLord
                        [0,      1,     0,      0,        0     ]] # Elaine

        self.names = ["Kramer's", "Jerry's", "Newman's", "Landlord's", "Elaine's"]
        self.stopped = 1
        self.kramer_loc = 0
        self.kramer_loc_old = 0
        self.pixel_index = [[450, 130], [85, 250], [230, 460], [600, 480], [740, 300]]
        self.pixel_loc = [450, 130]

        self.image = defaut_img
        self.change_img_flag = 0
        self.text = ''
        self.chance = 0
        self.at_apt = ''
        self.dest_apt = ''

    def where_does_krammer_go(self):
        temp = 0
        random = r(1, 100) / 100
        for i in range(len(self.matrix[self.kramer_loc])):
            temp += self.matrix[self.kramer_loc][i]
            temp = round(temp, 2)

            if random <= temp:
                return i
            
        return 0
    
    def on_the_move(self):
        image = defaut_img
        dest = self.pixel_index[self.kramer_loc]
        loc = self.pixel_loc
        print(dest, self.pixel_loc)
        if [round(self.pixel_loc[0]), round(self.pixel_loc[1])] != dest:
            self.pixel_loc[0] += (dest[0] - loc[0]) / 50
            self.pixel_loc[1] += (dest[1] - loc[1]) / 50
        else:
            self.change_img_flag = 1


    def play_sound(self):
        print('the image should change')
        self.image = 'cosmo.png'

    def run(self):
        kramer_was = self.kramer_loc
        self.kramer_loc_old = kramer_was
        self.kramer_loc = self.where_does_krammer_go()
        kramer_chance = self.matrix[kramer_was][self.kramer_loc]
        self.chance = kramer_chance
        self.at_apt = self.names[kramer_was]
        self.dest_apt = self.names[self.kramer_loc]
        self.text = f"Krammers going from {self.names[kramer_was]} apartment to {self.names[self.kramer_loc]} apartment (P = {kramer_chance})"

        self.stopped = 0
        
        sleep(1)