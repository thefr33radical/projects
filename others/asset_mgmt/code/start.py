import preprocess
print("SMS Case Study, modules initialized ")
print("Note : EDA module needs to be run manually. ")
preprocess.compute()
print("preprocess module completed. o/p file in data dir")
import FEATURE_ENGI
FEATURE_ENGI.feature_maker("main")
print("feature eng module completed. o/p file in data/global/processed dir")
import models
models.compute()
print(" train/Test module completed results are stored in logs/models.log file")