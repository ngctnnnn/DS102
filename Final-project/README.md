<div align='center'>

## Predict landslide disaster based on natural factors 
</div>

### Table of content
1. [Introduction](#1-introduction)

----
#### 1. Introduction
##### Dataset
- Taken from [Visual Crossing Weather's API](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/)

#### Methods

#### 2. Repo structure
- **data**
    - **GLC.csv**: the official Global Landslide Catalog from NASA [1]
    - **weather.json**: metadata taken from API's scrapping
    - **weather.csv**: data transformed from the original metadata
- **constant.py**
- **json_to_csv.py**: transform metadata from `json` to `csv`
- **scrape_api.py**: scrap metadata from Visual Crossing Weather's official API
- **merge_data.ipynb**: for joining transformed csv data into GLC's original data to add more features to the dataset
- **.gitignore**

#### References
[1] Kirschbaum, D.B., Stanley, T., & Zhou, Y. (2015). Spatial and temporal analysis of a global landslide catalog. Geomorphology, 249, 4-15. doi: [10.1016/j.geomorph.2015.03.016](https://doi.org/10.1016/j.geomorph.2015.03.016)[1-s2.0-S0169555X15001579-main.pdf](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1e074cb1-2a0f-4062-956d-2b2a9bc13400/1-s2.0-S0169555X15001579-main.pdf)      