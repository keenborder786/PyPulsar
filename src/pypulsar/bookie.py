import json
from typing import Dict

import requests

from pypulsar.cluster import Cluster


class Bookie(Cluster):
    """

    The main class to interact with specific bookie on pulsar cluster

    """

    def __init__(self, secured: bool, webservice_url: str, webservice_port: str, bookie_id: str):
        super().__init__(secured, webservice_url, webservice_port)
        self.bookie_id = bookie_id

    def delete_rack_placement_bookie(self) -> Dict:
        """
        Removed the rack placement information for a specific bookie in the cluster

        """

        response = requests.delete(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/bookies/racks-info/{self.bookie_id}"
        )
        if response.status_code == 200:
            print("Rack placement information was deleted")
        elif response.status_code == 404:
            print(response.content.decode("utf-8"))
        elif response.status_code == 403:
            print("Don't have admin permissions")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")
        return {}

    def get_rack_placement_bookie(self) -> Dict:
        """
        Gets the rack placement information for a specific bookie in the cluster

        """
        response = requests.get(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/bookies/racks-info/{self.bookie_id}"
        )
        if response.status_code == 200:
            return json.loads(response.content.decode("utf-8"))
        elif response.status_code == 404:
            print(response.content.decode("utf-8"))
        elif response.status_code == 403:
            print("Don't have admin permissions")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")
        return {}

    def update_rack_placement_info_bookie(self, rack_info: Dict) -> Dict:
        """

        Updates the rack placement information for a specific bookie in the cluster

        Parameters:
        ----------------------------------------------

        rack_info(Dict): The rack placment information which you to use in the form:{"hostname": "string","rack": "string"}

        """
        response = requests.post(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/bookies/racks-info/{self.bookie_id}",
            headers={"Content-Type": "application/json"},
            data=json.dumps(rack_info),
        )
        if response.status_code == 200:
            print("The rack placement information was updated")
        elif response.status_code == 404:
            print(response.content.decode("utf-8"))
        elif response.status_code == 403:
            print("Don't have admin permissions")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")
        return {}
