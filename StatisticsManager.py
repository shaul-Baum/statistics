import Statistics
from ReadData import ReadData
from Cleanr import Cleanr
from Examination import Examination

class StatisticsManager:
    def __init__(self):
        self.probability_table = {}
        self.class_labels = []
        self.loaded = False
        self.search =""
        self.search_column = None
        self.a = None
        self.data_test = None
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
            print("Error loading dataset:", e)
        return self.probability_table, self.class_labels

    def _load_data(self, csv):
        if not csv:
            csv = "phishing.csv"
            if not self.search:
                self.search = "class"
        if not self.search:
            print("")
            return "", ""
        b = ReadData(csv)
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
        self.a = Statistics.NaiveBayesHelper(train_data, self.search)
        self.probability_table, self.class_labels= self.a.calculate_probabilities()
        # self.columns_z =[i for i in self.columns]
    def evaluate_model(self,probability_table,class_labels):
        test = Examination(probability_table,self.data_test, self.search,class_labels)
        level_test = test.examination()
        print("Data loaded successfully.")
        print(f"Model confidence level at this stage: {level_test}%")
        return level_test


