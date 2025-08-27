import pandas as pd

class DataSplitter:

    @staticmethod
    def split_by_col(data):
        data = pd.DataFrame(data)
        dict_split_antisemitic = {}
        dict_split_antisemitic["antisemitic"] = data[data['Antisemitic'] == '1']
        dict_split_antisemitic["not_antisemitic"] = data[data['Antisemitic'] == '0']
        return dict_split_antisemitic
