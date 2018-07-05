import pandas as pd


def replicator(NO_OF_ROWS,PATH1,PATH2):
    """

    :param NO_OF_ROWS:
    :return:
    """

    dataset = pd.read_csv(PATH1, sep="\t")

    while len(dataset)<NO_OF_ROWS:
        dataset = pd.concat([dataset, dataset])

    dataset.to_csv(PATH2)
    print(len(dataset))


def csv_reader(PATH):
    data = pd.read_csv("/home/kuliza227/Downloads/YearPredictionMSD.txt",sep=",")
    new_data=data.iloc[:500000,:11]
    new_data.columns = ["AGE",	"SEX","CREDIT_SCORE",	"CIBIIL_SCORE",	"LOAN_AMT",	"ANNUAL_INCOME", "DURATION","RATING","INTEREST_RATE"," BALANCE", "RESULT"]
    new_data.to_csv("new_data.csv")
    print(new_data)


if __name__=="__main__":
    #replicator(int(input()),input(),input())
    csv_reader("")