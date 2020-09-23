import numpy as np
from rail.estimation.estimator import Estimator
from rail.estimation.utils import *
# this is temporary until unit test uses a definite test data set and creates
# the file on the fly
from rail.estimation.algos import randomPZ, sklearn_nn, flexzboost

test_base_yaml = './tests/base.yaml'

specific_estimator=[randomPZ.randomPZ, sklearn_nn.simpleNN]
input_dicts = [
    {'run_params': {'width': 0.025, 'zmin': 0.0, 'zmax': 3.0,
                    'nzbins': 301}}, 
    {'run_params': {'rand_width': 0.025, 'rand_zmin': 0.0, 'rand_zmax': 3.0,
                    'nzbins': 301}}
    {'run_params': {'zmin': 0.0, 'zmax': 3.0, 'nzbins': 301, 'trainfrac': 0.75,
                    'bumpmin': 0.02, 'bumpmax': 0.35, 'nbump': 20, 'sharpmin': 0.7,
                    'sharpmax': 2.1, 'nsharp': 15, 'max_basis': 35, 
                    'basis_system': 'cosine', 
                    'regression_params': {'max_depth': 8, 
                                          'objective':'reg:squarederror'}
                    }}
    ]

 
def test_algo(specific_estimator):
    """
    A basic test of simpleNN subclass
    """
    for one_estimator, one_input in zip(specific_estimator,input_dicts):

        pz = one_estimator(test_base_yaml,one_input)
        pz.inform()
        for _, end, data in iter_chunk_hdf5_data(pz.testfile, pz._chunk_size,
                                                 pz.hdf5_groupname):
            pz_dict = pz.estimate(data)
        assert end == pz.num_rows
        xinputs = inputs['run_params']
        assert len(pz.zgrid) == np.int32(xinputs['nzbins'])
