import openml
import pandas as pd


def getDatasets(limit=True):
    if limit == True:
        datasets = openml.datasets.list_datasets(output_format="dataframe").head(1)
    else:
        datasets = openml.datasets.list_datasets(output_format="dataframe")


    print(pd.DataFrame(datasets[["did", "name", "NumberOfInstances", "NumberOfFeatures"]]))
    return datasets
