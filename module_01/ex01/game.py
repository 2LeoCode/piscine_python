class GotCharacter:
    def __init__(self, first_name: str, is_alive: bool = True):
        assert (
            isinstance(first_name, str) and first_name
        ), "first_name must be a non-empty string"
        assert isinstance(is_alive, bool), "is_alive must be a boolean"
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """
    A class representing the Stark family.
    Or when bad things happen to good people.
    """
    family_name = "Stark"

    def __init__(self, first_name: str = None, is_alive: bool = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
