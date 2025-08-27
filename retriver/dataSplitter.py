class DataSplitter:

    @staticmethod
    def split_by_col(data):
        dict_split_antisemitic = {}
        dict_split_antisemitic["antisemitic"] = data[data['Antisemitic'] == '1']
        dict_split_antisemitic["not_antisemitic"] = data[data['Antisemitic'] == '0']
        return dict_split_antisemitic
