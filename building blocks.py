class Block(object):
    
    """docstring"""
    def __init__(self,list):
        """Constructor"""
        self.w = int(list[0])
        self.l = int(list[1])
        self.h = int(list[2])
    
    def get_width(self):
        return self.w
    
    def get_length(self):
        return self.l

    def get_height(self):
        return self.h
    
    def get_volume(self):
        return (self.w*self.l*self.h)
    
    def get_surface_area(self):
        return (2*(self.w*self.l+self.l*self.h+self.h*self.w))