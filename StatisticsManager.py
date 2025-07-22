import Statistics
from Reading_and_handling_data import ReadingAndHandingData
# from Examination import Examination
class StatisticsManager:
    def __init__(self):
        self.probability_table = {}
        self.class_labels = []
        self.label_scores = {}
        self.loaded = False
        self.search_column = None
        self.highest_score = 0
        self.most_likely_label = ""
        self.columns =[]
        self.a = None
    def read_csv(self,csv=None,search=None):
        if not csv:
            csv ="phishing.csv"
            if not search:
                search ="class"
        if not search:
            print("")
            return ""
        try:
            b = ReadingAndHandingData(csv, ["id","Index"])
            dataframe =b.gat_dataframe()
            dataframe = dataframe.sample(frac=1, random_state=42).reset_index(drop=True)
            split_index = int(0.7 * len(dataframe))
            # יצירת דאטא פריים לאימון ולבדיקה
            train_df = dataframe[:split_index]
            test_df = dataframe[split_index:]
            self.a = Statistics.NaiveBayesHelper(train_df,search)
            self.probability_table, self.class_labels,self.columns = self.a.calculate_probabilities()
            # test = Examination(test_df,search,self.columns)
            # realness = test.gat_realness()
            # print(f"Data loaded successfully. {realness}")
            # print(self.probability_table)
            self.loaded = True
        except Exception as e:
            print("Error loading dataset:", e)
        return self.probability_table, self.class_labels

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


