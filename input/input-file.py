class config_file():
    def __init__(self,title=''):
        self.title=title
        self.xc=''
        self.spin=''
        self.calculation_options=[]
        self.charge=''
        self.defaults=''
        self.ouput_options=[]

class geometry_file():
    def __init__(self,comment=''):
        self.comment=comment
        self.species=[]
        self.position=[]
        self.lattice=[]
        self.velocity=[]
    def self.add_atom(element,xyz,velocity=None):
        self.species.append[element]
        self.position.append[xyz]
        if velocity:
            self.velocity.append[velocity]
    
    


