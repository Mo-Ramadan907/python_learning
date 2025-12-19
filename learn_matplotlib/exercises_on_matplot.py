import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(1,11)
y = np.random.randint(low=-2,high=100,size=10)
y1 = np.random.randint(low=0,high = 15,size=10)
y2 = np.random.randint(low=10,high=800,size = 10)
plotshowing = dict(marker=".",
             markersize =10,
             markeredgecolor = "#00ff00",
             linestyle ="None",
             linewidth =3,
             )


# plt.tick_params(axis="both", colors='#0000ff', labelsize=14)
# plt.title("plotting data ",color ="#ff0000",fontsize=20,family="serif",fontweight="bold")
# plt.xlabel("number of eggs",color="#37DD0D",fontsize=20,family="serif",fontweight="bold")
# plt.ylabel("rate of things ",color="#af02e2",fontsize=20,fontweight="bold",family="serif")
# plt.plot(x,y,mfc="#e10223",**plotshowing)
# plt.plot(x,y1,mfc ="#f2810e" ,**plotshowing)
# plt.plot(x,y2,mfc = "#100500",**plotshowing)
# plt.grid(color="#0afb33",linestyle="solid",linewidth = 3)

# players = np.array(["messi","cristiano ronaldo","neymar","dyable","lewandoscki"])
# passes = np.array([20,15,33,17,10])
# plt.title("passed for players ",color ="#f10e21",fontsize=20,family="serif",fontweight="bold")
# plt.bar(players,passes,color="#ff0000")
# plt.xlabel("players")
# plt.ylabel("number of passes")

# department = ["cs","ai","it","is","ds"]
# numbers = [300,150,20,380,90]
# plt.title("department num of students")
# plt.pie(numbers,labels=department,colors=["red","blue","#0afe12","#0afeff",'#fffe12'],
#             autopct="%1.1f%%",
#             explode=[0,0,0.3,0,0])

# numbers = np.arange(0,11)
# y1 = np.random.randint(low = 2,high=15,size=11)
# plt.scatter(numbers,y1,color="red",s=50,alpha=0.8,label="class A")
# numbers =np.array([0,1,2,2,3,4,5,6,7,8,9])
# y1 = np.random.randint(low =0,high= 11,size = 11)
# plt.scatter(numbers,y1,color="blue",s=50,alpha=0.8,label="class B")
# plt.legend()
# numbers = np.random.normal(loc=60,scale=3.8,size=300)
# # numbers = np.random.randint(low=0,high=321,size=(100,100))
# plt.hist(numbers)

# fig ,ax = plt.subplots(3,3)

# ax[0,0].set_title("hello world")
# ax[0,1].set_title("my hestogram")
# ax[0,1].hist([10,11,10,12,13,14,11,15,17,18])

# plt.tight_layout()


# arr = np.arange(1,10)
# normal_arr = np.arange(1,10)
# cubic =  arr**3
# four_power = arr**4 
# arr = arr**2

# plt.plot(normal_arr,arr,color="#ff0000",marker='.',mfc="blue",ms=10,label="square")
# plt.plot(normal_arr,cubic,color="#00ff00",marker=".",mfc="blue",ms=10,label="cube")
# plt.plot(normal_arr,four_power,color="#0000ff",marker=".",mfc="red",ms=10,label="f-power")
# plt.legend()
# plt.show()

print(np.linspace(1,10,100))