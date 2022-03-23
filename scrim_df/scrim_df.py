import pandas as pd

class scrim_data:
    def __init__(self,file_name):
        self.file_name = file_name

        self.load_data()

    def load_data(self):
        self.scrim_df = pd.read_csv(self.file_name)

    