import base64
import pickle

def encode_model(dct_model):
    dct_encoded_model = {k:base64.b64decode(pickle.dumps(v, protocol=2)) for (k,v) in dct_model.items()}
    return dct_encoded_model


def decode_model(dct_encoded_model):
    dct_decoded_model = {k: pickle.loads(base64.standard_b64decode(v)) for (k,v) in dct_encoded_model.items()}
    return dct_decoded_model

"""
#sample dct_model
dct_model = {'tfidf':tfidf.fit(xtrain),
             'naivebayes': naivebayes.fit(xtrain)}
"""