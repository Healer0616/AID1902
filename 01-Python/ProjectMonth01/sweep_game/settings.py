class Settings:
    def __init__(self):
        self.length = 9
        self.width = 9
        self.homb_number = 10
        self.coord = (0,0)
        self.dict_count = {}

class Core:
    def __init__(self,set):
        self.list_screen = [[0 for i in range(set,length)]]