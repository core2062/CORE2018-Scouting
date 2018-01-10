""" Match schedule imported from TBA before competition. Use scraping program found at
    https://github.com/core2062/TBAScraper to quickly get this data that is
    formatted correctly,
    Format: red team1, red team2, red team3, blue team1, blue team3, blue team3 """

SCHEDULE = [
    (3276, 6732, 2830, 2062, 4657, 5003), (5098, 1739, 4021, 4247, 3100, 2530),
    (4959, 2506, 6419, 1306, 1625, 5586), (5442, 1091, 4624, 4762, 3695, 5826),
    (171, 5339, 2826, 5148, 5914, 48), (3750, 5903, 3090, 3418, 6624, 6574),
    (6166, 2451, 2194, 4531, 930, 5019), (1986, 967, 167, 269, 4655, 2077),
    (171, 6420, 1306, 2977, 4021, 3381), (6732, 3090, 2062, 5826, 5098, 5914),
    (1625, 930, 3695, 3750, 5339, 5148),
            (1739, 167, 269, 2506, 5442, 2451), (5586, 2977, 3100, 6166, 1986, 5019),
            (6624, 3276, 4624, 4655, 6420, 6574), (3418, 2194, 5003, 967, 4959, 1091),
            (2530, 48, 6419, 2077, 4531, 2830), (4762, 3381, 2826, 5903, 4247, 4657),
            (5148, 5098, 2977, 2506, 6574, 269), (2062, 3418, 1625, 4624, 3100, 167),
            (2451, 5586, 5914, 2194, 6420, 967), (3750, 2077, 5826, 1306, 5003, 2826),
            (930, 3090, 2530, 1986, 3276, 48), (4657, 1091, 5339, 6624, 5442, 4655),
            (2830, 4247, 5019, 171, 3695, 4531), (1739, 6732, 6166, 5903, 6419, 4021),
            (4959, 4762, 2977, 3381, 967, 930), (2506, 2530, 6624, 2062, 4624, 2826),
            (3100, 2451, 1091, 3750, 5586, 4657), (4531, 1306, 4655, 3695, 3418, 1739),
            (4247, 1986, 3381, 48, 5339, 6732), (6574, 6166, 5098, 5003, 2830, 6420),
            (5914, 167, 5019, 4762, 5148, 6419), (2077, 171, 5903, 5442, 3276, 1625),
            (2194, 4021, 4959, 269, 5826, 3090), (6166, 5003, 5339, 1091, 1739, 2062),
            (4624, 1986, 5098, 4531, 3750, 967), (1306, 4247, 6732, 6574, 167, 930),
            (4959, 5019, 3090, 5903, 2826, 4655), (3695, 4657, 2077, 171, 5914, 2194),
            (2506, 3276, 5826, 2451, 3381, 6419), (5148, 269, 5586, 4762, 2830, 6624),
            (5442, 3418, 3100, 6420, 2530, 2977), (4021, 1306, 967, 1625, 48, 4657), (6166, 6419, 167, 4959, 4624, 171),
            (1739, 6574, 3090, 2077, 4762, 5586), (3695, 5442, 1986, 5098, 2826, 2451),
            (1625, 3750, 4247, 2830, 4655, 2194), (5339, 2062, 6420, 269, 4531, 5903),
            (3276, 5148, 2530, 6732, 1091, 2977), (5826, 48, 3381, 5019, 6624, 3100),
            (5003, 5914, 4021, 930, 2506, 3418), (1986, 2062, 6574, 3695, 2194, 6419),
            (5339, 2977, 2830, 3090, 2077, 4624), (5903, 5019, 1091, 167, 1306, 5098),
            (2826, 3418, 4657, 6166, 930, 269), (5914, 4531, 5442, 3276, 4959, 5586),
            (1625, 2451, 6624, 4021, 2530, 4762), (4655, 3750, 48, 6732, 2506, 3381),
            (5826, 1739, 6420, 171, 5148, 967), (3100, 269, 6419, 4247, 5003, 3090),
            (5019, 5098, 5339, 3276, 4021, 3418), (4624, 4531, 2451, 1091, 5914, 1306),
            (2062, 4762, 48, 3750, 4959, 6420), (4655, 3100, 930, 6574, 171, 5442), (167, 3381, 5003, 5586, 3695, 2530),
            (6732, 1625, 2194, 1739, 2826, 2977), (5903, 5826, 5148, 4657, 2830, 1986),
            (967, 2077, 2506, 4247, 6166, 6624), (48, 930, 171, 2062, 5586, 5098), (4021, 269, 2826, 4655, 6419, 1091),
            (2830, 6574, 4959, 1739, 1986, 5339), (6420, 4657, 4531, 2506, 3090, 167),
            (5442, 2530, 967, 6732, 5019, 3750), (3381, 2194, 2077, 3418, 5148, 4624),
            (1306, 3695, 3276, 3100, 4762, 6166), (6624, 5903, 5914, 2451, 2977, 5003),
            (4247, 6420, 930, 1625, 5826, 1091), (269, 4624, 4657, 1739, 48, 5019), (167, 2830, 2826, 3100, 967, 3276),
            (2077, 6624, 6419, 4959, 5098, 3695), (4762, 171, 3418, 1986, 6732, 5003),
            (2506, 2194, 5586, 2530, 5903, 5339), (3090, 1625, 5914, 5442, 6166, 3381),
            (6574, 3750, 2977, 4021, 5826, 4531), (4247, 4655, 5148, 2451, 2062, 1306)
]