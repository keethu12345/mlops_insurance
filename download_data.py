import pandas as pd

url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
df = pd.read_csv(url)
df.to_csv("insurance.csv", index=False)

print("✅ Dataset downloaded and saved as insurance.csv")