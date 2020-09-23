import numpy as np
from rail.estimation.estimator import Estimator
from rail.estimation.utils import *
# this is temporary until unit test uses a definite test data set and creates
# the file on the fly
from rail.estimation.algos import randomPZ, sklearn_nn

test_base_yaml = './tests/base.yaml'


def test_random():
    """
    A couple of basic tests of the random class
    """

    inputs = {'run_params':{'rand_width': 0.025, 'rand_zmin': 0.0, 'rand_zmax': 3.0,
                            'nzbins': 301}}

    pz = randomPZ.randomPZ(test_base_yaml, inputs)
    for _, end, data in iter_chunk_hdf5_data(pz.testfile, pz._chunk_size,
                                                 pz.hdf5_groupname):
        pz_dict = pz.estimate(data)
    assert end == pz.num_rows
    xinputs = inputs['run_params']
    assert len(pz.zgrid) == np.int32(xinputs['nzbins'])

def test_simpleNN():
    """
    A basic test of simpleNN subclass
    """
    inputs = {'run_params': {'width': 0.025, 'zmin': 0.0, 'zmax': 3.0, 
                             'nzbins': 301}}

    pz=sklearn_nn.simpleNN(test_base_yaml, inputs)
    pz.inform()
    for _, end, data in iter_chunk_hdf5_data(pz.testfile, pz._chunk_size,
                                             pz.hdf5_groupname):
        pz_dict = pz.estimate(data)
    assert end == pz.num_rows
    xinputs = inputs['run_params']
    assert len(pz.zgrid) == np.int32(xinputs['nzbins'])
