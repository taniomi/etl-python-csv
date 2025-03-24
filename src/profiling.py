import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/data.csv")

profile = ProfileReport(df)
profile.to_file("output/report.html")