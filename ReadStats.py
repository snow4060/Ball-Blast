class GetStats:
    def __init__(self):
        self.stats = open("Stats.txt", "r+")

    def get_score(self):
        score = int(self.stats.readlines()[0][7:]) #first line is the score in the form of "score: x"
        self.stats.seek(0)
        return score

    def get_level(self):
        level = int(self.stats.readlines()[1][7:]) #second line is the level in the form of "level: x"
        self.stats.seek(0)
        return level 

    def edit(self, new_score, new_level):
        new_stats = ["score: " + str(new_score) + "\n", "level: " + str(new_level) + "\n"] #formating the stats so that it can be read
        self.stats.writelines(new_stats)
        self.stats.seek(0)

    def close(self):
        self.stats.close()
        
