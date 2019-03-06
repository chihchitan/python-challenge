import pandas as pd

#set file path and read as csv
budgetfile = "budget_data.csv"
pdbudgetfile = pd.read_csv(budgetfile)

#count total month
unique_months = len(pdbudgetfile["Date"].unique())
unique_months

#count total P&L
total = pdbudgetfile["Profit/Losses"].sum()
total

#average changes from the previous months
profit_loss_change = pdbudgetfile["Profit/Losses"]
change = profit_loss_change.diff()
average_change = round(float(change.mean()), 2)
average_change 

#idnetify most profitable month
profit_loss_max = pdbudgetfile["Profit/Losses"].max()
profit_loss_max_idx = pdbudgetfile["Profit/Losses"].idxmax()
profit_loss_max_month = pdbudgetfile.loc[profit_loss_max_idx, "Date"]

#idnetify least profitable month
profit_loss_min = pdbudgetfile["Profit/Losses"].min()
profit_loss_min_idx = pdbudgetfile["Profit/Losses"].idxmin()
profit_loss_min_month = pdbudgetfile.loc[profit_loss_min_idx, "Date"]

#summary
print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(unique_months))
print("Average  Change: $" + str(average_change))
print("Greatest Increase in Profits: " + profit_loss_max_month + ", $" + str(profit_loss_max))
print("Greatest Decrease in Profits: " + profit_loss_min_month + ", $" + str(profit_loss_min))

#output txt
outputfile = "budget_analysis.txt"
with open(outputfile, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("-----------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(unique_months))
    txt_file.write("\n")
    txt_file.write("Average  Change: $" + str(average_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + profit_loss_max_month + ", $" + str(profit_loss_max))
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + profit_loss_min_month + ", $" + str(profit_loss_min))