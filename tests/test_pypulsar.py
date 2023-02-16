from pandas import DataFrame

from pypulsar import Bookie, Broker, Cluster


def test_cluster():
    pulsar_cluster = Cluster(False, "localhost", "8080")
    assert isinstance(pulsar_cluster.all_bookie_info(), DataFrame) == True
    assert isinstance(
        pulsar_cluster.get_rack_placement_bookies(), dict) == True
    assert (
        isinstance(
            pulsar_cluster.get_pending_bookie_client_op_stats(), DataFrame) == True
        and pulsar_cluster.get_pending_bookie_client_op_stats().columns.tolist()
        == [
            "Type",
            "dataLedgerOpenOp",
            "dataLedgerCloseOp",
            "dataLedgerCreateOp",
            "dataLedgerDeleteOp",
            "cursorLedgerOpenOp",
            "cursorLedgerCloseOp",
            "cursorLedgerCreateOp",
            "cursorLedgerDeleteOp",
        ]
    ) or isinstance(pulsar_cluster.get_pending_bookie_client_op_stats(), dict) == True

    assert isinstance(pulsar_cluster.get_all_brokers(), list) == True


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


def test_brokers():
    pulsar_broker = Broker(False, "localhost", "8080")
    assert (
        isinstance(pulsar_broker.get_broker_availability_report(
            "public", "default"), dict) == True
    )
    assert isinstance(pulsar_broker.get_broker_stats_allocator(
        "default"), dict) == True
    broker_load = pulsar_broker.get_broker_load()
    if broker_load != {}:
        assert isinstance(broker_load, dict) == True and set(list(broker_load.keys())) == set(
            [
                "webServiceUrl",
                "pulsarServiceUrl",
                "persistentTopicsEnabled",
                "nonPersistentTopicsEnabled",
                "cpu",
                "memory",
                "directMemory",
                "bandwidthIn",
                "bandwidthOut",
                "msgThroughputIn",
                "msgThroughputOut",
                "msgRateIn",
                "msgRateOut",
                "lastUpdate",
                "lastStats",
                "numTopics",
                "numBundles",
                "numConsumers",
                "numProducers",
                "bundles",
                "lastBundleGains",
                "lastBundleLosses",
                "brokerVersionString",
                "protocols",
                "advertisedListeners",
                "bundleStats",
                "loadReportType",
                "maxResourceUsage",
            ]
        )
