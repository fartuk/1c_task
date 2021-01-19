import pickle


class TextStyleModel:
    def __init__(self,
                 model_path='model_data/model.pickle',
                 hw_path='model_data/hw.pickle',
                 tfidf_path='model_data/tfidf.pickle'):

        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(hw_path, 'rb') as f:
            self.hw = pickle.load(f) 
            
        with open(tfidf_path, 'rb') as f:
            self.tfidf = pickle.load(f)            

        
    def predict(self, text_arr):
        text_arr = [text.lower().replace('*', '').replace('\n', ' ').strip() for text in text_arr]
        X = self.tfidf.transform(self.hw.transform(text_arr).todense()).todense()
        pred = self.model.predict_proba(X)
        
        return pred
        
        
        