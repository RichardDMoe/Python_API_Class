
import pandas as pd

def main():
    excel_file ='movies.xls'

    movies = pd.read_excel(excel_file)

    print (movies.head())

    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
    print(movies_sheet1.head())

# grab the next 2 sheets as well
    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
                   # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet2.head())

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
                                # DF has 5 rows and 24 columns (indexed by title)
    print(movies_sheet3.head())


    movies = pd.concat([movies_sheet1,movies_sheet2,movies_sheet3])

    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    print(sorted_by_gross.head(10))




if __name__ == "__main__":
   main()
