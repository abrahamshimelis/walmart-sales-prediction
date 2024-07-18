import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def check_missing_data(df):
    """
    Check for missing data in a DataFrame and return a summary of missing values.
    
    Parameters:
    - df: Pandas DataFrame
    
    Returns:
    - DataFrame or str: Summary of missing data or success message
    """
    missing_data = df.isnull().sum()
    missing_data_summary = pd.DataFrame({
        'Column Name': missing_data.index,
        'Missing Values': missing_data.values,
        'Percentage Missing': (missing_data.values / len(df)) * 100
    })
    missing_data_summary = missing_data_summary[missing_data_summary['Missing Values'] > 0]
    
    if missing_data_summary.empty:
        return "Success: No missing values."
    else:
        # Keep only the required columns
        missing_data_summary = missing_data_summary[['Column Name', 'Missing Values', 'Percentage Missing']]
        
        return missing_data_summary

def evaluate_model (model, X_test, y_test):
    y_pred_proba = model.predict(X_test)
    y_pred = np.where(y_pred_proba > 0.5, 1, 0)  # binary classification

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)

    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 Score: {f1}')
    print(f'ROC-AUC: {roc_auc}')
    
    return accuracy, precision, recall, f1, roc_auc


def generate_predictions_and_submissions(models, test_data, categories, csv_path):
    dfs = []
    for model, X_test, category in zip(models, test_data, categories):
        # Generate predictions
        predictions = model.predict(X_test)
        
        # Create a DataFrame for the predictions
        df = pd.DataFrame({
            'Month': X_test['Month'],
            'ProductCategory': category,
            'Sales(In ThousandDollars)': predictions
        })
        
        # Append the DataFrame to the list
        dfs.append(df)
    
    # Concatenate all DataFrames
    submission = pd.concat(dfs)
    
    # Sort the DataFrame
    submission.sort_values(by=['Month', 'ProductCategory'], ascending=[True, False], inplace=True)
    submission.reset_index(drop=True, inplace=True)
    submission.index = range(1, len(submission) + 1)
    submission = submission.rename_axis('Year')
    
    # Drop unnecessary columns
    submission.drop(columns=['ProductCategory', 'Month'], inplace=True)
    
    # Save the DataFrame to a CSV file
    submission.to_csv(csv_path)