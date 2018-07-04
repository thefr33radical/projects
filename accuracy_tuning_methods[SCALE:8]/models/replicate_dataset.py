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


if __name__=="__main__":
    replicator(int(input()),input(),input())