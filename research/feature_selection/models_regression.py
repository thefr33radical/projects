from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet

MODELS_REGRESSION = [RandomForestRegressor(), LinearRegression(), SVR(kernel='linear', probability=True),
                  Ridge(alpha=3), ElasticNet(alpha=1)]