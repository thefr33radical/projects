
import pandas as pd


class WordEmbedding(object):

    """
    Manual implementaition of
    1. Count Matrix
    2. TF-IDF matrix
    3. Co-Occurence Matrix

    """
    def __init__(self):
        pass

    def vocab_construction(self,dataset):
        """
        Function to compute vocabulary of a corpus, stopwords not removed
        :param dataset:
        :return:
        """

        vocab=set()
        for doc in dataset:
            vocab.update((doc.split()))
        return vocab

    def co_occurence(self,datset):
        """
        :param datset: list of strings
        :return: pandas dataframe comprising of co occurence matrix
        """
        vocab = self.vocab_construction(datset)
        vocab=list(vocab)
        co_matrix = pd.DataFrame(columns=vocab,index=vocab)
        co_matrix.fillna(0,inplace=True)
        print(co_matrix)


if __name__=="__main__":
    data = ["i am here", "you are there", "lets go to ooty"]
    obj = WordEmbedding()
    obj.co_occurence(data)
