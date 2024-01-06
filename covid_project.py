import requests
import json
import pandas as pd

api_response = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(type(api_response))

print(api_response.status_code)
data = api_response.json()
#print(data)

#data = api_response.text

# with open('covid_project.txt', 'w') as f:
#           f.write(data)

# actives = data['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
# #print(actives)

# deceased = data['Andaman and Nicobar Islands']['districtData']['South Andaman']['deceased']
# #print(deceased)


# df = pd.DataFrame.from_dict(data, orient = 'columns')
# #print(df)
district_dataframes = {}

# for state, district_data in data.items():
#     for district, district_stats in district_data.get("districtData", {}).items():
#         # Create a DataFrame for each district
#         df = pd.DataFrame(district_stats)
        
#         # Store the DataFrame in the dictionary
#         district_dataframes[(state, district)] = df

# # Print DataFrames after the loop
# for (state, district), df in district_dataframes.items():
#     print(f"State: {state}, District: {district}")
#     print(df)
#     print("\n" + "="*40 + "\n")

for state, district_data in data.items():
    for district, district_stats in district_data.get("districtData", {}).items():
        # Flatten the "delta" dictionary into separate columns
        flat_delta = {"delta_" + key: value for key, value in district_stats.get("delta", {}).items()}
        
        # Combine all data into a single dictionary
        combined_data = {**district_stats, **flat_delta}
        
        # Create a DataFrame for each district
        df = pd.DataFrame([combined_data])
        
        # Store the DataFrame in the dictionary
        district_dataframes[(state, district)] = df

# Concatenate DataFrames to create a single DataFrame
result_df = pd.concat(district_dataframes.values(), keys=district_dataframes.keys())

# Print the result DataFrame


# result_df.rename(index={0: "State", 1: "District"}, inplace=True)
# #df.rename(index={0: "x", 1: "y", 2: "z"})
# print(result_df)


sum_active = sum(result_df['active'])
print(sum_active)
result_df.to_csv('covid_project.csv')

covid_report = pd.read_csv('covid_project.csv')

covid_report = covid_report.rename(columns = {'Unnamed: 0' : 'State', 'Unnamed: 1' : 'District', 'Unnamed: 2': 'delete'})



#monthly_report = monthly_report.drop('delete', axis=1)
covid_report = covid_report.drop('delete', axis=1)

print(covid_report.head())
covid_report.to_csv('covid_report_final.csv')