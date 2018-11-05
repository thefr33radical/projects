

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

from sklearn.preprocessing import StandardScaler
import numpy as np
class GradDescent(object):
    def compute(self):

        X=np.([1100, 1400,1425,1550,1600,1700,1700,1875,2350,2450])
        Y=np.array([199000,245000,319000,240000,312000,279000,310000,308000,405000,324000])

        Xz= StandardScaler().fit(X.reshape(1,-1))
        Xz= Xz.transform(X.reshape(1,-1))
        #Y=StandardScaler().fit_transform(Y.reshape(1,-1))
        print(Xz,Y)


if __name__ == '__main__':
    obj = GradDescent()
    obj.compute()

