
import PythonLib.COREDependencies as COREDependencies
import PythonLib.CORETeamData as CORETeamData


class TeamData(CORETeamData.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):

        """ Use Constants from RANK_AND_MATCH_HEADERS, MATCH_HEADERS, and RANK_ONLY_HEADERS when defining keys for team_data """

        """self.team_data[COREDependencies.COREConstants.REPORT_HEADER[0]] = 76
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[0])
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[2]] = self.return_best(COREDependencies.COREConstants.RADIO_NAMES[0], ('Moat', 'Rockwall', 'RoughTerrain'))
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[3]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[0])"""
        # Total amount of matches played
        MatchesPlayed = self.num_data_entries('MatchNumber')
        # Climb Percentage
        TotalClimbs = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_VALUES['Climb'][2]) + self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_VALUES['Climb'][3])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[0]] = TotalClimbs / MatchesPlayed
        # Comments
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[3]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[1])
        # Crossed Baseline percentage
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[4]] = self.times_key_exists_in_category(COREDependencies.COREConstants.CHECKBOX_NAMES[0], ['ON'])
        # Auto Switch Percentage and Stats
        AutoSwitchLeft = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES[['CubeSwitchAuto'][0]])
        AutoSwitchRight = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES[['CubeSwitchAuto'][1]])
        AutoSwitchFail = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES[['CubeSwitchAuto'][2]])
        AutoSwitchTotal = AutoSwitchLeft + AutoSwitchRight
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[1]] = AutoSwitchTotal / MatchesPlayed
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[0]] = AutoSwitchLeft + ' : ' + AutoSwitchRight + ' : ' + AutoSwitchFail
        # Auto Scale Percentage and Stats
        AutoScaleLeft = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[1], COREDependencies.COREConstants.RADIO_VALUES[['CubeScaleAuto'][0]])
        AutoScaleRight = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[1], COREDependencies.COREConstants.RADIO_VALUES[['CubeScaleAuto'][1]])
        AutoScaleFail = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[1], COREDependencies.COREConstants.RADIO_VALUES[['CubeScaleAuto'][2]])
        AutoScaleTotal = AutoScaleLeft + AutoScaleRight
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[1]] = AutoScaleTotal / MatchesPlayed
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[0]] = AutoScaleLeft + ' : ' + AutoScaleRight + ' : ' + AutoScaleFail
        # Auto Exchange Percentage
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[3]] = self.times_key_exists_in_category(COREDependencies.COREConstants.CHECKBOX_NAMES[3], ['ON']) / MatchesPlayed
        # Floor Intake
        Majority = self.times_key_exists_in_category(COREDependencies.COREConstants.CHECKBOX_NAMES[2], ['ON']) / MatchesPlayed
        if Majority > 0.5:
            FloorPickup = 'Yes'
        else:
            FloorPickup = 'No'
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = FloorPickup
        # 