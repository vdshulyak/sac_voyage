from pathlib import Path
import pandas as pd
import locale
import csv

budget_data = pd.read_csv("C:/Users/racon/OneDrive/Desktop/python-homework/PyBank/budget_data.csv")
Total_Month = budget_data.shape[0]
total = budget_data["Profit/Losses"].sum().round(2)
#currency_total = "${:,.2f}".format(total)
diffs = budget_data.set_index("Date").diff().dropna().sort_values(by = ["Profit/Losses"])

min_diff = diffs.head(1)
max_diff = diffs.tail(1)


max_month=max_diff.index.values
max_value = max_diff.values
min_month=min_diff.index.values
min_value = min_diff.values

sorted_diff = diffs.sort_values(by =  "Profit/Losses").dropna()
avg_diff = round(diffs["Profit/Losses"].mean(),2)

result =[]
a ="Financial Analysis"
print(a)
result.append(a)
        
b = ("------------------------")
print(b)
result.append(b)

c = (f"Total Months:{Total_Month}")
print(c)
result.append(c)

x =(f"Total: {total}")
print(x)
result.append(x)
x =(f"Average Change:{avg_diff}")
print(x)
result.append(x)
x =(f"Greatest Increase in Profits: {str(max_month).strip('[]')} {str(max_value).strip('[]')}")
print(x)
result.append(x)
x = (f"Greatest Decrease in Profits: {str(min_month).strip('[]')} {str(min_value).strip('[]')}")
print(x)
result.append(x)
print(result)


with open("Financial_Analysis.csv", 'w+', newline='') as f: 

    w = csv.writer(f)
    w.writerows(result)
    f.close
    
text = open("Financial_Analysis.csv", "r")
text = ''.join([i for i in text]) \
    .replace(",", "")
x = open("Financial_Analysis output.csv","w")
x.writelines(text)
x.close()