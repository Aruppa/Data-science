# Extract and read data
'''import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep =",")
print(health_data.head())'''


# Remove blank row
'''import pandas as pd
health_data = pd.read_csv("remove.csv" , header=0,sep=",")
health_data.dropna(axis=0,inplace=True)
print(health_data)'''

# Data type information
'''import pandas as pd
health_data = pd.read_csv("remove.csv" , header=0,sep=",")
health_data.dropna(axis=0,inplace=True)
print(health_data.info())'''


# Convert object to float
'''import pandas as pd
health_data = pd.read_csv("remove.csv" , header=0,sep=",")
health_data.dropna(axis=0,inplace=True)
health_data["Average_Pulse"] = health_data["Average_Pulse"].astype(float) 
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float) 
print(health_data.info())'''


import pandas
mydataset = {
    'cars':  ["BMW", "Volvo", "Toyoto"],
    'passing':  [3, 7, 9]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)
