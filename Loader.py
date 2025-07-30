import pandas as pd
from Logger import Logger
class Loader:
    def __init__(self,csv):
        self.logger =Logger()
        self.logger.log(f"name of file: {csv}")
        try:
            self.dataframe = pd.read_csv(csv)
            self.logger.log("loading dataset")
            self.loaded = True
            # self.dataframe = self.clean_table(clean)
        except Exception as e:
            self.loaded = False
            print("Error loading dataset:", e)
            self.logger.log(f"Error loading dataset:, {e}")
    def gat_dataframe(self):
        if self.loaded:
            return self.dataframe
        else:
            return None
