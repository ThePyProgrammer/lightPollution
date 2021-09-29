# An Analysis of The Global Light Pollution Standards

**Prannaya Gupta (M21404)**


## Introduction
A side-effect of technological advancement has been the amount of light pollution in the world today. Ever since Thomas Edison’s revolutionary invention of the light bulb, the world has been thrust into a landscape of light-afflicted skies. According to various studies, around 80% of people live under light pollution-afflicted skies every day, and whilst this may not affect the day-to-day life of an individual, astronomers are very much affected by the sudden illumination in the skies. Even the Singaporean sky is very much damaged by light pollution, with 99.5% of all stars being completely invisible without optical aid<sup>[22]</sup>.


## Research Questions

### A.	What are locations of minimal light pollution intensity which are optimum for astronomical observation?

While one might think that the best locations are in the middle of wilderness or large water bodies (i.e. the ocean), these locations need to be filtered based on accessibility, especially since locations like the middle of the ocean are not feasible locations for people to assemble to watch and will thus not be a great location for astrophotography.

In order to map this, I can use the absolute night-time light datasets<sup>[4-7]</sup> to analyse locations of minimal light intensity. In order to do the filtering of data, I can use the Base Map<sup>[8]</sup> and Matplotlib’s BaseMap Library<sup>[26]</sup>. This can give us a few optimum points best for this type of analysis.


### B.	How has the light pollution data around the world changed? Which countries are most susceptible to high light pollution in the future? Which countries are lessening in terms of light pollution?

There are many countries that have had rampant increases in Light Pollution over the past few years, while others have made an effort to reduce their already increased Light Pollution. We need to map the data in order to find out which countries are susceptible to the level of problematic light pollution that can be found in cities like Singapore.

Due to the possession of the Time Series Data of night-time light pollution data<sup>[1-3]</sup>, we can easily map locations based on relative changes in absolute light magnitude. I intend to use the geolocation datasets<sup>[9-12]</sup> against the time-series night-time light datasets<sup>[1,17]</sup> to find changes and from there and map it using a possible regression model so as to predict the curve of increase/decrease. This can be used to make predictions and compare to other light pollution levels.


### C. What are the impacts of Light Pollution on the Biodiversity around the area?

High Light Pollution can have a detrimental impact on animals’ survival, hence they are likely to be found in areas with lesser light pollution, which can be adopted as a hypothesis. Another investigation could be what types of animals can be found closer to Light pollution related areas. For example, Moths should ideally be found in high light pollution, but endangered species will likely not be found in similar areas.

Based on the eBird Observation Dataset<sup>[13]</sup>, we can find relative values symbolising the animals’ survival patterns and frequency of observations, thereby relating it to Time Series Night-time Light Data so as to procure information regarding how the birds have moved about in the presence of light pollution. The International Barcode of Life dataset<sup>[14]</sup> is also a logical dataset to not only map frequency patterns but also classify the observations based on existing models and thus finding frequencies of these animals based on Time Series Light Pollution.


### D.	What are the effects and relevance of different types of light facilities on light pollution in the area

One of the factors claimed culpable for the increased light pollution in Singapore is the extreme number of street lights and traffic lights. Hence, I wish to investigate how the frequency of these lights affect the light pollution around the area. I also want to find possible weights to see how relevant these frequencies are.

With the presence of the Light Facilities Datasets<sup>[15-19]</sup>, we can map this on the Absolute Positional Brightness Dataset<sup>[4-7]</sup> so that we can investigate how it’s affects the actual brightness, whilst we can also investigate how it changes with respect to time by using the Time Series night-light data<sup>[1-3]</sup> and the time based datasets<sup>[15,19]</sup>. This can then be used to compute possible patterns and predictions regarding where the Singapore light pollution may lead up to. To consider Singapore alone, I will be using Geopy<sup>[25]</sup> for the most part and filtering coordinates based on available geographical information.


### E.	What is the relation between the average energy consumption and general demographics in each area (eg Tampines, Jurong etc) and the Light Pollution?

A reason for considering this is the lack of mathematical analysis as to how energy consumption in specific districts affect the light pollution there. General mathematics regarding data in Singapore itself hasn’t been explored, hence using this is a good way of exploring something new. We can model the types of houses, general types of people living there, and the energy consumption based on that and from there, we can test how it affects nearby light pollution.

I intend to use the Economical Datasets that give data regarding the Singapore Energy Consumption statistics<sup>[20]</sup> and the Singapore Resident demographics<sup>[21]</sup>. The usage of the Absolute positional brightness datasets<sup>[4-7]</sup>, filtering Singapore similarly to the previous research question. This can therefore be using in conjunction to find possible patterns.