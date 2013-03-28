Welcome to the Open Contracting Data Spike
==========================================

The objective was to spend 5 days exploring the feasibility of developing a common
standard for open contracting data and scoping the opportunities and challenges.

This work was "supply-side" only, meaning that it looked at a number of available data
sets to examine the problem rather than looking at the "demand-side" - what information
do stakeholders want.

In addition to examining feasibility, opportunities and challenges, a draft standard 
was produced in order to provide something on paper for people to engage with - the draft
included here is in no way an accepted or agreed standard, mearly a talking point.

This work was presented at the ODI with http://www.open-contracting.org/ on March 28th 2013.

The following data was looked at during this project:
- UK Contracts Finder - https://online.contractsfinder.businesslink.gov.uk/
- Philippines - http://www.philgeps.gov.ph
- USA Spending - http://www.usaspending.gov/
- Colombia - https://www.contratos.gov.co/consultas/inicioConsulta.do
- World Bank - https://finances.worldbank.org/Procurement/Major-Contract-Awards/kdui-wcs3?
- Guinea - http://www.contratsminiersguinee.org/

The Guinea data was not used in the mapping as it was too disparate to facilitate the process that we were 
trying to do. However, bringing in extractive industry and other such disparate data will be an important 
part of future work. The US data was only partially looked at, specifically to look at the transaction 
data available.

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
