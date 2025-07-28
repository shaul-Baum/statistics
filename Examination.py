from Statistics_by_data import StatisticsByData
import pandas as pd


class Examination:
    def __init__(self,probability_table,data_test,search):
        self.ui = StatisticsByData(probability_table)
        self.data_test =data_test
        self.search =search
        self.correct_predictions = 0
        self.incorrect_predictions = 0
    def examination(self):
        for i in range(len(self.data_test)):
            row = self.data_test.iloc[i]
            actual_label = row[self.search]
            flattened = [item for col, val in row.items() if col != self.search for item in (col, val)]
            if self.ui.input_statistics(flattened)==actual_label:
                self.correct_predictions += 1
            else:
                self.incorrect_predictions += 1
        return self.get_accuracy()
    def get_accuracy(self):
        total = self.correct_predictions + self.incorrect_predictions
        if total == 0:
            return 0
        return int((self.correct_predictions *100 ) / total)


