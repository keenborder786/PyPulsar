# read version from installed package
from importlib.metadata import version

from pypulsar.bookie import Bookie
from pypulsar.cluster import Cluster

__version__ = version("pypulsar")
