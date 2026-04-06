---
title: Deploy Schema and Run Queries
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Deploy Schema and Run Queries

In this section, you create database tables, load sample data, and execute analytical queries on PostgreSQL.

At the end of this section, your database is:

* Populated with transactional data
* Structured with relational tables
* Ready for analytical SQL queries
* Accessible using the application user

## Connect to the database

Connect to the PostgreSQL database as the superuser.

```console
sudo -u postgres psql -d appdb
```

## Create database tables

Create two tables to simulate a transactional application.

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    amount NUMERIC,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**These tables represent:**

- `customers`: user information
- `orders`: transactional records linked via foreign key

## Insert sample data

Populate the `customers` table.

```sql
INSERT INTO customers (name, email)
SELECT 'user_' || i, 'user_' || i || '@example.com'
FROM generate_series(1, 100000) AS i;
```

Populate the `orders` table.

```sql
INSERT INTO orders (customer_id, amount, status)
SELECT
    (floor(random() * 100000) + 1)::int,
    (random() * 1000),
    CASE WHEN random() > 0.5 THEN 'completed' ELSE 'pending' END
FROM generate_series(1, 500000) AS i;
```

**This generates:**

- 100,000 customers
- 500,000 orders

## Fix ownership (important)

Ensure the application user owns the tables to allow schema changes and indexing.

```sql
ALTER TABLE customers OWNER TO appuser;
ALTER TABLE orders OWNER TO appuser;
```

## Run analytical queries

The queries in this section are analytical (OLAP-style) queries running against the transactional (OLTP) dataset you just loaded. PostgreSQL handles both workload types, which makes it well suited to applications that need operational reporting without a separate data warehouse.

## Total revenue

```sql
SELECT SUM(amount) FROM orders WHERE status = 'completed';
```
**What this query does:**

- Filters only completed orders
- Calculates the total revenue generated

The output is similar to:

```output
             sum
-----------------------------
 125444891.15572856461471770
(1 row)
```

**What the output means:**

- Total revenue ≈ 125 million
- This represents the overall business earnings from completed transactions

## Top customers by spending

This query aggregates order totals per customer across the full orders table — a typical OLAP aggregation on OLTP data.

```sql
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
```

The output is similar to:

```output
 customer_id |    total_spent
-------------+--------------------
       45136 | 9402.1803173247709
       70670 |  9179.385512892869
       57604 | 8936.2102913510321
        3594 | 8885.8026615034014
       68349 |  8817.484402872083
       45974 | 8761.6822572100911
       20049 | 8739.8605561353213
       79794 |  8615.155198629147
       67514 |  8573.093324224081
       49210 |  8497.876121330483
(10 rows)
```

**The output means:**

- Shows the top 10 highest-paying customers
- Helps identify:
  - High-value users
  - VIP customers
  - Revenue concentration

## Customer order counts

This query joins customers and orders, counts how many orders each customer placed, and ranks them by activity. It's a multi-table analytical query — the join across two OLTP tables produces an OLAP-style activity report.

```sql
SELECT c.name, COUNT(o.id)
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.name
ORDER BY COUNT(o.id) DESC
LIMIT 10;
```

The output is similar to:

```output
    name    | count
------------+-------
 user_24831 |    17
 user_59573 |    16
 user_92684 |    16
 user_20049 |    16
 user_99775 |    16
 user_35090 |    16
 user_39820 |    16
 user_45879 |    15
 user_18306 |    15
 user_45974 |    15
(10 rows)
```

**The output means:**

- Shows most active customers
- Useful for:
  - Engagement analysis
  - Identifying frequent buyers

## Validate as application user

Exit the current session first.

```sql
\q
```

Connect using the application user.

```bash
psql -h localhost -U appuser -d appdb
```

When prompted for a password, enter `StrongPassword123`.

## What you've accomplished and what's next

You've successfully deployed a relational schema and executed analytical queries on PostgreSQL. Your setup includes:

- Transactional schema with foreign key relationships
- Large dataset for realistic workloads
- Analytical queries for insights
- Verified access using application credentials

Next, you'll benchmark PostgreSQL performance and optimize query execution using indexing and monitoring tools.
