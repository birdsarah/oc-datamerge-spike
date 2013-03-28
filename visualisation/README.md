To run D3 visualizations requires a webserver. For example run: 
````
python -m SimpleHTTPServer 8888
````
from the command line in this directory

Inside the data folder are the series of visualizations that are presented in the presentation that's available in the top level of this repo. The names are a little cryptic though:
/blankset - this is a visualization of just the structure of the proposed standard - slide 8
/consolidated-standard - this looks at the mapped data for each of the data sets analyzed - slide 6
/consolidated-wextra - same as consolidated standard but adds the fields that were not used by the draft standard to show the "not used" block - slide 10 & 11
/consolidated-compressed - shows the maps like consolidated-standard but compressed calls/bids and awards where appropriate (UK & Philippines) - slide 12
/consolidated-overlayed - overlays the coverage maps from consolidated-compressed and so we can examine the good and bad areas of coverage across the standards.

In the wordcloud folder is an attempt at visualizing the harmonisation challenge for the category field, but this wasn't a successful visualization and didn't make it into the presentation - slide 15. 
