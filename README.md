# Pump It Up: Data Mining the Water Table

## Repo Contents:
- a folder containing the data used in this project
- a folder containing relevant images
- a 'P3' notebook containing some visualizations and exploration
- a 'Model Building' notebook explaining our model and going over various iterations
- a 'Functions.py' file containing custom functions and imports used in both notebooks
- a presentation of the findings

This purpose of this project is to use Machine Learning to predict the operational status of wells located throughout Tanzania.
These wells fell into three categories: functional, functional but in need of repair, and non-functional.

The OSEMN approach was used to handle this task.

## Obtain and Scrub

The data was available for download from the competition website. Looking it over, discovered several null values, redundant columns, and placeholder values. These were dealt with in ways appropriate for each category. For example. for 0s in the 'construction_year' category, we imputed random years based on the existing spread of years.

## Explore

### Column Names and Descriptions
- amount_tsh - Total static head (amount water available to waterpoint)
- date_recorded - The date the row was entered
- funder - Who funded the well
- gps_height - Altitude of the well
- installer - Organization that installed the well
- longitude - GPS coordinate
- latitude - GPS coordinate
- wpt_name - Name of the waterpoint if there is one
- num_private -
- basin - Geographic water basin
- subvillage - Geographic location
- region - Geographic location
- region_code - Geographic location (coded)
- district_code - Geographic location (coded)
- lga - Geographic location
- ward - Geographic location
- population - Population around the well
- public_meeting - True/False
- recorded_by - Group entering this row of data
- scheme_management - Who operates the waterpoint
- scheme_name - Who operates the waterpoint
- permit - If the waterpoint is permitted
- construction_year - Year the waterpoint was constructed
- extraction_type - The kind of extraction the waterpoint uses
- extraction_type_group - The kind of extraction the waterpoint uses
- extraction_type_class - The kind of extraction the waterpoint uses
- management - How the waterpoint is managed
- management_group - How the waterpoint is managed
- payment - What the water costs
- payment_type - What the water costs
- water_quality - The quality of the water
- quality_group - The quality of the water
- quantity - The quantity of water
- quantity_group - The quantity of water
- source - The source of the water
- source_type - The source of the water
- source_class - The source of the water
- waterpoint_type - The kind of waterpoint
- waterpoint_type_group - The kind of waterpoint

There were various connections between these features and the functionality of the wells.

## Model

The models shown are a Random Forest and a grid search to tweak hyperparameters. Our final model was reasonably accurate. Results were confirmed with a confusion matrix. Overall, it was the repairable wells that were hardest to classify. 

![Final_Confusion_Matrix.png](attachment:Final_Confusion_Matrix.png)

As the confusion matrix shows, the model was better at predicting functional wells rather than, non-functional.
