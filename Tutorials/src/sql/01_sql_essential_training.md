## +LinkedIn - SQL Essential Training

## [COURSE](https://www.linkedin.com/learning/sql-essential-training-20685933/the-data-driven-world-19067626?resume=false)

<details>
<summary>1. Introduction </summary>

# Introduction

[https://sqlitebrowser.org/](https://sqlitebrowser.org/)

<img width="1488" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/04b30ecf-8e3c-4b0d-a9c1-6fdcb72fd20d">

# #END

</details>

<details>
<summary>2. SQL Comments </summary>

# SQL Comments

```sql
-- THIS IS A COMMENT

/*
THIS IS A COMMENT
THIS IS ANOTHER COMMENT

*/
```

```sql

/*
CREATED BY: WALTER SHIELDS
CREATE DATE: MM/DD/YYYY
DESCRIPTION: THIS IS THE STRUCTURE OF A BASIC QUERY

*/
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/561914be-6140-4a48-8634-6e3d2b96d7a0">


# #END </details>

<details>
<summary>3. High-level questions for the composition of a Query </summary>

# High-level questions for the composition of a Query:

- What table within the database are we requesting data from?
- What fields within that table are we interested in?
- Do we want to exclude any data or filter or omit any range or time period?
- What does our query do?

# #END </details>

<details>
<summary>4. Select FirstName, LastName, and Email of all Customers in CUSTOMER Table </summary>

# Select FirstName, LastName, and Email of all Customers in CUSTOMER Table

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT
	FirstName,
	LastName,
	Email
FROM
	Customer
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/58385e2a-cff0-4210-915a-86a1c8b23381">


# #END </details>

<details>
<summary>5. Select FirstName, LastName, and Email of all Customers with Column Aliases </summary>

# Select FirstName, LastName, and Email of all Customers with Column Aliases

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT
	FirstName AS [Customer First Name],
	LastName AS "Customer Last Name",
	Email AS EMAIL
FROM
	Customer
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/0e186e27-b30e-44e5-adb8-6982fa5a45bf">


# #END </details>

<details>
<summary>6A. Sorting Query Results - Select Customers and Order BY Lastname Descending </summary>

# Sorting Query Results - Select Customers and Order BY Lastname Descending

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT
	FirstName AS [Customer First Name],
	LastName AS "Customer Last Name",
	Email AS EMAIL
FROM
	Customer
ORDER BY
	LastName
DESC
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d7067b8c-c9d0-4df0-b9ee-d96a276d9d3b">


# #END </details>

<details>
<summary>6B. Sorting Query Results - Select Customers and Order BY Lastname Ascending </summary>

# Sorting Query Results - Select Customers and Order BY Lastname Ascending

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT
	FirstName AS [Customer First Name],
	LastName AS "Customer Last Name",
	Email AS EMAIL
FROM
	Customer
ORDER BY
	LastName
ASC
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/568265ed-b759-4b0e-b90f-760554cc153b">

# #END </details>

<details>
<summary>6C. Sorting Query Results - Select Customers and Order BY Firstname Ascending, Lastname Descending </summary>

# Sorting Query Results - Select Customers and Order BY Firstname Ascending, Lastname Descending

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT
	FirstName AS [Customer First Name],
	LastName AS "Customer Last Name",
	Email AS EMAIL
FROM
	Customer
ORDER BY
	FirstName ASC,
	LastName DESC

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/30075a20-e537-499f-81d4-ba9b60922343">

# #END </details>

<details>
<summary>7A. Limiting Query Results - Select Customers and Order BY Firstname Ascending, Lastname Descending and show only first 5 records </summary>

# Limiting Query Results - Select Customers and Order BY Firstname Ascending, Lastname Descending and show only first 5 records

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT
	FirstName AS [Customer First Name],
	LastName AS "Customer Last Name",
	Email AS EMAIL
FROM
	Customer
ORDER BY
	FirstName ASC,
	LastName DESC
LIMIT
	5
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/2a300d05-c1ef-4c12-ad14-2649b1cce2ec">

# #END </details>

<details>
<summary>7B. Limiting Query Results - Code Challenge: Concise track pricing report </summary>

# Limiting Query Results - Code Challenge: Concise track pricing report

<img width="582" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/756f6d7e-fe1b-408b-a669-0a68cb83ff55">
<img width="668" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5a0309fa-93c7-48f2-985f-bb773ae7ca62">

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: Code Challenge
*/

SELECT
	t.Name AS "Track Name",
	t.UnitPrice AS Price
FROM
	Track AS t
ORDER BY
	t.Name ASC
LIMIT
	20;

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5af84f1d-fc70-4a2e-aea9-11748d5f9236">


# #END </details>

<details>
<summary>8. Filter Data - How many customers purchased two songs at 99 cents each?  </summary>

# Filter Data - How many customers purchased two songs at 99 cents each?

- there are tracks at 99 cents each, which is part of our question.
- two songs purchased at 99 cents each will total to $1.98.
- So let's take a look at our invoice table and if we scroll over to the total, we do see that there are invoices totaling $1.98.

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: This query displays all customers first names, last names and email addresses
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	Total = 1.98
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/51763537-ad58-428b-8ec0-ceb448ed5536">

# #END </details>

<details>
<summary>9. Filter Data - How many invoices exist between $1.98 and $5?  </summary>

# Filter Data - How many invoices exist between $1.98 and $5?

- We would simply have to make an alteration to our WHERE clause.
- We're simply going to include the logical operator between $1.98 and $5.

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices exist between $1.98 and $5?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	Total BETWEEN 1.98 AND 5.00
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/24be3aa0-98a3-4a83-b3e0-69aeaa91bd41">

# #END </details>

<details>
<summary>10. Filter Data - How many invoices do we have that are exactly $1.98 or $3.96?  </summary>

# Filter Data - How many invoices do we have that are exactly $1.98 or $3.96?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices do we have that are exactly $1.98 or $3.96?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	Total IN (1.98, 3.96)
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b6d75b05-82d6-4872-bf12-532ee7fcfa4f">

# #END </details>

<details>
<summary>11. Filter Data - How many invoices were billed to the city of Brussels?  </summary>

# Filter Data - How many invoices were billed to the city of Brussels?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices were billed to the city of Brussels?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	BillingCity = 'Brussels'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/da917cfd-3cfc-40ef-ae5a-ad69c2b2c9db">

# #END </details>

<details>
<summary>12. Filter Data - How many invoices were billed to Brussels, Orlando, or Paris?  </summary>

# Filter Data - How many invoices were billed to Brussels, Orlando, or Paris?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices were billed to Brussels, Orlando, or Paris?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	BillingCity IN ('Brussels', 'Orlando', 'Paris')
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/264cba36-ebf0-42cb-960b-04cacce39356">

# #END </details>

<details>
<summary>13. Filter Data - How many invoices were billed in the cities that start with B?  </summary>

# Filter Data - How many invoices were billed in the cities that start with B?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices were billed in the cities that start with B?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	BillingCity LIKE 'B%'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/04a5b037-37a9-4e78-b5bd-54b745369319">


# #END </details>

<details>
<summary>14. Filter Data - How many invoices were billed in cities that have a B anywhere in its name?  </summary>

# Filter Data - How many invoices were billed in cities that have a B anywhere in its name?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices were billed in cities that have a B anywhere in its name?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	BillingCity LIKE '%B%'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/5e6ec078-4473-4337-a9a1-f59689c912ea">

# #END </details>

<details>
<summary>15. Filter Data - How many invoices were billed on May 22, 2010 (2010-05-22 00:00:00)?  </summary>

# Filter Data - How many invoices were billed on May 22, 2010 (2010-05-22 00:00:00)?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices were billed on May 22, 2010 (2010-05-22 00:00:00)?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	Date(InvoiceDate) =  '2010-05-22'
	-- DateTime(InvoiceDate) =  '2010-05-22 00:00:00'
	-- InvoiceDate = '2010-05-22 00:00:00'
ORDER BY
	CustomerId ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/21378947-0d3e-4ea7-a32c-12b7aa267fb1">

# #END </details>

<details>
<summary>16. Filter Data - How many invoices were billed after 2010-05-22 and have a total of less than $3?  </summary>

# Filter Data - How many invoices were billed after 2010-05-22 and have a total of less than $3?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices were billed after 2010-05-22 and have a total of less than $3?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	Date(InvoiceDate) >  '2010-05-22' AND Total < 3.00
ORDER BY
	InvoiceDate ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/305a9eba-f2a0-452e-ba10-9aeade0d11d7">

# #END </details>

<details>
<summary>17. Filter Data - How many invoices whose billing city starts with P or the billing city starts with D?  </summary>

# Filter Data - How many invoices whose billing city starts with P or the billing city starts with D?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices whose billing city starts with P or the billing city starts with D?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	BillingCity LIKE  'P%'  OR BillingCity LIKE 'D%'
ORDER BY
	InvoiceDate ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/4b385d0e-c637-4df5-9ca4-a65fb0506fda">

# #END </details>

<details>
<summary>18. Filter Data - How many invoices are greater than $1.98 from any cities whose names start with P or D?  </summary>

# Filter Data - How many invoices are greater than $1.98 from any cities whose names start with P or D?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: How many invoices are greater than $1.98 from any cities whose names start with P or D?
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total
FROM
	Invoice
WHERE
	Total > 1.98 AND (BillingCity LIKE 'P%' OR BillingCity LIKE 'D%')
ORDER BY
	InvoiceDate ASC
LIMIT
	500

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/164fd339-1709-49cf-93ff-43c13724cff1">

# #END </details>

<details>
<summary>19A. Filter Data - Adding Customised Columns using IF THEN Logic with CASE  </summary>

# Filter Data - Adding Customised Columns using IF THEN Logic with CASE

## Sales Categories:

- They want as many customers as possible to spend between $7.00 and $15.00.
- Baseline Purchase - Between $0.99 and $1.99
- Low Purchase- Between $2.00 and $6.99
- Target Purchase Between $7.00 and $15.00
- Top Performer- Above $15.00

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/21/2024
DESCRIPTION: Adding Customised Columns using IF THEN Logic with CASE
*/

SELECT
	CustomerId,
	InvoiceDate,
	BillingAddress,
	BillingCity,
	Total,
	CASE
		WHEN Total < 2.00 THEN 'Baseline Purchase'
		WHEN Total BETWEEN 2.00 AND 6.99 THEN 'Low Purchase'
		WHEN Total BETWEEN 7.00 AND 15.00 THEN 'Target Purchase'
		ELSE 'Top Performance'
		END AS PurchaseType,
	CASE
		WHEN Total < 7.00 THEN 'Low'
		WHEN Total > 6.99 THEN 'High'
		END AS Potential
FROM
	Invoice
WHERE
	Total > 1.98 AND (BillingCity LIKE 'P%' OR BillingCity LIKE 'D%')
ORDER BY
	InvoiceDate ASC
LIMIT
	500
	
```

<img width="1414" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/0fe3fe64-1e0d-42b0-9b0f-0d38063f99f9">

# #END </details>

<details>
<summary>19B. Filter Data - Code Challenge: Categorize tracks by price  </summary>

# Filter Data - Code Challenge: Categorize tracks by price

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b266d087-55c3-41d4-b500-314e7a7ed68c)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/4c5bbb82-ad47-4875-ab42-24422c288e46)

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: This query selects track names, composers,
unit prices, and categorizes each track based on its price.
*/

SELECT 
    Name AS "Track Name",
    Composer,
    UnitPrice AS Price,
    CASE
        WHEN UnitPrice < 1.00 THEN 'Budget' 
        WHEN UnitPrice BETWEEN 1.00 AND 1.49 THEN 'Regular'
        WHEN UnitPrice BETWEEN 1.50 AND 1.99 THEN 'Premium'
        ELSE 'Exclusive'
		/*
		WHEN UnitPrice < 0.99 THEN "Budget'
		WHEN UnitPrice > 0.99 AND UnitPrice < 1.49 THEN 'Regular'
		WHEN UnitPrice > 1.49 AND UnitPrice < 1.99 THEN "Premium"
		ELSE 'Exclusive'
		*/
    END AS PriceCategory
FROM 
    Track
ORDER BY
    UnitPrice ASC;

```

<img width="1414" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/78921320-c04d-441f-a390-1838ef7c9c59">

# #END </details>

<details>
<summary>20. Accessing Data from multiple Tables - BASIC JOINS </summary>

# Accessing Data from multiple Tables - BASIC JOINS

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: JOINS
*/

SELECT 
    *
FROM 
    Invoice
INNER JOIN
	Customer
ON
	Invoice.CustomerId = Customer.CustomerId
ORDER BY
	Customer.CustomerId
	
```

<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/8ace37e0-f4ac-49ba-b90a-d4c889be1ce8">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/dfb1d7ea-6b63-4749-a301-978feccb33a9)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/e38dd40a-9a39-4aa6-a7ef-a25dc77eba03)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/f1c33eeb-b386-455b-b87c-38c43469519f)

<img width="1456" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/0cb7036c-92fa-40fb-990e-f2f07acf8cb2">
<img width="1500" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/439e855f-d094-4e2a-8004-a07e527e822f">
<img width="1500" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/4e3b795c-43eb-4a7c-8302-40cc445c1697">

# #END </details>

<details>
<summary>21. Accessing Data from multiple Tables - SIMPLIFYING JOINS WITH ALIAS </summary>

# Accessing Data from multiple Tables - SIMPLIFYING JOINS WITH ALIAS

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: JOINS
*/

SELECT 
    c.LastName,
	c.FirstName,
	i.InvoiceId,
	i.CustomerId,
	i.InvoiceDate,
	i.Total
FROM 
    Invoice AS i
INNER JOIN
	Customer AS c
ON
	i.CustomerId = c.CustomerId
ORDER BY
	c.CustomerId
	
```

<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/7f6aee53-4a1a-4bae-be0e-797234c87a3c">

# #END </details>

<details>
<summary>22. Accessing Data from multiple Tables - USING INNER JOINS </summary>

# Accessing Data from multiple Tables - USING INNER JOINS

- An inner join only returns matching records.
- Any unmatched data from either table is ignored.
- Joins are often described with the use of Venn diagrams.
- As our Venn diagram shows, an inner join represents only the overlapping section of the Venn diagram.
-  The inner join is the most common type of join that's used.
-  The main use of the inner join is to bring corresponding data together from different tables in a relational database.

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/15fa681e-ed29-405c-b535-926235c0cddc)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/300fb60b-9f89-4abb-a626-6843536cb273)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/2f9c8ab3-7d1c-4877-8204-8abb96b51a24)

# #END </details>

<details>
<summary>23. Accessing Data from multiple Tables - USING LEFT OUTER JOINS </summary>

# Accessing Data from multiple Tables - USING LEFT OUTER JOINS

- A left outer join combines all the records from the left table with any matching records from the right table.
- As shown in our Venn diagram, the concept of left table and right table depends entirely on the order these tables are listed in the join statement.
- So for example, our SQL statement here has listed invoices first. Then after the left outer join, it lists the customer table.
- Our invoice table is the left table and our customer table is the right table.
- With this type of join, everything in our invoice table will be displayed.
- Since customer 1 did not order any songs, that particular record is omitted.
- We are combining all 5 records from the invoice table with only 3 records from the customer table.
- Left joins are useful because they allow us to see discrepancies in our data.
- We can produce lists of customers that have not generated invoices or search for data that has been removed in the right table but still exist in the left.

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/b07245c9-8aa0-42b7-9d4c-8c1b6c4d4bde)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/d264d103-e099-48ad-9fc8-26d34e619a4b)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/133ba54d-1dba-4cbe-a013-68da4dd401cb)

# #END </details>

<details>
<summary>24. Accessing Data from multiple Tables - USING RIGHT OUTER JOINS </summary>

# Accessing Data from multiple Tables - USING RIGHT OUTER JOINS

- The right outer joins are not supported in SQLITE.
- However, right joins are still very popular in other relational database management systems.
- The right outer join returns the entire right table as well as matching information from the left table.
- The right join is a mirror image of the left join, and functions in a very similar way.
- The right join takes all fields from the right table, in this case the customer's table, and matches that data with any corresponding data from the invoice table or the left table. 

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/dc5f4981-82f8-4a4d-9073-813f06fb919c)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/803ec5c9-1305-48cd-ac89-191485958490)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/6c037f79-4d4e-474a-8a7e-1bb8190044b1)

 # #END </details>

<details>
<summary>25. Accessing Data from multiple Tables - Entity Relationship Diagrams </summary>

# Accessing Data from multiple Tables - Entity Relationship Diagrams

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/33f30a8d-0f36-4805-8ab0-ce603d313787)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/845d3b76-8ded-4391-a7cc-4a7c0e8351ff)

 # #END </details>

<details>
<summary>26A. Accessing Data from multiple Tables - JOIN TABLES - What employees are responsible for the 10 highest individual sales? </summary>

# Accessing Data from multiple Tables - JOIN TABLES - What employees are responsible for the 10 highest individual sales?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: JOINS
*/

SELECT 
    e.FirstName, 
	e.LastName, 
	e.EmployeeId, 
	c.FirstName, 
	c.LastName, 
	c.SupportRepId, 
	i.CustomerId, 
	i.Total
FROM 
    Invoice AS i
INNER JOIN
	Customer AS c
ON
	i.CustomerId = c.CustomerId
INNER JOIN
	Employee AS e	
ON
	c.SupportRepId = e.EmployeeId
ORDER BY
	i.Total DESC
LIMIT
	10	
	
```

<img width="1533" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/d28dd8b3-097e-4487-a41f-66f4b8d839e0">

# #END </details>

<details>
<summary>26B. Accessing Data from multiple Tables - Code Challenge: Analyzing customer support interactions </summary>

# Accessing Data from multiple Tables - Code Challenge: Analyzing customer support interactions

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/dc8b458b-ca0f-4a5e-a589-a40050c4880e)
![image](https://github.com/omeatai/src-AI-Software/assets/32337103/37a1e552-ef87-4a61-877f-686dd27ca179)

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: JOINS
*/

SELECT 
    c.FirstName AS CustomerFirstName, 
	c.LastName AS CustomerLastName, 
	e.FirstName AS SupportRepFirstName, 
	e.LastName AS SupportRepLastName
FROM 
	Customer AS c
JOIN
	Employee AS e	
ON
	c.SupportRepId = e.EmployeeId
ORDER BY
	e.LastName ASC, c.LastName ASC
	
```

<img width="1429" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/0ae3047e-3577-4b46-87d5-bc38f9d4fee8">

# #END </details>

<details>
<summary>27. SQL Functions - Connecting Strings </summary>

# SQL Functions - Connecting Strings

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: FUNCTIONS
*/

SELECT 
    FirstName,
	LastName,
	Address,
	FirstName || " " || LastName || ", " || Address || ", " || City || ", " || State || ", " || PostalCode AS "Mailing Address"
FROM 
	Customer
WHERE
	Country = 'USA'
	
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/c1d1847e-ed57-4556-90b2-d003bf20dab7">

# #END </details>

<details>
<summary>28. SQL Functions - Separating Strings </summary>

# SQL Functions - Separating Strings

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: FUNCTIONS
*/

SELECT 
    FirstName,
	LastName,
	Address,
	FirstName || " " || LastName || ", " || Address || ", " || City || ", " || State || ", " || PostalCode AS "Mailing Address",
	LENGTH(PostalCode),
	SUBSTR(PostalCode, 1, 5) AS [5 Digit Postal Code]
FROM 
	Customer
WHERE
	Country = 'USA'
	
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/a2d14f40-df48-4da1-bfa8-6af5c2208e63">

# #END </details>

<details>
<summary>29. SQL Functions - UPPER and LOWER Strings </summary>

# SQL Functions - UPPER and LOWER Strings

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/25/2024
Description: FUNCTIONS
*/

SELECT 
    FirstName,
	LastName,
	Address,
	FirstName || " " || LastName || ", " || Address || ", " || City || ", " || State || ", " || PostalCode AS "Mailing Address",
	LENGTH(PostalCode),
	SUBSTR(PostalCode, 1, 5) AS [5 Digit Postal Code],
	UPPER(FirstName) AS [FirstName all Caps],
	LOWER(LastName) AS [LastName all Lower]
FROM 
	Customer
WHERE
	Country = 'USA'
	
```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/acae8b82-5026-4fb2-82d2-ebaacc40f5ec">


# #END </details>

<details>
<summary>30. SQL Functions - DATE Functions - Calculate the ages of all employees </summary>

# SQL Functions -  DATE Functions - Calculate the ages of all employees

- We need to leverage the birth date field to calculate each employee's age. 
- We need to find out the difference between the current date and the employee's birthdate.
- We can employ a new date function which is called the strftime.
- The strftime function converts date and time strings into another format.

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Calculate the ages of all employees
*/

SELECT
	FirstName,
	LastName,
	BirthDate,
	strftime('%Y-%m-%d', BirthDate) AS [BirthDate with-no-Timecode],
	strftime('%Y-%m-%d', 'now') - strftime('%Y-%m-%d', BirthDate) AS Age
FROM
	Employee

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/b2fd841c-ed79-474c-b2dc-6fccbf537028">

# #END </details>

<details>
<summary>31. SQL Functions - AGGREGATE Functions - Calculate the total global sales of all time </summary>

# SQL Functions - AGGREGATE Functions - Calculate the total global sales of all time

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Calculate the total global sales of all time
*/

SELECT
	SUM(Total) AS [Total Sales],
	AVG(Total) AS [Average Sales],
	MAX(Total) AS [Maximum Sale],
	MIN(Total) AS [Minimum Sale],
	COUNT(*) AS [Sales Count]
FROM
	Invoice

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/96420f20-9c9a-4019-901e-0372a46bbd0e">

![image](https://github.com/omeatai/src-AI-Software/assets/32337103/bace6257-486d-4988-b736-72d65e59081e)

# #END </details>

<details>
<summary>32. SQL Functions - NESTING Functions - Rounding decimals </summary>

# SQL Functions - NESTING Functions - Rounding decimals 

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Rounding decimals 
*/

SELECT
	SUM(Total) AS [Total Sales],
	round(AVG(Total), 3) AS [Average Sales],
	MAX(Total) AS [Maximum Sale],
	MIN(Total) AS [Minimum Sale],
	COUNT(*) AS [Sales Count]
FROM
	Invoice

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/6366d0f7-5138-4c57-ac1b-b207dccd5990">

# #END </details>

<details>
<summary>33. Code Challenge: Customer postal code transformation </summary>

# Code Challenge: Customer postal code transformation

<img width="725" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/88e816e5-f50f-44aa-8597-d28faf5af9f6">
<img width="674" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/78e7757a-cc2b-4736-ae25-3beab698722f">

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Code Challenge: Customer postal code transformation
*/

SELECT
	c.FirstName || " " || c.LastName AS CustomerFullName,
	substr(c.PostalCode, 1, 5) AS StandardizedPostalCode
FROM
	Customer AS c
WHERE
	c.Country = "USA"
ORDER BY
	CustomerFullName;	

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/4a559dc1-54e5-4308-9e4d-0fcbd709c4e6">

# #END </details>

<details>
<summary>34. Grouping - What are the average invoice totals by City? </summary>

# Grouping - What are the average invoice totals by City?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Grouping - What are the average invoice totals by City?
*/

SELECT
	BillingCity,
	avg(Total) AS [Average Per City],
	round(avg(Total),2) AS [Rounded Average Per City]
FROM
	Invoice
GROUP BY
	BillingCity
ORDER BY
	BillingCity;	

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/2f54e5a1-3c79-4339-88cc-0bd6e408244e">

# #END </details>

<details>
<summary>35. Grouping - What are the average invoice totals by City for only Cities that start with L? </summary>

# Grouping - What are the average invoice totals by City for only Cities that start with L?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Grouping - What are the average invoice totals by City for only Cities that start with L?
*/

SELECT
	BillingCity,
	avg(Total) AS [Average Per City],
	round(avg(Total),2) AS [Rounded Average Per City]
FROM
	Invoice
WHERE
	BillingCity LIKE "L%"
GROUP BY
	BillingCity
ORDER BY
	BillingCity;	

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/faafd22e-a408-4e51-bfab-a6a707ec326c">

# #END </details>

<details>
<summary>36. Grouping - What are the average invoice totals greater than $5.00? </summary>

# Grouping - What are the average invoice totals greater than $5.00?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Grouping - What are the average invoice totals greater than $5.00?
*/

SELECT
	BillingCity,
	avg(Total) AS [Average Per City],
	round(avg(Total),2) AS [Rounded Average Per City]
FROM
	Invoice
GROUP BY
	BillingCity
HAVING	
	avg(Total) > 5	
ORDER BY
	round(avg(Total),2) DESC;	

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/1289a5ec-24c8-4975-8ac6-2ddfcf7317fe">

# #END </details>

<details>
<summary>37. Grouping - What are the average invoice totals greater than $5.00 for cities starting with B? </summary>

# Grouping - What are the average invoice totals greater than $5.00 for cities starting with B?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Grouping - What are the average invoice totals greater than $5.00 for cities starting with B?
*/

SELECT
	BillingCity,
	avg(Total) AS [Average Per City],
	round(avg(Total),2) AS [Rounded Average Per City]
FROM
	Invoice
WHERE
	BillingCity LIKE "B%"	
GROUP BY
	BillingCity
HAVING	
	avg(Total) > 5	
ORDER BY
	round(avg(Total),2) DESC;	

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/ef49d7f8-14cf-4f5e-8348-0507119a3b9a">

# #END </details>

<details>
<summary>38. Grouping by many Fields - What are the average invoice totals by billing Country and City? </summary>

# Grouping by many Fields - What are the average invoice totals by billing Country and City?

```sql
/*
CREATED BY: IFEANYI OMEATA
CREATE DATE: 05/28/2024
DESCRIPTION: Grouping by many Fields - What are the average invoice totals by billing Country and City?
*/

SELECT
	BillingCountry,
	BillingCity,
	avg(Total) AS [Average Per City],
	round(avg(Total),2) AS [Rounded Average Per City]
FROM
	Invoice
GROUP BY
	BillingCountry,
	BillingCity
ORDER BY
	BillingCountry ASC;	

```

<img width="1473" alt="image" src="https://github.com/omeatai/src-AI-Software/assets/32337103/15851e82-7879-4a1f-8c0b-2bc1bf7e5cec">

# #END </details>

<details>
<summary>39. Code Challenge: Calculate average spend per city </summary>

# Code Challenge: Calculate average spend per city

```sql

```

# #END </details>

