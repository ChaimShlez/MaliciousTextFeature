import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')  # נכון
nltk.download('wordnet')                     # להמרה ללמה
nltk.download('omw-1.4')   
import pandas as pd
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

class DataProcessing:
    def __init__(self,data):
        self.data = pd.DataFrame(data)
        # nltk.download('stopwords')
        # nltk.download('punkt')
        # nltk.download('averaged_perceptron_tagger_eng')
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

        tagged_tokens = pos_tag(tokens)

        def get_wordnet_pos(tag):
            if tag.startswith('J'):
                return 'a'
            elif tag.startswith('V'):
                return 'v'
            elif tag.startswith('N'):
                return 'n'
            elif tag.startswith('R'):
                return 'r'
            else:
                return 'n'

        lemmatized_sentence = []

        for word, tag in tagged_tokens:
            if word.lower() == 'are' or word.lower() in ['is', 'am']:
                lemmatized_sentence.append(word)
            else:
                lemmatized_sentence.append(self.lemmatizer.lemmatize(word, get_wordnet_pos(tag)))

        return ' '.join(lemmatized_sentence)


    def processing_text(self):
        self.data['clean_text'] =  self.data['Text'].apply(self.remove_marks)
        self.data['clean_text'] = self.data['clean_text'].apply(self.replace_to_lower)
        self.data['clean_text'] = self.data['clean_text'].apply(self.remove_stop_words)
        self.data['clean_text'] = self.data['clean_text'].apply(self.Lemmatizing_text)

        return self.data





df = pd.DataFrame({
    "Text": [
        "Hello!!! This is an example, of TEXT... that we ARE going to clean.",
        "Another row: running, cars, better, amazing!!!"
    ]
})


d=DataProcessing(df)
d.processing_text()
print(d.data)
