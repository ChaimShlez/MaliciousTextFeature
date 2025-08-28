import re
from datetime import datetime
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Features:
    def __init__(self, weapons):
        self.weapons = weapons.split()
        self.data= None 
        nltk.download('vader_lexicon')
        self.analyzer = SentimentIntensityAnalyzer()

    def finding_emotion_text(self,tweet):
        score = self.analyzer.polarity_scores(tweet)
        compound = score['compound']
        if 0.5 < compound <= 1:
            return 'positive'
        elif -0.49 <= compound <= 0.49:
            return 'neutral'
        elif -1 <= compound < -0.5:
            return 'negative'


    def find_weapons(self,text):
        weapons_list=[]
        words = text.split()
        for weapon in self.weapons:
            if weapon in words:
                weapons_list.append(weapon)
        return weapons_list

    def date_extraction(self,text):
        matches = re.findall(r'\d{4}-\d{2}-\d{2}', text)
        if not matches:
            return None
        dates = []
        for match in matches:
          dates.append(datetime.strptime(match, '%Y-%m-%d').date())
        max_date = max(dates)
        return str(max_date)


    def add_features(self, data):
        self.data = pd.DataFrame(data)
        self.data['Sentiment'] = self.data['clean_text'].apply(self.finding_emotion_text)
        self.data['weapons_detected'] = self.data['clean_text'].apply(self.find_weapons)
        self.data['relevant_timestamp']=self.data['text'].apply(self.date_extraction)
        return self.data.to_dict(orient='records')
