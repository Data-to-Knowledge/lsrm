# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:25:41 2019

@author: michaelek
"""
import os
import pandas as pd

pd.options.display.max_columns = 10

#################################################
### Parameters


dataset_path = r'E:\ecan\git\lsrm\lsrm\datasets'

irr_file = 'AQUALINC_NZTM_IRRIGATED_AREA_20160629.pkl.xz'
paw_file = 'LAND_NZTM_NEWZEALANDFUNDAMENTALSOILS.pkl.xz'


#################################################
### Save datasets


irr1.to_pickle(os.path.join(dataset_path, irr_file))

irr2 = irr1.copy()
irr2['geometry'] = irr2['geometry'].simplify(40)

irr2.to_pickle(os.path.join(dataset_path, irr_file))

irr3 = pd.read_pickle(os.path.join(dataset_path, irr_file))

paw1.to_pickle(os.path.join(dataset_path, paw_file))

paw2 = paw1.copy()
paw2['geometry'] = paw2['geometry'].simplify(40)

paw2.to_pickle(os.path.join(dataset_path, paw_file))

paw3 = pd.read_pickle(os.path.join(dataset_path, paw_file))






















