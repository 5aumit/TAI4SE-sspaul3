'''
Created on 8 Oct 2017

@author: matt
'''

class Line(object):
    '''
    classdocs
    '''
    
    
    def __init__(self, dot_1, dot_2):
        '''
        Constructor
        '''
        self.dot_1 = dot_1
        self.dot_2 = dot_2    
    
    def __str__(self):
        return "Line: \n\t %s \n\t %s" % (self.dot_1, self.dot_2)
    
    def lenght(self):
        return ( ((self.dot_1.x-self.dot_2.x)**2) 
                 + ((self.dot_1.y-self.dot_2.y)**2) 
                 + ((self.dot_1.z-self.dot_2.z)**2))**0.5