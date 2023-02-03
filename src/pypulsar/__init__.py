# read version from installed package
from importlib.metadata import version
from pypulsar.cluster import Cluster
__version__ = version("pypulsar")