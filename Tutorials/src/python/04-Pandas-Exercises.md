## +LinkedIn - Pandas Exercises

## [COURSE](https://www.linkedin.com/learning/coding-exercises-pandas/stretch-and-test-your-knowledge-with-pandas-code-challenges?resume=false)

<details>
<summary>1. Install Jupyter Notebook </summary>

# Check Python version 

```x
python3 --version
```

# Install Pip

```x
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

# Install Virtual Environment

```x
python3 -m venv venv
source venv/bin/activate
```

# Install Jupyter Notebook

```x
pip install notebook
```

# Run Jupyter Notebook

```x
jupyter notebook
```

# Check Installed Packages

```x
pip freeze
```

# Install Pandas and matplotlib

```x
pip install pandas
pip install matplotlib
```

# Uninstall all currently installed packages

```x
pip freeze > installed_packages.txt
pip uninstall -r installed_packages.txt -y
```

# Install packages from requirements.txt:

```x
pip install -r requirements.txt
```

# #END</details>

<details>
<summary>2. Task: Read Data from CSV and Excel files </summary>

# Task: Read Data from CSV and Excel files

![image](https://github.com/user-attachments/assets/48cb9650-aba3-40a4-a3d5-d2526d4fad80)
![image](https://github.com/user-attachments/assets/66625d86-9e7e-4f9b-b07a-885c4111d78e)

```py
import pandas as pd
```

![image](https://github.com/user-attachments/assets/97501b97-c4c4-44a3-8ff8-73856549d66a)
![image](https://github.com/user-attachments/assets/94769fbb-b27c-4bc2-89e6-f20c65d86b63)



# #END</details>

<details>
<summary>Solution for 2 </summary>

# Solution for 2

## Solution 1: Using Python

```py
with open("data/auto_mpg.csv", "r") as f:
    lines = f.readlines()
    print('MPG | Cylinders | Displacement | HorsePower | Weight | Acceleration | Model Year | Origin')
    for line in lines[1:11]:
        # line = line.strip().replace(',',' | ')
        line = line.strip().split(",")
        line = " | ".join(line)
        print(line)
```

```x
MPG | Cylinders | Displacement | HorsePower | Weight | Acceleration | Model Year | Origin
18.0 | 8 | 307.0 | 130.0 | 3504.0 | 12.0 | 70 | India
15.0 | 8 | 350.0 | 165.0 | 3693.0 | 11.5 | 70 | India
18.0 | 8 | 318.0 | 150.0 | 3436.0 | 11.0 | 70 | India
16.0 | 8 | 304.0 | 150.0 | 3433.0 | 12.0 | 70 | India
17.0 | 8 | 302.0 | 140.0 | 3449.0 | 10.5 | 70 | India
15.0 | 8 | 429.0 | 198.0 | 4341.0 | 10.0 | 70 | India
14.0 | 8 | 454.0 | 220.0 | 4354.0 | 9.0 | 70 | India
14.0 | 8 | 440.0 | 215.0 | 4312.0 | 8.5 | 70 | India
14.0 | 8 | 455.0 | 225.0 | 4425.0 | 10.0 | 70 | India
15.0 | 8 | 390.0 | 190.0 | 3850.0 | 8.5 | 70 | India
```

![image](https://github.com/user-attachments/assets/4b7671e3-6758-44c3-a8d1-9e779b2dcda0)

## Solution 2: Using Pandas Basic

```py
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("data/auto_mpg.csv")
df.columns = ['MPG','Cylinders','Displacement','HorsePower','Weight','Acceleration','Model Year','Origin']
df.head(10)

# print(pd.options.display.max_rows)
# To Print the first 10 rows (excluding the header row)
# print(df.head(10).to_string(header=False, index=False))
```

![image](https://github.com/user-attachments/assets/1447e823-26c9-4b0b-96a3-6ca741b82f9f)


## Solution 3: Using Pandas Advanced

```py
import pandas as pd

df = pd.read_csv("./data/auto_mpg.csv", header=0, names=['MPG','Cylinders','Displacement','HorsePower','Weight','Acceleration','Model Year','Origin'])
df.head(10)
```

![image](https://github.com/user-attachments/assets/3ea83ea8-67df-4ade-b526-da8d92acae2c)

# #END</details>

<details>
<summary>3. Task: Check DataFrame information and identify types of columns </summary>

# Task: Check DataFrame information and identify types of columns

![image](https://github.com/user-attachments/assets/1d58c264-5970-4245-90a1-94f0e3d2d637)

```py
import pandas as pd

df = pd.read_csv("./data/auto_mpg.csv",
                 header=0,
                 names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower','Weight',\
                          'Acceleration', 'Model Year', 'Origin'])

df.head(10)
```

![image](https://github.com/user-attachments/assets/7a896604-7e49-4cbb-8f1d-bdb3fed5d2d5)

# #END</details>

<details>
<summary>Solution for 3 </summary>

# Solution for 3

## Get only the number of Rows and Columns

```py
df.shape
```

```x
(398, 8)
```

![image](https://github.com/user-attachments/assets/fb66a183-d831-4dc0-9341-6ab8af24d9dd)

# Get only the columns

```py
df.columns
```

```x
Index(['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
       'Acceleration', 'Model Year', 'Origin'],
      dtype='object')
```

```py
list(df.columns)
```

```x
['MPG',
 'Cylinders',
 'Displacement',
 'Horsepower',
 'Weight',
 'Acceleration',
 'Model Year',
 'Origin']
```

```py
len(list(df.columns))
```

```x
8
```

![image](https://github.com/user-attachments/assets/7c9807c5-0b2e-40b1-9cf2-00feda042dbd)

# Get only the Index of the Rows

```py
df.index
```

```x
RangeIndex(start=0, stop=398, step=1)
```

![image](https://github.com/user-attachments/assets/cc58b15b-be5a-4f4d-a31b-5ac48ced326b)

# Get all Info: the number of Rows and Columns, with Index, Names and DataType of Columns

```py
df.info()
```

```x
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 8 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   MPG           398 non-null    float64
 1   Cylinders     398 non-null    int64  
 2   Displacement  398 non-null    float64
 3   Horsepower    392 non-null    float64
 4   Weight        398 non-null    float64
 5   Acceleration  398 non-null    float64
 6   Model Year    398 non-null    int64  
 7   Origin        398 non-null    object 
dtypes: float64(5), int64(2), object(1)
memory usage: 25.0+ KB
```

![image](https://github.com/user-attachments/assets/263627ef-8493-4747-a602-e437c3a783d2)

# #END</details>

<details>
<summary>4. Task: The summary statistics of numerical and categorical features </summary>

# Task: The summary statistics of numerical and categorical features

![image](https://github.com/user-attachments/assets/71632380-b090-4218-9f75-d989d6e6dc08)

```py
import pandas as pd

df = pd.read_csv("./data/auto_mpg.csv",
                 header=0,
                 names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower','Weight',\
                          'Acceleration', 'Model Year', 'Origin'])

df.head(10)
```

![image](https://github.com/user-attachments/assets/71f00dd8-1a88-4d72-bc5c-171eed386c61)

# #END</details>

<details>
<summary>Solution for 4 </summary>

# Solution for 4

## Display the Summary Statistics for Non Class variables

```py
df.describe()
```

![image](https://github.com/user-attachments/assets/81b6bf6a-b6d9-4160-a9ce-9b82a7f3a5d7)

## Display the Summary Statistics for Class Variables

```py
df.describe(include='object')
```

![image](https://github.com/user-attachments/assets/e9de6e07-e5c5-4f0a-a4cb-b7b8facb5517)

## Display the Frequencies for Class Variables

```py
df['Origin'].value_counts()
```

![image](https://github.com/user-attachments/assets/3dadc060-0178-4004-80ff-57d9559df6f8)

# Visualize distribution of frequencies for Class Variables

```py
import matplotlib

df['Origin'].value_counts().plot(kind="bar")
df['Origin'].value_counts().plot(kind="pie")
df['Origin'].value_counts().plot(kind="line")
df['Origin'].value_counts().plot(kind="area")
```

![image](https://github.com/user-attachments/assets/b8e29d1d-15a9-4125-bb3f-ff08840d571b)
![image](https://github.com/user-attachments/assets/27ea5313-1a7d-4228-99c8-59790f85ab53)
![image](https://github.com/user-attachments/assets/9e4d8b4b-d8d7-419d-9301-7804013c5efd)
![image](https://github.com/user-attachments/assets/7777db7c-82c8-4aa9-aae2-7f4b58b9c46f)

# #END</details>

<details>
<summary>5. Task: Add new columns to a DataFrame </summary>

# Task: Add new columns to a DataFrame

![image](https://github.com/user-attachments/assets/2580716c-66f7-41f8-9438-396d2ded3dbd)
![image](https://github.com/user-attachments/assets/7c9f3192-e3b0-4e84-8aed-6c60a55343ac)
![image](https://github.com/user-attachments/assets/da67c905-ec06-4d81-8a2c-8a42a85438ab)

# #END</details>

<details>
<summary>Solution for 5 </summary>

# Solution for 5

## Solution 1:

```py
df['Displacement-Power Ratio'] = None
# num_rows = df.index.stop
num_rows = df.shape[0]

for i in range(num_rows):
    displacement_value = df.loc[i,'Displacement']
    power_value = df.loc[i,'Horsepower']
    df.loc[i,'Displacement-Power Ratio'] = "{:.2f}".format(round(displacement_value/power_value, 2))
```

![image](https://github.com/user-attachments/assets/9f9b9059-4ad0-4d74-b66c-1685a777ae4d)

## Solution 2:

```py
df['Dis_Power_Ratio'] = round(df['Displacement']/df['Horsepower'], 2)
df['Weight_Per_Cylinder'] = round(df['Weight']/df['Cylinders'], 2)
df['Acc_Per_UnitPower'] = round(df['Acceleration']/df['Horsepower'], 2)
df.head(10)
```

![image](https://github.com/user-attachments/assets/1f2acfc6-49ec-4c2f-a095-3358e3cc7934)

# #END</details>

<details>
<summary>6. Task: Select specific columns in a DataFrame </summary>

# Task: Select specific columns in a DataFrame

![image](https://github.com/user-attachments/assets/086f0848-98c2-43c8-81f8-605e09416b23)
![image](https://github.com/user-attachments/assets/0ed87996-efb4-4555-b4b9-6cb387c8c7a6)
![image](https://github.com/user-attachments/assets/919b0173-b297-4f27-adaf-e70c7a02811d)
![image](https://github.com/user-attachments/assets/e292b527-82cb-4fc1-b4f1-c0433e2bd060)

```py
import pandas as pd
import numpy as np

camp_df = pd.read_csv("./data/marketing_campaign.csv", sep='\t')
camp_df.head(10)

camp_df.info()
```

![image](https://github.com/user-attachments/assets/88024c10-d33f-401e-b383-fa30582741ec)
![image](https://github.com/user-attachments/assets/baa972bc-a11b-4009-9aa6-692651b1f118)

# #END</details>

<details>
<summary>Solution for 6 </summary>

# Solution for 6

## Solution 1:

```py
mnt_purchases = pd.DataFrame({
    'MntWines': camp_df['MntWines'],
    'MntFruits': camp_df['MntFruits'],
    'MntMeatProducts': camp_df['MntMeatProducts'],
    'MntFishProducts': camp_df['MntFishProducts'],
    'MntSweetProducts': camp_df['MntSweetProducts'],
    'MntGoldProds': camp_df['MntGoldProds'],
})

mnt_purchases
```

## Solution 2:

```py
mnt_purchases2 = camp_df[['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']]

mnt_purchases2
```

![image](https://github.com/user-attachments/assets/8eea03db-9472-4949-b581-e36f654847aa)

## Solution 3:

```py
mnt_purchases3 = camp_df.loc[:,['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']]

mnt_purchases3
```

## Solution 4:

```py
mnt_purchases4 = camp_df.filter(['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds'])

mnt_purchases4
```

# #END</details>

<details>
<summary>7. Task: Subset the data from labels using .loc[] method </summary>

# Task: Subset the data from labels using .loc[] method

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

# #END</details>


