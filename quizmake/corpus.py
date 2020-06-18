"""
Corpus module (for storing variable data)
"""


class Corpus:
    """
    Corpus class
    """

    def __init__(self):
        self.amazing = "lmao"

    def speak(self):
        """
        This will just make the Corpus speak its assigned word
        """
        print(self.amazing)

    def yell(self):
        """
        This will also just make the corpus say random stuff
        """
        print(self.amazing + " LMaO")


def corn():
    """
    Returns the string 'corn' lmao
    """
    return "corn"
