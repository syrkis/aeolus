---
title: A Geospatial Exploration of Wind Energy in Brazil
author: Noah Syrkis & Christina Gaitanou
geometry: margin=3cm
fontsize: 12pt
---
## Abstract

Brazil is a country with large renewable energy potential.
In this report, we explore the potential for wind energy in Brazil.
Using the tools of geospatial data science, we connect meteorological, demographic, topological, and infrastructure data to better understand this potential.
We find that wind energy is a viable option for Brazil, and that the country has the potential to become a world leader in wind energy production.

## Introduction

Wind energy is a renewable energy source that has been growing in popularity in recent years. 


## Literature Review

@zhang2015 @abdalla2022 write something here. @yu2022 is cool as well. @winkler2012 can't go without mentioning (@ulak2019).


### Wind Energy

Wind energy is a renewable energy source that has been growing in popularity in recent years. There are many reasons for this growth. Part of it is the existence of large investments funds such as [Copenhagen Infrastructure Partners (CIP)](https://www.cipartners.dk/), which has invested in wind energy projects in Brazil. Another reason is the increasing efficiency of wind turbines, which has made wind energy more economically viable. Finally, the increasing concern about climate change along with the high demand on energy supply, have led to a push for renewable energy sources, such as wind energy, globally. 

### Brazil


Renewable energy development relies on the establishment of effective political efforts and economic interventions @we_brazil, thus the political and economical state of any country directly affect the decisions and constructions regarding energy supply.
Brazil has a history of political instability, which makes it difficult to invest in long-term projects. In addition, Brazil is quite polarised politically, with recent administrations being anti-environmentalist. Finally, Brazil has a history of corruption, which makes it difficult to invest in long-term projects; complicated legal systems; and a lack of transparency.

However, Brazil is in many ways also on the forefront of environmentalism, having played an important role in the Paris Agreement and having a large renewable energy sector. Al Gore has called Brazil "a leader in the global effort to combat climate change". Alfredo Sirkis, a Brazilian politician and environmentalist, has called Brazil "the most important country in the world for the future of the environment".  

// population 

### Wind Energy in Brazil

Brazil is a country with large renewable energy potential; its large land area and coastline  makes it a great candidate for both offshore and on shore wind farm installations. Brazil's increasing demand and strong industrial base enhances its potential @we_brazil. The country stands out for its successful implementation of wind energy resources and capacity, including the development cost @overcoming_barriers.  More specifically, "Brazil has the eighth larger installed wind energy capacity in the world", according to Neilton Fidelis da Silva @utilization_we.  Between 2008 and 2017, the capacity grew 37 times nationally and reached 12,770 MW. @overcoming_barriers. Only the Northeast region has reported an average capacity that is much more than the averages of many countries around the world @overcoming_barriers. Additionally, the generation forecasts are pretty reliable with strong and stable trade winds, that makes the country a suitable region. However, there have been studies on the barriers one has to consider in wind farm constructions in Brazil. Among others, the unstable macroeconomic environment and inadequate access to capital, with the poor transmission infrastructure to be identified as the most impactful one (regarding on shore wind farms) @overcoming_barriers.

For this project's purposes, we will consider the domain of locations for wind farm installations both on shore and off shore across Brazil, due to the country's strong potential of wind farm construction. 

## Data

The main objective of this project is to use Geospatial Data science techniques to identify and recommend the optimal location of wind farm constructions across Brazil. For achieving this, we firstly have to acquire and understand Geospatial Datasets relevant to the goals of this project, in order to later use the information they provide productively and meaningfully. This section will investigate, explore and analyse the different types of data we will be using following our common sense and relevant literature review on the subject. Since utilising the data appropriately is one of the most important aspects of this project, we will spend time on exploratory analysis before we attempt to combine the datasets for an optimal result. That being said,  criteria and constrains for each dataset will be identified and modified along the way. 

### Meteorological 
- Global Wind Atlas [https://globalwindatlas.info/en] 

### Demographic
something

### Topological

For the topological data, we start with gathering elevation data for Brazil from a Digital Elevation Model (DEM) which is a type of raster geospatial data. Essentially, DEM is a 3D representation of the terrain's surface created from elevation data, excluding any objects like buildings and vegetation. We acquired the elevation data for the country of Brazil from [http://www.diva-gis.org/gdata]. We will use these to also calculate the slope, as the rate of maximum change in elevation. For this calculation, we will have to convert the Geographic Coordinate System (CRS) to be described in meters instead of degrees. In other words, instead of working with a 3D representation, will have to transform the data into a flat 2D space such as the Projected Coordinate System (PCS) before performing analysis. 

Constrains to consider in elevation : 

1. **Elevation**: Wind farms are usually located at higher altitudes where the wind is stronger, so areas with low elevation might not be suitable.
    
2. **Slope**: The terrain should not be too steep for construction and maintenance of wind turbines. You can calculate the slope from the elevation data using a slope function. This will give you another raster where each cell value represents the steepness of the terrain. You can then set a threshold slope above which the terrain is considered too steep for a wind farm.
    
3. **Aspect**: The aspect, or the compass direction that a slope faces, can also affect the suitability of a location for a wind farm. For example, in some areas, the prevailing wind direction could make certain aspects more desirable.

--Multi-level constraints wind farms siting for a complex terrain in a tropical region using MCDM approach coupled with GIS
--GIS-BASED METHOD FOR WIND FARM LOCATION MULTI-CRITERIA ANALYSIS 

-  Land Cover Data
- Road Networks
- Transmission Lines
- Protected Areas and Environmental Constraints

### Infrastructure
something

## Methodology

### Data Preprocessing

### Exploratory Data Analysis

### Model Selection

### Model Evaluation

## Results

## Discussion

## Conclusion

## References

<div id='refs'></div>

## Appendix
