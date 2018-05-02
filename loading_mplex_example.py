import scipy
import scipy.io
import pymnet


def load_layer(net,filename,threshold=0):
    m=scipy.io.loadmat(filename)["adj"]
    n=len(m)
    for i in range(n):
        for j in range(i+1,n):
            w=m[i,j]
            if abs(w)>0.8:
                net[i,j]=w

def load_mplex(filenames,netnames,threshold=0):
    net=pymnet.MultiplexNetwork(couplings='none')
    for fn,nn in zip(filenames,netnames):
        net.add_layer(nn)
        load_layer(net.A[nn],fn,threshold=threshold)
    return net


#net=pymnet.MultiplexNetwork(couplings='none')
#net.add_layer('test')
#fn="/private/tmp/braindata/ABIDE/NT/Leuven_1_0050682_rois_cc400.mat"
#load_layer(net.A["test"],fn,threshold=0.9)

filenames=["/private/tmp/braindata/ABIDE/NT/Leuven_1_0050682_rois_cc400.mat","/private/tmp/braindata/ABIDE/NT/Leuven_1_0050683_rois_cc400.mat"]
netnames=["Leuven_1_0050682","Leuven_1_0050683"]
net=load_mplex(filenames,netnames,threshold=0.8)
