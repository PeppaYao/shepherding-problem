import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X1 = np.arange(5,150,5)
#Y1 = np.array([388,303,298,405,407,396,353,350,356,395,504,596,531,739,498,506,533,594,524,535,617,675,689,700,659,589,589,630,797])
Y2 = np.array([318,317,306,339,329,382,372,360,350,365,393,383,487,484,454,449,445,465,464,461,469,502,499,517,527,536,541,584,572])
Y3 = np.array([284,294,283,341,317,329,347,363,361,399,426,412,446,459,461,445,485,487,470,484,505,501,525,519,512,561,540,556,544])

#plt.plot(X1, Y1,'-o',label='SPPL')
plt.plot(X1, Y2,'-p',label='LMAM')
plt.plot(X1, Y3,'-v',label='RMAM')

plt.xlabel("the number of sheep")
plt.ylabel("total steps")
plt.legend()
plt.grid()
plt.xticks(np.arange(5,150,10))
plt.show()