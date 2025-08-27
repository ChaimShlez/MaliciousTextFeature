from connectionWrapper import ConnectionWrapper
from datetime import datetime

class Main():

    def __init__(self):
        self.mongo_client = ConnectionWrapper()


    def run(self):
        start_date = datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        while True:
            try: 
                data = self.get_100_doc(start_date)
                start_date = data[-1]['CreateDate']
            except Exception as e:
                print(str(e))
                return {"Error" : str(e)}

    def get_100_doc(self, start_date):
        return self.mongo_client.get_data(start_date)
    
if __name__ == "__main__":
    main = Main()
    main.run()
    





