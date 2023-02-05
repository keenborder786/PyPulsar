import json
from typing import Dict

import pandas as pd
import requests
from pandas import DataFrame


class Cluster:
    """

    The class which act as an entry point to execute all cluster-wide operations


    """

    def __init__(self, secured: bool, webservice_url: str, webservice_port: str) -> None:
        if not secured:
            self.request_type = "http"
        else:
            self.request_type = "https"
        self.webservice_url = webservice_url
        self.webservice_port = webservice_port

    def all_bookie_info(self) -> DataFrame:
        """

        Gets raw information for all the bookies in the cluster

        """
        response = requests.get(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/bookies/all"
        )
        if response.status_code == 200:
            final_response = json.loads(response.content)["bookies"]
            final_response_df = pd.DataFrame(final_response)
            return final_response_df
        elif response.status_code == 403:
            print("Don't have admin permission")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")
        return {}

    def get_rack_placement_bookies(self) -> Dict:
        """
        Gets the rack placement information for all the bookies in the cluster

        """
        response = requests.get(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/bookies/racks-info"
        )
        if response.status_code == 200:
            final_response = json.loads(response.content)
            return final_response
        elif response.status_code == 403:
            print("Don't have admin permission")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")
        return {}
