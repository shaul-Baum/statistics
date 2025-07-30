from TrainerManager import TrainerManager
from Validator import Validator
a =[
    'UsingIP', -1,
    'LongURL', -1,
    'ShortURL', 1,
    'Symbol@', 1,
    'Redirecting//', -1,
    'PrefixSuffix-', 1,
    'SubDomains', 1,
    'HTTPS', -1,
    'DomainRegLen', -1,
    'Favicon', -1,
    'NonStdPort', 1,
    'HTTPSDomainURL', 1,
    'RequestURL', -1,
    'AnchorURL', 1,
    'LinksInScriptTags', -1,
    'ServerFormHandler', 1,
    'InfoEmail', -1,
    'AbnormalURL', 1,
    'WebsiteForwarding', 1,
    'StatusBarCust', -1,
    'DisableRightClick', 1,
    'UsingPopupWindow', -1,
    'IframeRedirection', 1,
    'AgeofDomain', -1,
    'DNSRecording', 1,
    'WebsiteTraffic', -1,
    'PageRank', 1,
    'GoogleIndex', -1,
    'LinksPointingToPage', 1,
    'StatsReport', -1
]
b = [
    "age","youth",
    "income","high",
    "student","no",
    "credit_rating","fair"
]
# csv="phishing.csv",search="class"
# csv = "data_for_NB_buys_computer.csv",search = "Buy_Computer"
if __name__ == "__main__":
    ui = TrainerManager()
    t = False
    choice = None
    while choice != "exit":
        print("To replace the csv press 1"
                "\nTo see the accuracy percentage press 2"
                "\nTo ask questions press 3"
                "\nTo exit press exit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            ui._input_csv()
        if not t or choice == "1" or not loaded:
            probability_table,loaded = ui.read_csv()
            t = True
            if loaded:
                level_test = ui.evaluate_model(probability_table)
        if loaded:
            if choice == "2":
                print(f"Model confidence level at this stage: {level_test}%")
            if level_test > 55:
                if choice == "3":
                    e = Validator(probability_table)
                    print("To replace data press 1 To use default press 0")
                    choice_2 = input("Please enter your choice: ")
                    if choice_2 != "1":
                        r = a
                    else:
                        r = None
                    e.input_statistics(r)
                    e.print_percentage()
            else:
                print("Sorry, our model was unable to produce good enough data based on the data you entered. You are welcome to try again at any time.")
        else:
            print("Sorry, the information did not load correctly. Replace the file and try again.")