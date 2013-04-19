Welcome to the Open Contracting Data Spike
==========================================

The report with visualizations can be seen here: http://birdsarah.github.io/oc-datamerge-spike/ 

Contents
--------
At the top level, the presentation is available

/draft-standard - contains the created initial standards as a working document for discussion
/maps - contains the mapping between the draft standard and the data sources that were used 
/merge-spike - step one of doing a full data merge with the generated maps (currently only does one field)
/raw-data - the raw data used and the web scraping code where it was needed
/utils - random snippets of python used to work with the data
/visualization - using D3.js to make maps of the standards 

Code
----

The code is mostly python, with the D3 work in javascript. This was a spike, the code
is not future or bullet proof! It is only really here for institutional memory if this 
works goes onto a more broad phase.

If you do want to use bits though, you will need:
- MongoDB - http://www.mongodb.org
- pymongo (pip install pymongo)
- xmltodict (pip install xmltodict)
- scrapy (pip install scrapy)
- D3.js - http://d3js.org/
