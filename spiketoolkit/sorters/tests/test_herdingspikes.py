import unittest
import pytest
import spikeextractors as se
from spiketoolkit.sorters import HerdingspikesSorter

from spiketoolkit.sorters.tests.common_tests import SorterCommonTestSuite

# This run several tests
@pytest.mark.skipif(not HerdingspikesSorter.installed, reason='herding spikes not installed')
class HSCommonTestSuite(SorterCommonTestSuite, unittest.TestCase):
   SorterClass = HerdingspikesSorter

if __name__ == '__main__':
    HSCommonTestSuite().test_on_toy()
    HSCommonTestSuite().test_several_groups()
    
