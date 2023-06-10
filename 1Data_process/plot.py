import torch
import matplotlib.pyplot as plt

x = [20,40,60,80,100,120,140,160]
t1 = torch.tensor([4.513609713434879,4.144460103372793,3.8051402946963226,3.540796985070212,3.307183996183451,3.122983793572847,3.0203891499392563,2.836936539553493])
t2 = torch.tensor([4.575977599845,4.378759235866605,4.174283055742484,3.982795368184635,3.800914739675879,3.6326673314299915,3.483954167087866,3.3521816236869593])
t3 = torch.tensor([4.911354948941902,4.778559821089313,4.694523969230683,4.633126901113152,4.583682534620573,4.542704699316892,4.506271841697614,4.474170136889001])
plt.plot(x,t1,label='lr=0.1')
plt.plot(x,t2,label='lr=0.05')
plt.plot(x,t3,label='lr=0.01')
plt.title('ciaoDVD')
plt.xlabel('communication round')
plt.ylabel('rmse')
plt.legend()
plt.grid()
plt.show()