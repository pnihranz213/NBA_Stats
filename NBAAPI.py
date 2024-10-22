# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

import requests
import time

class ResponseError(Exception):
    """Raised when the API response is not 200"""
    pass


class NBA_API():

    #Create a session object to persist cookies across requests
    session = requests.Session()
    session.headers = {'accept': 'application/json'}

    def __init__(self, api_key, format_='json', language='en',
                 access_level='trial'):
        
        self.api_key = {'api_key': api_key}
        self.api_root = 'http://api.sportradar.us/'
        self.access_level = access_level
        self.language = language
        self.version = 8
        self.prefix = 'nba/{level}/v{ver}/{lang}/'.format(
                        level=self.access_level, ver=self.version, lang=self.language)

    def get_game_summary(self, game_id):
        """Provides top-level boxscore information, along with detailed game stats at the
            team and player levels
        """
        path = "games/{game_id}/summary.json?api_key={api_key}".format(game_id=game_id, api_key=self.api_key)
        response = requests.get(self.api_root + self.prefix + path)
        if response.status_code == 200:
            return response.json()
        else:
            print (response.status_code)
            raise ResponseError

    def get_league_hierarchy(self):
        """League, conference, division, and team identification"""
        path = "league/hierarchy.json?api_key={api_key}".format(api_key=self.api_key)
        response = requests.get(self.api_root + self.prefix + path)
        if response.status_code == 200:
            return response.json()
        else:
            print (response.status_code)
            raise ResponseError       
        

    def get_schedule(self, season_year, season_type='REG'):
        """Get the schedule for a given NBA Season"""
        path = "games/{season_year}/{season_type}/schedule.json?api_key={api_key}".format(
            season_year=season_year, season_type=season_type, api_key=self.api_key)
        response = requests.get(self.api_root + self.prefix + path)
        if response.status_code == 200:
            return response.json()
        else:
            print (response.status_code)
            raise ResponseError

    def get_seasonal_statistics_season_to_date(self, season_year, team_id, season_type='REG'):
        """Provides detailed team and player statistics for the defined season"""
        path = "seasons/{season_year}/{season_type}/teams/{team_id}/statistics.json?api_key={api_key}".format(
            season_year=season_year, season_type=season_type, team_id=team_id, api_key=self.api_key)
        response = requests.get(self.api_root + self.prefix + path)
        if response.status_code == 200:
            return response.json()
        else:
            print (response.status_code)
            raise ResponseError
