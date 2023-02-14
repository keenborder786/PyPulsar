# read version from installed package
from importlib.metadata import version

from pypulsar.bookie import Bookie
from pypulsar.broker import Broker
from pypulsar.cluster import Cluster

__version__ = version("pypulsar")
