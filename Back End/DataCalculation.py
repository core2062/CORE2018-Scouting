
import PythonLibrary.COREDependencies as COREDependencies
import PythonLibrary.CORETeamData as CORETeamData


class TeamData(CORETeamData.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):

        """ Use Constants from RANK_AND_MATCH_HEADERS, MATCH_HEADERS, and RANK_ONLY_HEADERS when defining keys for team_data self.team_data[COREDependencies.COREConstants.REPORT_HEADER[0]] = 76
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[0])
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[2]] = self.return_best(COREDependencies.COREConstants.RADIO_NAMES[0], ('Moat', 'Rockwall', 'RoughTerrain'))
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[3]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[0])"""
        # Total amount of matches played
        MatchesPlayed = self.num_data_entries('MatchNumber')
        # Climb Percentage
        TotalClimbs = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[3], 'DidClimb')
        TotalLevitates = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[3], 'ClimbLevitate')
        TotalNoClimbs = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[3], 'NoClimb')
        TotalParks = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[3], 'ClimbPark')
        TotalClimbFails = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[3], 'ClimbFail')
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[0]] = str(TotalClimbs) + ' : ' + str(TotalLevitates) + ' : ' + str(TotalParks) + ' : ' + str(TotalClimbFails) + ' : ' + str(TotalNoClimbs)
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[3]] = (TotalClimbs + TotalLevitates) / MatchesPlayed
        # Comments
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[4]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[1])
        # Crossed Baseline percentage
        # TotalBaselineCrosses = self.times_key_exists_in_category('CrossedBaselineAuto', 'ON')
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[0]] = self.times_key_exists_in_category('CrossedBaselineAuto', 'ON') / MatchesPlayed
        # Auto Switch Percentage and Stats
        AutoSwitchLeft = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], 'LeftSwitchAuto')
        AutoSwitchRight = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], 'RightSwitchAuto')
        AutoSwitchNone = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], 'NoAttempt')
        AutoSwitchFail = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], 'FailedSwitchAuto')
        AutoSwitchTotal = AutoSwitchLeft + AutoSwitchRight
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[0]] = AutoSwitchTotal / MatchesPlayed
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[1]] = str(AutoSwitchLeft) + ' : ' + str(AutoSwitchRight) + ' : ' + str(AutoSwitchFail) + ' : ' + str(AutoSwitchNone)
        # Auto Scale Percentage and Stats
        AutoScaleLeft = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[1], 'LeftScaleAuto')
        AutoScaleRight = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[1], 'RightScaleAuto')
        AutoScaleFail = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[1], 'FailedScaleAuto')
        AutoScaleNone = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[1], 'NoAttempt')
        AutoScaleTotal = AutoScaleLeft + AutoScaleRight
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[1]] = AutoScaleTotal / MatchesPlayed
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = str(AutoScaleLeft) + ' : ' + str(AutoScaleRight) + ' : ' + str(AutoScaleFail) + ' : ' + str(AutoScaleNone)
        # Auto Exchange Percentage
        AutoExchangeDeliver = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[2], 'DidDeliverInExchange')
        AutoExchangeNoDeliver = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[2], 'DidNotDeliverInExchange')
        AutoExchangeFailedDeliver = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[2], 'FailedDeliveryInExchange')
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[2]] = AutoExchangeDeliver / MatchesPlayed
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[3]] = str(AutoExchangeDeliver) + ' : ' + str(AutoExchangeNoDeliver) + ' : ' + str(AutoExchangeFailedDeliver)
        # Floor Intake
        #FloorPickupON = self.times_key_exists_in_category(COREDependencies.COREConstants.CHECKBOX_NAMES[1], ['ON'])
        #MajorityFI = FloorPickupON / MatchesPlayed
       # if MajorityFI > 0.5:
       #     FloorPickup = 'Yes'
       # else:
        #    FloorPickup = 'No'
       # self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = FloorPickup
        # Avg Cubes Tele Home Switch
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[1])
        # Avg Cubes Tele Scale
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[2]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[2])
        # Avg Cubes Tele Opposing Switch
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[3]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[3])
        # Avg Cubes Tele Exchange
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[4]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[4])

