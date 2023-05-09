import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,path):
        """ 
        Read dictionary file -> dict 
        & print number of words registered 
        """   
        dict = open(path)
        self.words = self.parse(dict)
        print(f"Read {len(self.words)} words successfully.")
    
    def parse(self, dict):
        """Parse dictionary file -> list of words."""

        return [w.strip() for w in dict]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

    
