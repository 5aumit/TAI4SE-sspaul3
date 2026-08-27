class Balloon(object):
    def __init__(self, color, size, shape):
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False
        self.working = True

    def inflate(self):
        if self.working:
            self.inflated = True
        else:
            print "You exploded this balloon. Idiot."

    def explode(self):
        self.inflated = False
        self.working = False
        print "BANG!"

    def deflate(self):
        self.inflated = False

    
class BigBalloon(Balloon):
    def __init__(self, color, shape):
        super(Balloon, self).__init__(color, 'Big', shape)
        
balloon = BigBalloon('green', 'round')
balloon.paint('red')

bigBalloon.print_info(self.color, self.size, self.shape)