import pandas as pd
import csv

### reading the csv file
biz_df = pd.read_csv('C://Users/Melissa F/Desktop/MDS/Data Science MDS 564/Spend_Type-BlackFriday.csv')

print(biz_df)

### creating a variable called categoryCounter by looking at the columns contains numbers between 1 and 18
### to create a column titled category number (this is the number in the range) and then setting value to uninitialized
### creating a column titled category 1, category 2, etc and entering value uninitialized for each column and row
for categoryCounter in range(1,19):	
	biz_df["Category " + str(categoryCounter)]="UNINITIALIZED"

print(biz_df)
	
### for every row in the df and for the counter in the range, if these columns equal the counter (1-18), then enter Y or N 
### if there is counter of 1-18 in columns Product_category_1, etc, then replace uninitialized in new columns with Y or N
for index, row in biz_df.iterrows():
	print(index)
	for counter in range(1,19):	
		if row["Product_Category_1"]==counter or row["Product_Category_2"]==counter or row["Product_Category_3"]==counter:
			biz_df.at[index, "Category " + str(counter)] = "Y"
		else:
			biz_df.at[index, "Category " + str(counter)] = "N"
						
### write to csv file
biz_df.to_csv('C://Users/Melissa F/Desktop/MDS/Data Science MDS 564/FinalSpend_Type-BlackFriday.csv', sep=',')