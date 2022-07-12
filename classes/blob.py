class Blob:
    def __init__(self, is_altruist):
        self.is_altruist = is_altruist
    
    def assexual_reproduction(self):
        return [Blob(self.is_altruist),Blob(self.is_altruist),Blob(self.is_altruist)]