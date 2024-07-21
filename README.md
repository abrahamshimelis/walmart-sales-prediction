# Walmart Sales Forecasting

## Project Overview
This repository contains a project that focuses on forecasting monthly and yearly sales for different Walmart product categories. The project uses historical sales data and various external datasets. The performance of the forecasting models is evaluated based on the Root Mean Squared Error (RMSE) on the test set.

## Data Preprocessing
The data preprocessing stage involves cleaning and merging multiple datasets including weather, macro economic, events and holidays, and training datasets. The cleaning process includes handling missing values, replacing certain values, calculating monthly mean for numerical columns, and more. The datasets are then merged based on 'Month' and 'Year'.

## Model Training and Evaluation
The merged dataset is split into three datasets based on 'ProductCategory': Women_clothing, Men_clothing, and Other_clothing. The data from 2009 to 2013 is used for training and the data from 2014 is used for testing. 

The following models have been trained and their performance evaluated:

- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- Support Vector Regression
- Gradient Boosting Regression

## Results
The Decision Tree Regression model had the lowest private score, and the Support Vector Regression model had the lowest public score.

## Future Work
It’s suggested to further optimize the Support Vector Regression model and explore more advanced models. Including more data like weekly sales or promotional activities could improve accuracy. Continual validation and updates are also crucial for maintaining the model’s relevance.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)