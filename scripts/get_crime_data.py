import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", token)

query = """SELECT * WHERE community_id='14' and Date>='2021-01-01' \
limit 20000000"""

results = client.get("ijzp-q8t2")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
