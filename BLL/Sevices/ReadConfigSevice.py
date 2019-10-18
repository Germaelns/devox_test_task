import sys
import json


class ReadConfigService:

    @staticmethod
    def get_postgres_uri():
        with open(sys.path[1] + "/config.json") as json_file:
            data = json.load(json_file)
        return data["postgres"]["uri"]