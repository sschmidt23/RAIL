import sys
import yaml
from estimator import Estimator as BaseEstimation
from utils import *
import algos

#Note: This is where 'base.yaml' actually belongs, but how to make it so 
def main(argv):
    if len(argv) != 2:
        print(len(argv))
        print("Usage: main <yaml file>")
        exit()
    input_yaml = argv[1]
    name = input_yaml.split("/")[-1].split(".")[0]

    with open(input_yaml, 'r') as f:
        config_dict = yaml.safe_load(f)

    print(config_dict)
    run_dict = config_dict

    try:
        run_dict['class_name'] = BaseEstimation._find_subclass(name)
    except KeyError:
        raise ValueError(f"Class name {name} for PZ code is not defined")

    code = BaseEstimation._find_subclass(name)
    print(f"code name: {code}")

    pz = code(run_dict)
    
    pz.train()

    for i, (start, end, data) in enumerate(iter_chunk_hdf5_data(pz.testfile,
                                                                pz._chunk_size)):
        if i==0:
            outhandle = pz.initialize_writeout()
        pz.test_data = data
        pz.run_photoz()
        pz.write_out_chunk(outhandle, start, end)

    pz.finalize_writeout(outhandle)
        
    print("finished")

if __name__=="__main__":
    main(sys.argv)
