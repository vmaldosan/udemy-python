# Useful commands

- Show headers in query results:
```
>.headers on
```

- Backup database to a file:
```
>.backup <?db_to_backup (defaul "main")> <file>
```

- Restore database backup from a file:
```
>.restore <?db_to_backup (defaul "main")> <file>
```

- Show the CREATE statements:
```
>.schema <?table_name>
```

- Show CREATE and data as INSERTS:
```
>.dump <?table_name>
```

- Exit:
```
>.quit
```

# Differences with other common RDBMS

- Types of columns are only for reference, you can actually insert any type of data in any column.