import pandas as pd
from sodapy import Socrata

token = open('secrets','r').readlines()[0].replace('\n','')


client = Socrata("data.cityofchicago.org", token)

query = """SELECT date \
    ,primary_type \
    ,description \
    ,location_description \
    ,arrest \
    ,domestic \
    ,x_coordinate \
    ,y_coordinate \
    ,latitude \
    ,longitude \
    WHERE community_area='14' and Date>='2021-01-01' \
    limit 20000000"""

results = client.get("ijzp-q8t2", query=query)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

print(results_df.columns)