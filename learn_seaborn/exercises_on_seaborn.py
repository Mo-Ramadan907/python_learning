import seaborn as sns

iris = sns.load_dataset("iris")

sns.scatterplot(x="sepal_length",y="species",data=iris,hue="petal_width",palette="YlGnBu")