## Background

This repository contains the work of our team in developing an anomaly detection system for the National Railway Company of Belgium (SNCB) on Belgian Railways Class 41. Our task is to analyze real-life time series data from diesel trains to detect and distinguish anomalies within their cooling systems. Anomalies could indicate various issues such as sensor failures, problems within a single cooling system, or more critical engine-wide problems that could lead to service interruptions or train incidents.
More information about AR41(Belgian Railways Class 41) is available at: https://fr.wikipedia.org/wiki/S%C3%A9rie_41_SNCB, https://ferrovia.be/Trains_Materiel_Autorail_SNCB-NMBS_AR-MW_41.php

## Project Goals

The goal of this project is to provide a robust method for detecting and explaining anomalies in train engine cooling systems. By leveraging historical data and incorporating weather information, we aim to predict and prevent potential failures, preserving vehicle health and preventing train incidents.

## Dataset Overview

We are given a 2GB CSV file containing time series data from January 2023 to September 2023. The data includes various measurements such as engine temperatures, pressures, RPMs, and GPS locations of the trains. This dataset presents several challenges, including non-uniform sampling times, duplicates, and erroneous readings such as zeroed GPS positions or temperatures.

You can access the dataset at: https://drive.google.com/file/d/1AuKXD1Ti11JkcOOwOLxInbUGKFFJk-8j/view

### Maximum Acceptable Temperatures

- Air: 65°C
- Water: 100°C
- Oil: 115°C

Temperatures above these thresholds will automatically stop the engines to prevent damage.

## Repository Structure

- `data/` - Contains the dataset and any additional data files.
- `notebooks/` - Jupyter notebooks with detailed analysis, exploration, and model development.
- `src/` - Source code for the anomaly detection methods and dashboard.
- `presentation/` - The presentation of our work and results in PDF format.
- `dashboard/` - Code and resources for the live dashboard demo.
- `requirement/` - Stored all the requirements and useful information for this project. 

# Getting Started

To get started with our anomaly detection project, follow these steps to access and run our code on Kaggle:

### Prerequisites

Before you begin, make sure you have an account on [Kaggle](https://www.kaggle.com). If you do not have an account, you can sign up for free.

### Accessing the Notebooks

1. **Navigate to the Project on Kaggle**:
   - Our project is hosted on Kaggle, and you can find all the related Jupyter Notebooks in our Kaggle workspace. 
   - Visit our [Kaggle project page](link-to-your-kaggle-project) to view the notebooks and datasets.

2. **Fork the Notebook**:
   - Once you are on the project page, you can see a list of available notebooks. Click on the notebook you are interested in.
   - To run or edit the notebook, click the "Copy and Edit" button. This will create a fork of the notebook in your own Kaggle account, allowing you to execute the code and make changes without affecting the original notebook.

3. **Run the Notebook**:
   - After forking the notebook, Kaggle will open an interactive session for you. Here, you can run the code cells one by one or run the entire notebook.
   - To run a single code cell, click on the cell and then press the "Run" button. To run all cells in the notebook, use the "Run All" option at the top of the notebook.

4. **Interact with the Notebook**:
   - You can interact with the data, tweak parameters, and experiment with different models directly within your browser.
   - If you have any suggestions or improvements, feel free to tweak the notebook and then save your changes.


## Group Members

- Yutao Chen
- Benjamin Gold
- Min Zhang
- Xianyun Zhuang

## License

The project will be openly licensed, allowing for reuse and collaboration within the data science community.

## Acknowledgments



---

This README is a living document and will be updated regularly to reflect the progress and changes in the project's scope and direction. We encourage collaboration and feedback. If you encounter any problems or have suggestions, please create an issue or pull request on GitHub.
