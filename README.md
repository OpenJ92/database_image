# __dbm__
## Version 2.0 under construction

This package seeks to construct Tree x Graph structure from queries to information_schema objects in a variable Database implementation. With such a structure, one can materialize queries to the imaged database through graph traversals and populate templated files of any kind that depend on the database structure. An example of the latter might be dbt or looker configuration files. Additionally, I look to serialize and store these structures so that one can explore a history of a given database and alert the user of changes and carry out templating actions.  

[dbm.1](https://github.com/OpenJ92/dbm)

## Database : [src/database](https://github.com/OpenJ92/__dbm__/tree/master/src/database)
Implementation specific configuration for proper execution of __dbm__. To contribute an implementation, navigate to the above link.

## Context : [src/context](https://github.com/OpenJ92/__dbm__/tree/master/src)
Object containing Connection, and executing Database Image. Actions act on a context.

## Connect : [src/connect](https://github.com/OpenJ92/__dbm__/tree/master/src/connect)
Connection to provided database implementation.

## Structures : [src/struct](https://github.com/OpenJ92/__dbm__/tree/master/src/struct)
Tree and Graph data structures upon which your database is imaged.

## Objects : [src/objects](https://github.com/OpenJ92/__dbm__/tree/master/src/objects)
Nodes generated provided the database implementation supplied.



