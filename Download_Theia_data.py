# -*- coding: Latin-1 -*-
#########################
# Importing module
#########################

import os

#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====
# Definition of the function
#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====



def download_tiles(tile, date_init, date_end, dir_write):
    cli='python theia_download.py -t ' + tile + ' -a config_theia.cfg -d ' + date_init + ' -f ' + date_end + ' -c SENTINEL2  ' + ' -w '+ dir_write
    os.system(cli)
    
    
#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====
# Declaration and assignment of variables 
#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====



tiles = ('T30TYQ','T30TYR','T31TCL','T31TCK')
init_date = '2018-01-01'
end_date = '2018-12-31'
dir_out = 'F:/Sentinel2/Dordogne/2017-2018' #F:\Dordogne


#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====
# Code execution 
#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====



for tuile in tiles:
    download_tiles(tuile,init_date,end_date, dir_out)
    
    
#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====
# End of the execution
#  ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ====  


print(' OK Jazz '.center(80, '*'))

