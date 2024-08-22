import math


def read_freq(fn):
    data={}
    with open(fn,'r') as fi:
         for line in fi:
             aa,x,n,freq=line.strip('\n').split('\t')
             data[aa]=[int(x),int(n)]
    return data


def cal_z(data1,data2):
    for aa in data1:
        p1=data1[aa][0]/data1[aa][1]
        p2=data2[aa][0]/data2[aa][1]
        p0=(data1[aa][0]+data2[aa][0])/(data1[aa][1]+data2[aa][1])
        z=(p1-p2)/math.sqrt(p0*(1-p0)*(1/data1[aa][1]+1/data2[aa][1]))
        print('%s\t%f'%(aa,z))


B_lanA_Z=read_freq('bacteria_lanA_AA_freq.txt')
B_lanM_Z=read_freq('bacteria_lanM_AA_freq.txt')
A_lanA_Z=read_freq('archaea_lanA_AA_freq.txt')
A_lanM_Z=read_freq('archaea_lanM_AA_freq.txt')

print('lanA z-score:')
cal_z(A_lanA_Z,B_lanA_Z)
print('lanM z-score:')
cal_z(A_lanM_Z,B_lanM_Z)
