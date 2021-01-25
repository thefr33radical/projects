import pandas as pd
import os
import sys
import logging
import json
logging.basicConfig(level=logging.INFO,filename=os.getcwd()+ "/logs/app.log", filemode='a')

class Agg:
    def __init__(self):
        self.p_name = os.getcwd() + "/history/processed.json"
        pass

    def load_logs(self,input_path):
        """
        reads all csv files under the given path
        :param input_path: string
        :return: pandas dataframe
        """
        df=pd.DataFrame()

        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith(".csv"):
                    print(file,root,dirs)
                    file_name=root+"/"+file
                    temp = pd.read_csv(file_name, low_memory=False,sep=",",index_col=False)

                    # can  run out of memory, should be processed file by file/chunks in that case
                    df = pd.concat([df, temp], axis=0)
        logging.info("Read all files Success")
        return df

    def process(self,df):
        """
        Function to split timestamp to day & aggregate o/p by day.
        :param df: pandas dataframe
        :return: None
        """

        df.columns = ["timestamp", "serviceid", "consumptionid", "consumptionvalue"]
        dat_col = df.loc[:, "timestamp"].str.split(' ', 1, expand=True)
        df.drop("timestamp", inplace=True, axis=1)
        df = pd.concat([dat_col.iloc[:, 0], df], axis=1)
        df.columns = ["timestamp", "serviceid", "consumptionid", "consumptionvalue"]
        d = df.groupby("timestamp")

        for name_of_the_group, group in d:
            op_name = name_of_the_group.replace("/", "-")
            logging.info("Wrting to file "+name_of_the_group)

            # Check for previous o/p files, merge and drop duplicates. Else create new file.
            try:
                df1 = pd.read_csv(os.getcwd()+ '/output/' + op_name + '.csv', low_memory=False, sep=",",index_col=False)
                df1.columns = ["timestamp", "serviceid", "consumptionid", "consumptionvalue"]
                df1.reset_index(inplace=True)
                df1.drop_duplicates(keep=False, inplace=True)
                df1 = pd.concat([df1, group])
                df1.drop_duplicates(keep=False,inplace=True)
                df1.to_csv(os.getcwd() +'/output/' + op_name + '.csv', mode='w',
                             header=False,index=False)
                logging.info("Merged previous records "+name_of_the_group)
                try:
                    data = {}
                    with open(self.p_name, "r") as json_file:
                        data = json.loads(json_file.read())
                    with open(self.p_name, "w+") as op:
                        print(data)
                        data[op_name] = 1
                        print(data)
                        op.write(json.dumps(data))
                    logging.info("Processed all files Success")
                except Exception as e:
                    logging.info("Error in writing record to processed history " + str(e))
                    return 0

            except Exception as e:
                logging.info("Created file "+name_of_the_group +str(e))
                group.to_csv(os.getcwd()+ '/output/' + op_name + '.csv', index=False, mode='w',
                             header=False)
                try:
                    data={}
                    with open(self.p_name, "r") as json_file:
                        data = json.loads(json_file.read())
                    with open(self.p_name, "w+") as op:
                        data[op_name]=1
                        op.write(json.dumps(data))
                    logging.info("Processed all files Success")
                except Exception as e:
                    logging.info("Error in writing record to processed history " + str(e))
                    return 0

    def isprocessed(self,day):
        """
        Function to check if the file is already processed
        return True if already processed else False
        :param input_path: string
        :return: bool
        """
        try:
            with open(self.p_name,"r") as json_file:
                data = json.loads(json_file.read())
                print(data)
                if day in data:
                    return 1
                else:
                    return 0
        except Exception as e:
            logging.info("Record not processesd "+str(e))
            return 0

    def initiate(self,date):
        d_list=date.split("/")
        dname = date.replace("/", "-")
        input_path=os.getcwd()+"/input/"+d_list[2]+"/"+d_list[0]+"/"+d_list[1]

        # Check if records are already processed or not before transformation
        val=self.isprocessed(dname)
        if not val:
            logging.info("Record not found previously, Reading")
            df=self.load_logs(input_path)
            self.process(df)
        else:
            logging.info("Records already procesed")

    def create_op_structure(self):
        """
        Needs to be put in helper function
        Function to create a output project directory, runs once
        :return: int
        """
        op_create_path = os.getcwd() + "/history/create_op_dir.txt"
        try:
            with open(op_create_path,"r") as f:
                dat=f.read()
                return 1
        except:
            logging.info("op created")
            for dir1 in range(2019,2025):
                for dir2 in range(1,13):
                    os.makedirs(os.path.join("output",str(dir1), str(dir2)))
            with open(op_create_path,"w+") as f:
                f.write("1")

if __name__=="__main__":
    obj=Agg()
    try:
        args=str(sys.argv[1:][0])
        # To be used when parttiion by year is needed
        #obj.create_op_structure()
        logging.info("started")
        obj.initiate(args)
        logging.info("finished")
    except Exception as e:
        logging.error(str(e))


