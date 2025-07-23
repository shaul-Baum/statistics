from StatisticsManager import StatisticsManager


class UserInteraction(StatisticsManager):
    def __init__(self):
        super().__init__()
    def check_feature_name(self, feature_name):
        return feature_name in self.columns_z
    def check_feature_value(self,feature_value,feature_name):
        return feature_value in self.probability_table[self.class_labels[0]][feature_name]
    def get_valid_feature_name(self):
        while True:
            print("Available features (columns):", self.columns_z)
            feature_name = input("Enter feature name (column): ")
            if self.check_feature_name(feature_name):
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
            if self.check_feature_value(feature_value,feature_name):
                return feature_value
            print("Value not found in feature. Please try again.")
    def process_feature_pairs(self,feature_input_list):
        for i in range(0,len(feature_input_list),2):
            feature_name =feature_input_list[i]
            feature_value = feature_input_list[i+1]
            if not self.check_feature_name(feature_name):
                return False
            if not self.check_feature_value(feature_value,feature_name):
                return False
            self.update_statistics(feature_name, feature_value)
            self.columns_z.remove(feature_name)
        return True
    def run_classification(self):
        continue_input = "yes"
        while continue_input.lower() in ["yes", "y"]:
            feature_name = self.get_valid_feature_name()
            feature_value = self.get_valid_feature_value(feature_name)
            self.update_statistics(feature_name, feature_value)
            self.columns_z.remove(feature_name)
            if len(self.columns_z) > 0:
                continue_input = input("Do you want to enter another feature? (yes/no): ")
            else:
                continue_input = "no"
    def input_statistics(self,feature_input_list=None):
        if not self.loaded:
            print("No data available. Please load the CSV file first.")
            return
        self.label_scores = {label: 1 for label in self.class_labels}
        self.columns_z = [i for i in self.columns]
        if not feature_input_list or not self.process_feature_pairs(feature_input_list):
            self.run_classification()
            print("Data entry is complete. Calculation is in progress.")


        # self.Percentage_display()
        self.finalize_scores()
        return self.most_likely_label
    def print_percentage(self):
        print(f"\nMost probable classification: {self.most_likely_label} (probability score: {self.highest_score})")
        print("\nProbability scores for all classes:")
        for label in self.label_scores:
            print(f"\t{label}: {self.label_scores[label]}")

