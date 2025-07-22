import pandas as pd
from UserInteraction import UserInteraction


class Examination:
    def __init__(self,data_test,search,columns):
        self.ui = UserInteraction()
        self.data_test =data_test
        self.search =search
        self.columns = columns
    def examination(self,dataframe):
        if self.ui.input_statistics(a)==1111111111111:
            pass







#
# # נניח שזה הדאטא פריים שלך
# df = pd.read_csv("data.csv")
#
# # ערבוב רנדומלי של השורות
# df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
#
# # חישוב אינדקס החיתוך
# split_index = int(0.7 * len(df_shuffled))
#
# # יצירת דאטא פריים לאימון ולבדיקה
# train_df = df_shuffled[:split_index]
# test_df = df_shuffled[split_index:]
#
# # בדיקה
# print(f"Total rows: {len(df)}")
# print(f"Train set: {len(train_df)}")
# print(f"Test set: {len(test_df)}")
