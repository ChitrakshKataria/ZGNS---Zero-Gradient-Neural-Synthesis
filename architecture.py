import openml
import pandas as pd

def getDatasets(amount=1):
    datasets = openml.datasets.list_datasets(output_format="dataframe")
    print(pd.DataFrame(datasets[["did", "name", "NumberOfInstances", "NumberOfFeatures"]]))
