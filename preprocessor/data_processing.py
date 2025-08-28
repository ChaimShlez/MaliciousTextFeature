
import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class DataProcessing:
    def __init__(self):
        self.data = None
        nltk.download('stopwords')
        nltk.download('punkt_tab')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('averaged_perceptron_tagger_eng')
        self.lemmatizer = WordNetLemmatizer()


    def remove_marks(self,text):

        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        cleaned_string = re.sub(r'\s+', ' ', text)
        final_string = cleaned_string.strip()
        return final_string

    def replace_to_lower(self,text):
        text = text.lower()
        return text

    def remove_stop_words(self,text):
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(text.lower())
        filtered = [word for word in tokens if word not in stop_words]
        return ' '.join(filtered)


    def Lemmatizing_text(self, text):
        tokens = word_tokenize(text)
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in tokens]

        return ' '.join( lemmatized_words)


    def processing_list_data(self, data):
        try:
            self.data = pd.DataFrame(data)
            self.data['clean_text'] =  self.data['text'].apply(self.remove_marks)
            self.data['clean_text'] = self.data['clean_text'].apply(self.replace_to_lower)
            self.data['clean_text'] = self.data['clean_text'].apply(self.remove_stop_words)
            self.data['clean_text'] = self.data['clean_text'].apply(self.Lemmatizing_text)
            return self.data.to_dict(orient='records')
        except Exception as e:
            print("Error2", str(e))

    # def processing_data_str(self, data_str):
    #     try:
    #         self.data = data_str
    #         self.data = self.remove_marks()
    #         self.data = self.replace_to_lower()
    #         self.data = self.remove_stop_words()
    #         self.data = self.Lemmatizing_text()
    #         return self.data
    #     except Exception as e:
    #         print("Error2", str(e))



