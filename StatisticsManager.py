import Statistics
from Reading_and_handling_data import ReadingAndHandingData
from Examination import Examination

class StatisticsManager:
    def __init__(self):
        self.probability_table = {}
        self.class_labels = []
        self.label_scores = {}
        self.loaded = False
        self.search =""
        self.search_column = None
        self.highest_score = 0
        self.most_likely_label = ""
        self.columns =[]
        self.columns_z = []
        self.a = None
        self.data_test = None
    def read_csv(self, csv=None, search=None):
        self.search = search
        try:
            dataframe= self._load_data(csv)
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
        b = ReadingAndHandingData(csv, ["id", "Index"])
        dataframe = b.gat_dataframe()
        dataframe = dataframe.sample(frac=1, random_state=42).reset_index(drop=True)
        return dataframe

    def _split_data(self, dataframe):
        split_index = int(0.7 * len(dataframe))
        train_data = dataframe[:split_index]
        self.data_test = dataframe[split_index:]
        return train_data

    def _train_model(self, train_data):
        self.a = Statistics.NaiveBayesHelper(train_data, self.search)
        self.probability_table, self.class_labels, self.columns = self.a.calculate_probabilities()
        self.columns_z =[i for i in self.columns]
    def evaluate_model(self,ui):
        test = Examination(self.data_test, self.search,ui)
        level_test = test.examination()
        print("Data loaded successfully.")
        print(f"Model confidence level at this stage: {level_test}%")
        return level_test
    def update_statistics(self, feature_name, feature_value):
        for label in self.class_labels:
            if label not in self.label_scores:
                self.label_scores[label] = 1
            self.label_scores[label] *= self.probability_table[label][feature_name][feature_value]
    def finalize_scores(self):
        self.most_likely_label = max(self.label_scores, key=self.label_scores.get)
        self.highest_score = self.label_scores[self.most_likely_label]
        return self.most_likely_label, self.highest_score
    def Percentage_display(self):
        for i in self.label_scores:
            self.label_scores[i] = int(self.label_scores[i] *100)


