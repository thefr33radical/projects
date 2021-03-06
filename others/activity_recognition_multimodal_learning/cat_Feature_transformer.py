
import pandas as pd 
import prince
import matplotlib.pylab as plt
import category_encoders as ce

class FeatureExtract:
  def __init__(self):
    self.cat=[]
    self.ord=[]
    self.cont=[]

  def MCAX(data,cat_columns):
    """
    cat_columns: list of categorical columns
    """
    X=data[[cat_columns]]
    print(X.head())
    mca = prince.MCA()

    mca = mca.fit(X) # same as calling ca.fs_r(1)
    mca = mca.transform(X) # same as calling ca.fs_r_sup(df_new) for *another* test set.
    print(mca)
    return mca

    def OneHotEncode(self,data,column):
        encoder = ce.OneHotEncoder(cols=[column], return_df=True)
        return encoder.fit_transform(data)

    # High Cardinality of Features
    def FeatureHasher(selfself,data,column,components):
        encoder = ce.HashingEncoder(cols=column, n_components=components)
        return encoder.fit_transform(data)

    def LabelEncoding(self,data,column):
        encoder = ce.OrdinalEncoder(cols=[column], return_df=True)
        return encoder.fit_transform(data)

    # High Cardinality of Features
    def BinaryEncoder(self,data,column):
        encoder = ce.BinaryEncoder(cols=[column], return_df=True)
        return encoder.fit_transform(data)

    def feature_encode(self,data):
        l=[]
        for col in data.columns:
            n=data.groupby([col])
            if n.ngroups >10000 :
                continue
            if n.ngroups <10000 and n.ngroups > 1000:
                l.append(self.BinaryEncoder(data,col,25))
                continue
            if n.ngroups < 1000 and n.groups >10:
                l.append(self.FeatureHasher(data, col, 15))
                continue

  


