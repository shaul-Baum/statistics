import pandas as pd
import numpy as np

class NaiveBayesHelper:
    def __init__(self,dataframe,search):
        self.class_counts_table = {}
        self.counts = pd.Series(dtype=int)
        self.values =[]
        self.columns = []
        self.search = search
        self.dataframe = dataframe
    def handle_zeros(self,NumberTimes):
        for i in NumberTimes.keys():
            if i == "__total__":
                continue
            if 0 in NumberTimes[i].values():
                NumberTimes["__total__"] += 1
                for i in NumberTimes.keys():
                    if i == "__total__":
                        continue
                    for y in NumberTimes[i]:
                        NumberTimes[i][y] += 1
                break
        return NumberTimes
    def validate_search_column(self):
            try:
                self.counts = self.dataframe[self.search].value_counts()
                return True
            except Exception as e:
                print("Error loading dataset:", e,"not in data frame.")
                return False
    def handle_zeros_in_table(self):
        for value in self.values:
            if value == "__total__":
                continue
            self.class_counts_table[value] = self.handle_zeros(self.class_counts_table[value])

    def normalize_counts_to_probabilities(self):
        for i in self.class_counts_table.keys():
            if i == "__total__":

                continue
            # total_tabl = self.class_counts_table["__total__"]
            total = self.class_counts_table[i]["__total__"]
            # a = total/total_tabl
            for y in self.class_counts_table[i].keys():
                if y == "__total__":
                    continue
                for v in self.class_counts_table[i][y].keys():
                    self.class_counts_table[i][y][v] = self.class_counts_table[i][y][v] / total #*a


    def build_class_count_table(self):
        self.class_counts_table = {value: {"__total__": int(self.counts.get(value, 0))} for value in self.values}
        self.class_counts_table["__total__"] = sum(self.class_counts_table[value]["__total__"] for value in self.values)
        for column in self.columns:
            grouped_feature_counts = self.dataframe.groupby([self.search, column]).size()
            for value in self.values:
                if column not in self.class_counts_table[value]:
                    self.class_counts_table[value][column] = {}
                for val_in_col in self.dataframe[column].dropna().unique():
                    count = grouped_feature_counts.get((value, val_in_col), 0)
                    self.class_counts_table[value][column][val_in_col] = int(count)
    def values_of_column(self,column_name):
        values = self.dataframe[column_name].dropna().unique()
        cleaned = [int(v) if isinstance(v, (np.integer, int)) else v for v in values]
        return cleaned
    def calculate_probabilities(self):
        self.columns = [col for col in self.dataframe.columns if col not in ["id","Index", self.search]]
        if not self.validate_search_column():
            return ""
        self.values = self.values_of_column(self.search)
        self.build_class_count_table()
        self.handle_zeros_in_table()
        self.normalize_counts_to_probabilities()
        return self.class_counts_table,self.values,self.columns