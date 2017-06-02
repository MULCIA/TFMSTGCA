class Genome(object):
    
    def __init__(self, sg, igi, ea, ei, gi):
        self.sg = sg
        self.igi = igi
        self.ea = ea
        self.ei = ei
        self.gi = gi

    def mutations(self):
        return sum(vars(self).values())

    def __str__(self):
        return str(self.sg) + str(self.igi) + str(self.ea) + str(self.ei) + str(self.gi)