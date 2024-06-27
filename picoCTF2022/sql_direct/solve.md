# picoCTF2022 SQL Direct Write Up

## Description

> Connect to this PostgreSQL server and find the flag!
> 
>`psql -h saturn.picoctf.net -p 57720 -U postgres pico` Password is `postgres`

## Solution

The challenge states that running the command will connect us to a PostgreSQL server. After running the command and entering the password, a prompt appears for interacting with the server. PostgreSQL commands are a form of SQL querying. Running the query:

```
select table_name from information_schema.tables;
```

Fetches all the table names in the database. It produces the following output:

```
              table_name
---------------------------------------
 flags
 pg_statistic
 pg_type
 pg_foreign_table
 pg_authid
 pg_shadow
 pg_roles
 pg_statistic_ext_data
-- snipped
```

Thus there is a table named `flags` in the database. We can fetch the contents of this table with the query:

```
select * from flags;
```

Which produces the following output:

```
 id | firstname | lastname  |                address
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
```

And thus the flag is:

```
 picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
```