import json
from typing import Dict, Union

import pandas as pd
import requests
from pandas import DataFrame


class Cluster:
    """

    The class which act as an entry point to execute all cluster-wide operations


    """

    def __init__(self, secured: bool, webservice_url: str, webservice_port: str) -> None:
        """
        Parameters:
        ------------------------------

        secured(bool): http or https requests

        webservice_url(str): The web-service url for brokers to execute the api requests

        webservice_port(str): The web-service port for broker to execute the api requests

        """
        if not secured:
            self.request_type = "http"
        else:
            self.request_type = "https"
        self.webservice_url = webservice_url
        self.webservice_port = webservice_port

    def all_bookie_info(self) -> DataFrame:
        """

        Gets raw information for all the bookies in the cluster

        Returns
        ----------------------------

        DataFrame: All of the bookie information in form of dataframe.

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

        Returns:
        -------------------------------------

        Dict: Rack placement info for all bookie in form of dictionary

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

    def get_pending_bookie_client_op_stats(self) -> Union[DataFrame, Dict]:
        """

        Get pending bookie client op stats by namespace

        Returns:
        --------------------------------------
        Dict: Pending bookie client op stats by namespace in form dataframe

        """
        response = requests.get(
            f"{self.request_type}://{self.webservice_url}:{self.webservice_port}/admin/v2/broker-stats/bookieops"
        )
        if response.status_code == 200:
            final_response = json.loads(response.content)
            keys = list(final_response.keys())
            final_dataframe_data = []
            for key in keys:
                topic_function_data = final_response[key]
                topics_functions = list(topic_function_data.keys())
                for topic_func in topics_functions:
                    instance = {}
                    instance["Type"] = topic_func
                    metric_data = topic_function_data[topic_func]
                    for key, value in metric_data.items():
                        instance[key] = value
                    final_dataframe_data.append(instance)
            df_final_response = pd.DataFrame(final_dataframe_data)
            return df_final_response
        elif response.status_code == 403:
            print("Don't have admin permission")
        else:
            print(
                f"Request could not happen due to the following to error {response.status_code}")

        return {}
