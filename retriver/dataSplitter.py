import pandas as pd

class DataSplitter:

    @staticmethod
    def split_by_col(data):
        dict_split_antisemitic = {
            "antisemitic": [],
            "not_antisemitic": []
        }
        for record in data:
            record['_id'] = str(record['_id'])
            record['CreateDate'] = str(record['CreateDate'])
            if record['Antisemitic'] == 1:
                dict_split_antisemitic["antisemitic"].append(record) 
            else:    
                dict_split_antisemitic["not_antisemitic"].append(record) 
        return dict_split_antisemitic
