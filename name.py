import pandas as pd 
import plotly.figure_factory as ff
import statistics as s 
import random 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

populationMean = s.mean(data)
print(f"Population Mean : {populationMean}")
std = s.stdev(data)
print(f"Population STD : {std}")



# mean = s.mean(dataset)
# print("\nMean of sampling distribution : " , mean)

# std = s.stdev(dataset)
# print("SD of sampling distribution : " , std)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint( 0, len(data) - 1 )
        value = data[random_index]
        dataset.append( value )
    mean = s.mean(dataset)
    return mean

def setup():
    meanList = []
    for i in range(0,1000):
        setofmean = random_set_of_mean(100)
        meanList.append( setofmean )
    print(f"Mean of sampling distribution : { s.mean( meanList )  } " )
    print(f"sd of sampling distrubution : { s.stdev( meanList )  } " )
    fig = ff.create_distplot(  [ meanList ] , ["temperature"], show_hist = False)
    fig.show()
setup()

#SD of the sampling mean =  SD Population / sqrt (number of data in each sample)
# sd of sampling mean = 5.699/ sqrt(100)
# sd of sampling mean = 5.699 / 10
