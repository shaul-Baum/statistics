import Statistics
import Reading_and_handling_data
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
            csv ="data_for_NB_buys_computer.csv"
            if not search:
                search ="Buy_Computer"
        if not search:
            print("")
            return ""
        try:
            b = Reading_and_handling_data.ReadingAndHandingData(csv, "id")
            dataframe =b.gat_dataframe()
            self.a = Statistics.NaiveBayesHelper(dataframe,search)
            self.probability_table, self.class_labels,self.columns = self.a.calculate_probabilities()
            print("Data loaded successfully.")
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


