

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