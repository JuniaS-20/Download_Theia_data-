# Download_Theia_data-
This code  allow to automatically  download more than one tile  of  data delivered by  THEIA LAND.
It allows to download products delivered  by THEIA LAND : - Sentinel 2 level 2A (TOC: Top of canopy or Bottom of atmosphere) or 3A (the images obtained from the synthesis of level 2A images), processed by MAJA the Cnes algorithm.  - Landsat L2A products - Venus and   SpotWorldHeritage L1C products using the download code theia_download.py provided here https://github.com/olivierhagolle/theia_download. 
This peace of code allows to launch at once a command that automatically downloads the tiles covering the area of interest.
To make it work, we  need to adapt the Tiles tuple which contains the tiles we need in the tuple, the init_date and end_date variables which provide the start and end date of the download respectively, as well as dir_out which is the directory where the downloaded data will be stored. 
Example : to download the Sentinel 2 images of 4 tiles covering the Dordogne department in France, for the year 2018
Tiles = (‘T30TYQ’,’T30TYR’,’T31TCL’,’T31TCK’)
init_date = ‘2018-01-01’
end_date = ‘2018-12-31’
dir_out = ‘F:/Sentinel2/Dordogne/Images_2018’
as we wish to acquire the synthetic images, we will have to specify it in the Download_Theia_data function, by writing '-c SENTINEL2 - level LEVEL3A' . To know more about other parameters like the cloud rate read the README on Olivier Hagolle's github, link given above.
NB: for this code to work you must:
* Have a THEIA LAND account
*Download the code theia_download.py and accompanying files, fill in the username and password of your THEIA account in the file config_theia.cfg
*Place this code Download_Theia_data in the directory where you have stored the above mentioned files.
