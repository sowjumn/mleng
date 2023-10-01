Pandas provides a lot of useful data analysis tools 

### Working with Excel Files 

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

### Typecast to a numeric value
Sometimes pandas loads data as a different type as such we need to cast the DataFrame to a numeric value

`df['salary'] = pd.to_numeric(df['salary'], errors = 'coerce')

Coerce for errors means we catch and ignore any records

### String Replace and type cast
The columns need to be strings if we want to work with raw text in DataFrame.
Example Operations:
* Check If a word appears in column
* Replace specific text in a column

as such we need to cast the text to string at times

df["name"] = df["name"].astype(str)

To Replace text use `str.replace` method
df["name"] = df["name"].str.replace('$','')

### Deal with Missing values:

Many datasets have missing values and pandas has specific methods to deal with missing values

To Drop the rows with missing values use dropna()
`df.dropna(inplace = True)`

inplace means changes are made in DataFrame itself

To Fill in the missing values use fillna()
`df.fillna(0)` 

In this case all NaN elements will be replaced with 0s

### Join Excel Sheets
Pandas function to perform a join is .merge

`df = pd.merge(left = df,right = df_cities, how = 'inner', left_on = 'city_id', right_on = 'id')`

### Delete a column
`del df['id_x']`

### Slicing rows
`df[start_index:end_index_not_inclusive]`

