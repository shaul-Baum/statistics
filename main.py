from StatisticsManager import StatisticsManager
from Statistics_by_data import StatisticsByData
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
if __name__ == "__main__":
    ui = StatisticsManager()
    probability_table = ui.read_csv()
    if ui.evaluate_model(probability_table) > 65:
        e = StatisticsByData(probability_table)
        e.input_statistics(a)
        e.print_percentage()
    else:
        print("Sorry, our model was unable to produce good enough data based on the data you entered. You are welcome to try again at any time.")