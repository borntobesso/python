class GotCharacter:
    def __init__(self, first_name, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Martell(GotCharacter):
    """A class representing the Martells, residing in the desert region of Westeros."""
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Martell"
        self.house_words = "Unbowed, Unbent, Unbroken"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False