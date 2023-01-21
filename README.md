# Climate Analysis App


## SQLAlchemy

SQLAlchemy in python has been used as an Object Relational Mapper (ORM) to reflect the sqlite database (local).
Using the same library, queries have been to make the relevant analysis giving the following results:

### Precipitation Analysis

![89f20d77-79c3-4bfc-8665-b3790dd63ee2](https://user-images.githubusercontent.com/85002751/213861861-427347d4-febb-435d-a14c-a6652564e871.png)

### Station Analysis

- There are 9 stations within the dataset
- The list of the most active stations in descending order
- Lowest, highest and average temperature of the most active station
- The diagram below displays the station with the highest number of temperature observations

![d2e89fa7-763c-4df7-97a9-71c9126897e1](https://user-images.githubusercontent.com/85002751/213861955-0f040518-b80a-477b-b307-1ed3add604df.png)

## Python Flask

A connection to the sqlite file is established in the application also using sqlalchemy.
Using Flask, a landing page is rendered to advise users on different static and dynamic routes to view the database.

<img width="947" alt="1" src="https://user-images.githubusercontent.com/85002751/213864479-9e32be7f-448b-4f5f-82e3-a59c1ac84aaa.png">
<img width="956" alt="2" src="https://user-images.githubusercontent.com/85002751/213864484-97f4634f-ab60-40cb-ab27-939fa36c6f64.png">
