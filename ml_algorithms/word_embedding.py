
import pandas as pd
from nltk.corpus import stopwords


class WordEmbedding(object):

    """
    Manual implementaition of
    1. Count Matrix
    2. TF-IDF matrix
    3. Co-Occurence Matrix

    """
    def __init__(self):
        pass

    def remove_stopwords(self, data):
        """
        :param data: string
        :return: string
        """
        stop_words = set(stopwords.words('english'))
        stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '@,'
                                                                                            '}'])  # remove it if you need punctuation
        sentence = data.split()
        for word in sentence:
            if word.lower() in stop_words:
                sentence.remove(word)

        new_data = " ".join(sentence)

        return new_data

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

    def co_occurence(self,dataset,stop_word_condition,context_window_size):
        """
        :param datset: list of strings
        :return: pandas dataframe comprising of co occurence matrix
        """
        new_data=[]
        if stop_word_condition is True:
            for doc in dataset:
                new_doc = self.remove_stopwords(doc)
                new_data.append(new_doc)
            dataset = new_data

        vocab = self.vocab_construction(dataset)
        vocab=list(vocab)
        co_matrix = pd.DataFrame(columns=vocab,index=vocab)
        co_matrix.fillna(0,inplace=True)

        indexes = co_matrix.index.values
        columns = co_matrix.columns.values

        for i in indexes:
            counter = 0
            for c in columns:
                counter = self.search(i,j,dataset)
                co_matrix[i][j]=counter
                counter = 0



        print(co_matrix)


if __name__=="__main__":
    data = ["i am here", "you are there", "lets go to ooty"]
    obj = WordEmbedding()
    obj.co_occurence(data,True,3)
