import Statistics
from StatisticsManager import StatisticsManager
class UserInteraction(StatisticsManager):
    def __init__(self):
        super().__init__()
    def get_valid_feature_name(self):
        while True:
            print("Available features (columns):", self.columns)
            feature_name = input("Enter feature name (column): ")
            if feature_name in self.columns:
                return feature_name
            print("Feature not found. Please try again.")
    def get_valid_feature_value(self,feature_name):
        while True:
            print("Available values for this feature:", list(self.a.values_of_column(feature_name)))
            feature_value = input("Enter feature value: ")
            if feature_value in self.probability_table[self.class_labels[0]][feature_name]:
                return feature_value
            print("Value not found in feature. Please try again.")

    def input_statistics(self):
        if not self.loaded:
            print("No data available. Please load the CSV file first.")
            return
        continue_input = "yes"
        while continue_input.lower() in ["yes", "y"]:
            feature_name = self.get_valid_feature_name()
            feature_value = self.get_valid_feature_value(feature_name)
            self.update_statistics(feature_name, feature_value)
            self.columns.remove(feature_name)
            if len(self.columns) >0:
                continue_input = input("Do you want to enter another feature? (yes/no): ")
            else:
                continue_input = "no"
        print("Data entry is complete. Calculation is in progress.")

        self.Percentage_display()
        self.finalize_scores()
        print(f"\nMost probable classification: {self.most_likely_label} (percentage: {self.highest_score} %)")
        print("\nAll class scores:")
        for label in self.label_scores:
            print(f"\t{label} : {self.label_scores[label]:} %")