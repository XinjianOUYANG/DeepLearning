def preprocessing(x, L, H):

    import numpy as np

    # zero padding for having constant overlap add of the window at the
    # begining of the signal to be analysed
    Nzp_beg = int(L-H)
    tmp = np.zeros(Nzp_beg)
    x = np.hstack((tmp, x))
    T = x.shape[0]

    # Number of frames - add one frame if T is not multiple of hop
    if np.mod(T, H) == 0:
        N = int(np.fix(T/H))
    else:
        N = int(np.fix(T/H) + 1)
        
    # zero padding for handling last frame
    T_zp = (N - 1)*H + L
    Nzp_end = T_zp - T
    tmp = np.zeros(Nzp_end)
    x = np.hstack((x, tmp))

    return x