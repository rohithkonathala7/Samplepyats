'''
testing_job.py

'''
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2019, Cisco Systems Inc.'
__contact__ = ['pyats-support-ext@cisco.com']
__credits__ = ['list', 'of', 'credit']
__version__ = 1.0

import os
from genie.harness.main import grun

SCRIPT_PATH = os.path.dirname(__file__)

def main(runtime):
    '''job file entrypoint'''
    
    grun(
    	pdb = False,
    	trigger_datafile = "~/pyats/project/testing/testing_data.yaml",
    	trigger_uids = ["InitializeTestbed"]
    )
    
    # run script
    run(testscript= os.path.join(SCRIPT_PATH, 
                                 'testing.py'),
        runtime = runtime)
