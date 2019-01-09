# Cadencer
Plots cadences and does stuff

Crawls through data directories to collect MJDs of pulsar observations and collates them into either a:
- python dictionary object dumped in a pickle 
- plots using matplotlib library

Since, there are two observatories and we would want our plots to have the same style, it is advised (suggested) to make pickle files at the sites and copy them over to the same system where one can have the plots in the same style.

`cadencer.py` can do the following:
- it can take a pickle file and plot the cadence sheet
- it can take a source list and dump the pickle file
- it can take a source list and do either or both

`cadencer.py` uses regex to match filenames and directory names and extracts MJDs from it. 


_regex is so cool : J\d{4}[+-]\d{2,4}[AB]*[_.](\d{5})\S*[prof,tim]*_
