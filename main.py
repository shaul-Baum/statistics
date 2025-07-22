from UserInteraction import UserInteraction

if __name__ == "__main__":
    ui = UserInteraction()
    ui.read_csv()
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


    ui.input_statistics(a)
