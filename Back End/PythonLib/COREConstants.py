
""" Various constants used throughout the program that are intended primarily to map form fields,
    but also for key names

        form dependency : Needs to be the same names as those given by the html form.
            It is important that these names appear EXACTLY the same as those supplied by the front end!
        no dependency : Names that will be visually displayed on output tables.
            Should be named in accordance of which they are displaying, but the name is not dependant on any
            other input or variable names"""

"""===========================================
General Team Info (no dependency)
-------------------------------------------"""

TEAM_NUMBER = 2062

COMPETITION_NAME = '2018_PreComp'

"""===========================================
Scout HTML input field names (form dependency)
-------------------------------------------"""

#  form value name that contains the match and team number. (change second name)
TEAM_FIELD_NUMBER = {'team_number': 'TeamNumber'}
MATCH_NUMBER = {'match_number': 'MatchNumber'}

CHECKBOX_NAMES = [
    'CubeFloorPickup',
    'CrossedBaselineAuto'
]
NUMBER_NAMES = [
    MATCH_NUMBER['match_number'],
    'OwnSwitchCubesDelivered',
    'ScaleCubesDelivered',
    'OpposingSwitchCubesDelivered',
    'ExchangeCubesDelivered'
]
TEXT_NAMES = [
    'ScoutName',
    'comments'
]
RADIO_NAMES = [
    'CubeSwitchAuto',
    'CubeScaleAuto',
    'CubeExchangeAuto',
    'Climb'

]
RADIO_VALUES = {
    'CubeSwitchAuto': ('LeftSwitchAuto', 'RightSwitchAuto', 'NoAttempt', 'FailedSwitchAuto'),
    'CubeScaleAuto': ('LeftScaleAuto', 'RightScaleAuto', 'NoAttempt', 'FailedScaleAuto'),
    'CubeExchangeAuto': ('DidDeliverInExchange', 'DidNotDeliverInExchange', 'FailedDeliveryInExchange'),
    'Climb': ('NoClimb', 'ClimbPark', 'DidClimb', 'ClimbLevitate', 'ClimbFail')
}

ALL_NAMES = []

for checkbox in CHECKBOX_NAMES:
    ALL_NAMES.append(checkbox)
for number in NUMBER_NAMES:
    ALL_NAMES.append(number)
for text in TEXT_NAMES:
    ALL_NAMES.append(text)
for radio in RADIO_NAMES:
    ALL_NAMES.append(radio)

"""=====================================
Match Report Row Headers (no dependency)
-------------------------------------"""


# Show up on Match Report and Ranking Report if applicable
RANK_AND_MATCH_HEADERS = [
    'Climb Percentage',
    'Crossed Baseline Percentage',
    'Avg Cubes Delivered: Home Switch',
    'Avg Cubes Delivered: Scale',
    'Avg Cubes Delivered: Opposing Switch',
    'Avg Cubes Delivered: Exchange'
]

# Shows up as a ranking Option only
RANK_ONLY_HEADERS = [
    'Auto Switch Percentage',
    'Auto Scale Percentage',
    'Auto Exchange Percentage'
]

# Shows up on Match Report only
MATCH_HEADERS = [
    'Switch Auto, Left:Right:Fail:None',
    'Scale Auto, Left:Right:Fail:None',
    'Exchange Auto, Yes:No:Fail',
    'Comments'
]


"""=============================================
Match Report input field names (form dependency)
---------------------------------------------"""

RANK_REPORT_FIELD_NAMES = {
    'ranking_options': 'ranking_type'
}

""" The following describes how to use RANK_OPTIONS to map form values to rank statistics.
    it should be a list of tuples that have the following data in them (IN ORDER).

        1. Form value name of RANK_REPORT_FIELD_NAMES['ranking_options'] that you wish to
            correspond the ranking to. (The ranking report form value)
        2. Name of statistic to rank by from RANK_AND_MATCH_HEADERS or RANK_ONLY_HEADERS
        3. Order in which teams should be ranked. The following are accepted
                'descending' - Ranking from best to worst
                'ascending' - Ranks from worst to best
                'category' - Ranks based on multiple strings given a 3'd argument.
        (4). (ORDER SPECIFIC ARGUMENT) Should only be supplied if order is 'category'.
            A tuple of all possible submission data for the supplied rank_statistic
            category corresponding to the statistic's RADIO_VALUES values in order of
            which should be displayed last, worst -> best.
            Intended to be used for ranking based on a priority of strings.
    EX: 'High Goal Accuracy': ('highGoals', 'high Goal Accuracy', 'descending')
    EX: 'Highest Auto Type': ('highest_auto_type', 'Highest Auto', 'category', ('breach', 'reach', 'no_interaction')) """

RANK_OPTIONS = [
    # EXAMPLE     ('Defense', 'Defense Rating', 'category', ('Amazing', 'Good', 'Alright', 'Not Great')) (Also can look above for example^^^
    ('ClimbPercent', 'Climbing Percentage', 'descending'),
    ('AutoSwitchPercent', 'Auto Switch Percentage', 'descending'),
    ('AutoScalePercent', 'Auto Scale Percentage', 'descending'),
    ('AutoExchangePercent', 'Auto Exchange Percent', 'descending'),
    ('CrossBaselinePercent', 'Cross Baseline Percentage', 'descending'),
    ('TeleCubesHSwitch', 'Cubes Delivered: Home Switch', 'descending'),
    ('TeleCubesOSwitch', 'Cubes Delivered: Opposing Switch', 'descending'),
    ('TeleCubesScale', 'Cubes Delivered: Scale', 'descending'),
    ('TeleCubesExchange', 'Cubes Delivered: Exchange', 'descending'),
]