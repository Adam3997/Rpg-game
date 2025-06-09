

class Destiny_movements():
    """This is the class that holds predetermined movements
    along with the time between those movements."""

    def __init__(self,**kwargs):
        """This will hold an arbitrary number of movements
        and time between movements."""

        self.destiny_movements = kwargs

        self.destiny_movements_list = kwargs['movements']
        self.destiny_timing_list = kwargs['timing']
        self.directions = kwargs['directions']

        self.movement_counter = 0
        