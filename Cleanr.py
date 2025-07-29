import pandas as pd
from Logger import Logger
class Cleanr:
    def __init__(self,dataframe,clean=None):
        self.logger =Logger()
        self.dataframe = dataframe
        self.clean =clean
        self.dataframe = self.clean_table()

    def clean_table(self):
        self.dataframe.dropna(inplace=True)
        # self.dataframe = self.dataframe[~(self.dataframe == 0).any(axis=1)]
        if isinstance(self.clean, list):
            for i in self.clean:
                try:
                    self.dataframe.drop(i, axis=1, inplace=True)
                except:
                    pass
        elif isinstance(self.clean, str):
            try:
                self.dataframe.drop(self.clean, axis=1, inplace=True)
            except:
                pass
        self.logger.log(f"data is clean")

        return self.dataframe
    def gat_dataframe(self):
        return self.dataframe



