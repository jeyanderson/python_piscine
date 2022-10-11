from multiprocessing.sharedctypes import Value


class GotCharacter:
    def __init__(self,first_name,is_alive):
        def input_error(err_code):
            if err_code==0:
                raise ValueError("erorr: corrupted first_name provided.")
            else:
                print("error: corrupted is_alive provided, set to default(True).")
                self.is_alive=True
        self.name=first_name if isinstance(first_name,str)and first_name.isalpha()else input_error(0)
        self.is_alive=is_alive if isinstance(is_alive,bool)else input_error(1)

class Stark(GotCharacter):
    '''A class representing the Stark family. Or when bad things happen to good people.'''
    def __init__(self,first_name=None,is_alive=True):
        super().__init__(first_name=first_name,is_alive=is_alive)
        self.family_house="Stark"
        self.house_words="Winter is Coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive=False
