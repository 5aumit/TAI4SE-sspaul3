__author__ = 'Jager'
from char import Character

class Rouge (Character):

    def special_attack1(self, opponent, hitdamage_callback, specatt_callback):
        pass    # hook method

    def special_attack2(self, opponent, hitdamage_callback, specatt_callback):
        pass    # hook method

    def heal(self, target):
        pass    # hook method

    def regen_resource(self):
        pass    # hook method


    def full_resource(self):
        pass