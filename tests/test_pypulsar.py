from pandas import DataFrame

from pypulsar import Bookie, Cluster


def test_cluster():
    pulsar_cluster = Cluster(False, "localhost", "8080")
    assert isinstance(pulsar_cluster.all_bookie_info(), DataFrame) == True
    assert isinstance(
        pulsar_cluster.get_rack_placement_bookies(), dict) == True


def test_bookies():
    pulsar_bookie = Bookie(False, "localhost", "8080", "127.0.0.1:3181")
    assert isinstance(
        pulsar_bookie.delete_rack_placement_bookie(), dict) == True
    assert isinstance(pulsar_bookie.get_rack_placement_bookie(), dict) == True
    assert (
        isinstance(
            pulsar_bookie.update_rack_placement_info_bookie(
                {"hostname": "string", "rack": "string"}
            ),
            dict,
        )
        == True
    )
