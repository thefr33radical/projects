use assignment_1;
select count(DISTINCT(techcrunch.company)) from techcrunch  ; 

/*
Problem 1. Normalization (5o pts).
This problem will use the file techcrunch.csv. This dataset consists of company funding records reported
by TechCrunch. Each row represents one funding event for a company.
1) (10 pts) What is a good choice for a primary key here? In contrast, give an example of an
attribute (or composite) that would not be a valid primary key.

index_id is the primay key as it can identify tuple uniquely.
(We can also consider index_id,company as PK)
Ex of invalid primary key
category would not be primary key as it consists of multiple values and cannot identify tuple uniquely.
numEmps cannot be primary key because it has null values.

pre requisites for primary key:
The value of primary key should be unique for each row of the table. 
The column(s) that makes the key cannot contain duplicate values.
The attribute(s) that is marked as primary key is not allowed to have null values.

Be careful. You can check that your proposal really satisfies the definition of a primary key
by sorting your data by the relevant column(s) in Excel.

2) (10 pts) For your choice of primary key, do the data satisfy 1NF? Why or why not?
index_id is the pimary key.
Yes the data is in 1 NF as all the values are atomic. 
For the data to be in 1 NF there should be no composite or multi valued data which is not present in the table.
Hence we conclude the data is in 1NF.

3) (10 pts) For your choice of primary key, do the data satisfy 2NF? Why or why not?
No the data violates 2nf.
There are repeated values for company, raised_currency, round etc and normalization is done to reduce redundancy at each form.
company -> city,state
company fund_date -> Raised_curency, Round

(Theory states that to violate 2nf the primary key must be composite as partial(to get partial dependency). However the PK is singular so I am uncertain??
so i felt index_id,company should be the primary key as this would be appropriate.so in this case

index_id company -> city,state
company -> city,state
so there exists partial dependency hence violates 2nf)

4) (10 pts) For your choice of primary key, do the data satisfy 3NF? Why or why not?
No the data does not satisfy 3nf.
because there exists transitive FD 
Examples :
index_id -> company
index_id -> fund_date 
company -> city,state
company fund_date -> Raised_curency, Round

*/