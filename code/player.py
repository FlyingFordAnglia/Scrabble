class player(object):

    def __init__(self, name, score=0, rack=None):
        self.name = name
        self.score = score
        if rack is None:
            self.rack = []
        else:
            self.rack = rack
