from Trainer import Trainer
from Logger import Logger
from Loader import Loader
from Cleanr import Cleanr
from Examination import Examination
import numpy as np
class TrainerManager:
    def __init__(self):
        self.probability_table = {}
        self.class_labels = []
        self.loaded = False
        self.search =""
        self.search_column = None
        self.a = None
        self.data_test = None
        self.logger =Logger()
    def convert_keys(self,obj):
        if isinstance(obj, dict):
            new_dict = {}
            for key, value in obj.items():
                # המרה של המפתח ל־int אם הוא np.int64
                if isinstance(key, np.integer):
                    key = int(key)
                new_dict[key] = self.convert_keys(value)
            return new_dict
        elif isinstance(obj, list):
            return [self.convert_keys(item) for item in obj]
        else:
            return obj

    def read_csv(self,clean = ["id","Index"], csv=None, search=None):
        self.search = search
        try:
            dataframe= self._load_data(csv)
            dataframe = self._cleanr(dataframe,clean)
            dataframe = dataframe.sample(frac=1, random_state=42).reset_index(drop=True)
            train_data = self._split_data(dataframe)
            self._train_model(train_data)
            self.loaded = True

        except Exception as e:
            self.logger.log(f"Error loading dataset: {e}","ERROR")
            print("Error loading dataset:", e)
        self.probability_table = self.convert_keys(self.probability_table)
        return self.probability_table

    def _load_data(self, csv):
        if not csv:
            csv = "phishing.csv"
            if not self.search:
                self.search = "class"
        if not self.search:
            print("")
            return "", ""
        b = Loader(csv)
        dataframe = b.gat_dataframe()
        return dataframe
    def _cleanr(self,dataframe,clean):
        a = Cleanr(dataframe,clean)
        dataframe = a.gat_dataframe()
        return dataframe
    def _split_data(self, dataframe):
        split_index = int(0.7 * len(dataframe))
        train_data = dataframe[:split_index]
        self.data_test = dataframe[split_index:]
        return train_data

    def _train_model(self, train_data):
        self.a = Trainer(train_data, self.search)
        self.probability_table, self.class_labels= self.a.calculate_probabilities()
    def evaluate_model(self,probability_table):
        test = Examination(probability_table,self.data_test, self.search)
        level_test = test.examination()
        self.logger.log("Data loaded successfully.")
        self.logger.log(f"Model confidence level at this stage: {level_test}%","METRIC")
        print("Data loaded successfully.")
        print(f"Model confidence level at this stage: {level_test}%")
        return level_test


