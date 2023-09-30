Pandas provides a lot of useful data analysis tools 

Read and write excel files
xd = pd.ExcelFile('file_1.xlsx')
df = xd.parse('my_sheet')
type(df) #  DataFrame
len(df) #Count
shape(df) #Get the size of the dataframe (rows,cols) 

# Data Ops
Get a count of values in each column 

`df.count()`

Look at the column headers by accessing the columns attribute
`df.columns`

Type of data stored in each column by accessing the dtypes attribute
`df.dtypes`

Summary statistics of numerical values in DataFrame
`df.describe()`

Head method displays first 5 rows of data
`df.head()`

To get the first 50 rows of data
`df.head(50)`

Drop the duplicates from df
`df.drop_duplicates()`

Select specific columns of data
`df["name"]`

select the first 100 rows of certain columns
`attrs = ["name", "city_id", "state_id"]`
`df[attrs].head(100)`
