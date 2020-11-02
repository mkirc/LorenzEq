
class LorenzSystem:

    def __init__(self):

        self.sigma = 10.
        self.rho = 28.
        self.beta = 8. / 3.

        self.initVector = [0.1, 0, 0]
    
    
    def computeState(self, stateVector, t):
        x, y, z = stateVector
        a = self.sigma * (y - x)
        b = x * (self.rho - z) - y
        c = x * y - self.beta * z

        return [a, b, c]
