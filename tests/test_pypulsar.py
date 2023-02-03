from pypulsar import Cluster
from pandas import DataFrame

def test_cluster():
    pulsar_cluster = Cluster(False , 'localhost' , '8080')
    bookie_info = pulsar_cluster.all_bookie_info()
    print(pulsar_cluster.get_rack_placement_bookies())
    assert isinstance(bookie_info , DataFrame) == True
