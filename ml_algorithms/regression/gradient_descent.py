

"""
Gradient Descent Algorithm :
    1. Statndardize values between  0 and 1
    2. Assign random values to A and  B in Y = A + X * B
    3.
        a.Compute SSEi = 1/2 * Sum<0~n>[  (Y-Yp)^2 ]
        b.Compute Error Gradients
            dSSE/dA = -(Y-Yp)
            dSSE/dB = -(Y-Yp)*X
        c.Find new A & B
            New A = A - ( r * dSSE/dA )
            New B = B -( r * dSSE/dB )

        d.Compute SSEi+1

    4. Stop when (| SSEi-SSEi+1 | ) < minimum_margin

"""

from sklearn.preprocessing import MinMaxScaler,StandardScaler
import numpy as np
import random


class GradDescent(object):

    def compute(self):

        X=np.array([1100.0, 1400,1425,1550,1600,1700,1700,1875,2350,2450])
        Y=np.array([199000,245000,319000,240000,312000,279000,310000,308000,405000,324000])
        data_len = len(X)
        scaler= MinMaxScaler()
        scaler2=StandardScaler()
        X = scaler.fit_transform(X.reshape(-1,1))
        Y = scaler.fit_transform(Y.reshape(-1, 1))
        print(" 1. Standardized ", "\n")

        a = random.choice([0.35,0.45,0.55,0.65,0.75])
        b = random.choice([0.35,0.45,0.55,0.65,0.75])
        print(" 2. Random values a,b :",a,b, "\n")

        Ypred=[]
        ypred=[]

        for i in range(0,data_len):
            ypred.append(a + X[i]*b)
            temp = a + X[i] * b
            Ypred.append(   float(   (Y[i]- temp)*(Y[i]- temp) ) )

        #print(Ypred)
        SSE = (sum(Ypred))/2
        print(" 3a.SSE:",SSE)

        dSSEa=[]
        dSSEb=[]
        for i in range(0,data_len):
            dSSEa.append( float( -(Y[i]-ypred[i]) ) )

        for i in range(0,data_len):
            dSSEb.append( float( -(Y[i]-ypred[i])*X[i] ) )

        gradA =sum(dSSEa)
        gradB = sum(dSSEb)

        print("3b. A,B : ",gradA, gradB)

        NewA= a - (0.01 * gradA)
        NewB= b - (0.01 * gradB)
        print(" 3c. NewA,NewB:", a,b)




if __name__ == '__main__':
    obj = GradDescent()
    obj.compute()

