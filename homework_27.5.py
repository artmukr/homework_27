domains = [
    'nytimes.com', 'google.com', 'bk.com',
    'google.com', 'geeksforgeeks.com', 'portal.com',
    'bk.com', 'google.com', 'bk.com',
    'mcdonalds.com', 'test.ua', 'jackdanials.us'
]


def popular_searcher(links):
    dict1 = {}
    keys = []
    for item in links:
        if item not in dict1.keys():
            dict1.update({item: 1})
        else:
            dict1[item] += 1
    max_value = max(dict1.values())
    for key, value in dict1.items():
        if value == max_value:
            keys.append(key)
    return keys


print(popular_searcher(domains))
