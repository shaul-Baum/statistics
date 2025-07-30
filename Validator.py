from Logger import Logger
import inspect
import os
class Validator:
    def __init__(self,dataStatistics):
        self.logger = Logger()
        self.probability_table =dataStatistics
        self.label_scores = {}
        self.most_likely_label = ""
        self.class_labels =[i for i in self.probability_table if i != "__total__"]
        self.highest_score = 0
        self.succeeded = 0
        self.not_succeeded = 0
    def check_feature_value(self,feature_value,feature_name):
        try:
            return feature_value in self.probability_table[self.class_labels[0]][feature_name]
        except:
            return False
    def update_statistics(self, feature_name, feature_value):
        for label in self.class_labels:
            if label not in self.label_scores:
                self.label_scores[label] = 1
            try:
                self.label_scores[label] *= self.probability_table[label][feature_name][feature_value]
            except:
                try:
                    feature_value = float(feature_value)
                    self.label_scores[label] *= self.probability_table[label][feature_name][feature_value]
                except:
                    try:
                        feature_value = int(feature_value)
                        self.label_scores[label] *= self.probability_table[label][feature_name][feature_value]
                    except KeyError:
                        self.logger.log("This is an error message","ERROR")
                        raise ValueError("This is an error message")
    def get_valid_feature_name(self):
        while True:
            feature_name = input("Enter feature name (column): ")
            if feature_name is not None:
                return feature_name
            print("Feature not found. Please try again.")
    def get_valid_feature_value(self):
        while True:
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
            feature_value = self.get_valid_feature_value()
            self.update_statistics(feature_name, feature_value)
            continue_input = input("Do you want to enter another feature? (yes/no): ")
    def process_feature_pairs(self,feature_input_list):
        for i in range(0,len(feature_input_list),2):
            feature_name =feature_input_list[i]
            feature_value = feature_input_list[i+1]
            if self.check_feature_value(feature_value,feature_name):
                self.succeeded += 1
            else:
                self.not_succeeded += 1
            try:
                self.update_statistics(feature_name, feature_value)
            except Exception as e:
                print(f"Failed to update statistics for feature '{feature_name}' with value '{feature_value}'")
                self.logger.log(f"Error processing feature '{feature_name}': {e}","WARNING")
        if self.succeeded > self.not_succeeded:
            caller_file = os.path.basename(inspect.stack()[2].filename) == "main.py"
            if caller_file:
                self.logger.log(f"Validation succeeded: {self.succeeded} features succeeded, {self.not_succeeded} failed.")
            return True
        else:
            print("More failed feature inputs than successful ones.")
            self.logger.log(f"Validation failed: {self.not_succeeded} features failed, {self.succeeded} succeeded.","ERROR")
            return False
    def finalize_scores(self):
        self.most_likely_label = max(self.label_scores, key=self.label_scores.get)
        self.highest_score = self.label_scores[self.most_likely_label]
        return self.most_likely_label, self.highest_score
    def input_statistics(self,feature_input_list=None):
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
