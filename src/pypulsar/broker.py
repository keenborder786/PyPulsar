import json
from typing import Dict

import requests

from pypulsar.cluster import Cluster


class Broker(Cluster):
    """

    The main class to interact with specific bookie on pulsar cluster

    """

    def __init__(self, secured: bool, webservice_url: str, webservice_port: str):
        """
        Parameters:
        ------------------------------

        secured(bool): http or https requests

        webservice_url(str): The web-service url for brokers to execute the api requests

        webservice_port(str): The web-service port for broker to execute the api requests

        bookie_id(str): The unique id to identify the bookie on pulsar cluster


        """
        super().__init__(secured, webservice_url, webservice_port)

    def get_broker_stats_allocator(self, allocator: str) -> Dict:
        """

        Parameters:
        --------------------------------------

        allocator(str): Available allocators are 'default' and 'ml-cache'


        Get the stats for the Netty allocator. Available allocators are 'default' and 'ml-cache'

        Returns:
        --------------------------------------
        Dict: Stats for the Netty allocator in form of dictionary

        """
        response = requests.get(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/broker-stats/allocator-stats/{allocator}"
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

    def get_broker_availability_report(self, tenant: str, namespace: str) -> Dict:
        """

        This API gives the current broker availability in percent, each resource percentage usage is calculated and
        thensum of all of the resource usage percent is called broker-resource-availability

        Parameters:
        --------------------
        tenant(str): The tenant for which you want availability report

        namespace(str): The namespace for which want availability report

        Returns:
        --------------------
        dict: The broker availability information in form of dictionary

        """

        response = requests.get(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/broker-stats/broker-resource-availability/{tenant}/{namespace}"
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

    def get_broker_load(self) -> Dict:
        """

        Gets the broker load which consists of topics stats & systemResourceUsage

        Returns:
        --------------------
        dict: The broker load information in form of dictionary

        """
        response = requests.get(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/broker-stats/load-report"
        )

        if response.status_code == 200:
            final_response = json.loads(response.content)
            return final_response
        elif response.status_code == 403:
            print("Don't have admin permission")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")
