import pandas as pd
class ReadingAndHandingData:
    def __init__(self,csv,clean=None):
        try:
            self.dataframe = pd.read_csv(csv)
            self.loaded = True
            self.dataframe = self.clean_table(clean)
        except Exception as e:
            self.loaded = False
            print("Error loading dataset:", e)
    def clean_table(self ,clean=None):
        # self.dataframe.dropna(inplace=True)
        if clean is not None:
            self.dataframe.drop(clean, axis=1, inplace=True)
        return self.dataframe
    def gat_dataframe(self):
        if self.loaded:
            return self.dataframe
        else:
            return None
