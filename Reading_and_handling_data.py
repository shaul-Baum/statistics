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
        self.dataframe.dropna(inplace=True)
        # self.dataframe = self.dataframe[~(self.dataframe == 0).any(axis=1)]
        if isinstance(clean, list):
            for i in  clean:
                try:
                    self.dataframe.drop(i, axis=1, inplace=True)
                except:
                    pass
        elif isinstance(clean, str):
            try:
                self.dataframe.drop(clean, axis=1, inplace=True)
            except:
                pass
        return self.dataframe
    def gat_dataframe(self):
        if self.loaded:
            return self.dataframe
        else:
            return None
