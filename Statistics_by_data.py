class StatisticsByData:
    def __init__(self,dataStatistics):
        self.probability_table =dataStatistics
        self.label_scores = {}
        self.most_likely_label = ""
        self.class_labels =[i for i in self.probability_table if i != "__total__"]
        self.highest_score = 0
    def check_feature_value(self,feature_value,feature_name):
        return feature_value in self.probability_table[self.class_labels[0]][feature_name]
    def update_statistics(self, feature_name, feature_value):
        try:
            for label in self.class_labels:
                if label not in self.label_scores:
                    self.label_scores[label] = 1
                self.label_scores[label] *= self.probability_table[label][feature_name][feature_value]
        except:
            try:
                feature_value = float(feature_value)
            except:
                pass
            try:
                feature_value = int(feature_value)
            except:
                pass
            for label in self.class_labels:
                if label not in self.label_scores:
                    self.label_scores[label] = 1
                self.label_scores[label] *= self.probability_table[label][feature_name][feature_value]
    def get_valid_feature_name(self):
        while True:
            print("Available features (columns):", self.columns_z)
            feature_name = input("Enter feature name (column): ")
            if feature_name is not None:
                return feature_name
            print("Feature not found. Please try again.")
    def get_valid_feature_value(self,feature_name):
        while True:
            print("Available values for this feature:", list(self.a.values_of_column(feature_name)))
            feature_value = input("Enter feature value: ")
            try:
                feature_value = int(feature_value)
            except:
                pass
            if feature_value is not None:
                return feature_value
            print("Value not found in feature. Please try again.")
    def run_classification(self):
        continue_input = "yes"
        while continue_input.lower() in ["yes", "y"]:
            feature_name = self.get_valid_feature_name()
            feature_value = self.get_valid_feature_value(feature_name)
            self.update_statistics(feature_name, feature_value)
            continue_input = input("Do you want to enter another feature? (yes/no): ")
    def process_feature_pairs(self,feature_input_list):
        for i in range(0,len(feature_input_list),2):
            feature_name =feature_input_list[i]
            feature_value = feature_input_list[i+1]
            # if not self.check_feature_name(feature_name):
            #     return False
            if not self.check_feature_value(feature_value,feature_name):
                return False
            self.update_statistics(feature_name, feature_value)
            # self.columns_z.remove(feature_name)
        return True
    def finalize_scores(self):
        self.most_likely_label = max(self.label_scores, key=self.label_scores.get)
        self.highest_score = self.label_scores[self.most_likely_label]
        return self.most_likely_label, self.highest_score
    def input_statistics(self,feature_input_list):
        self.label_scores = {label: 1 for label in self.class_labels}
        if not feature_input_list or not self.process_feature_pairs(feature_input_list):
            self.run_classification()
            print("Data entry is complete. Calculation is in progress.")
        self.finalize_scores()
        return self.most_likely_label
    def print_percentage(self):
        print(f"\nMost probable classification: {self.most_likely_label} (probability score: {self.highest_score})")
        print("\nProbability scores for all classes:")
        for label in self.label_scores:
            print(f"\t{label}: {self.label_scores[label]}")
