# Tips

> mysql版本5.7以上sql_mode ONLY_FULL_GROUP_BY,
即使用GROUP BY子句,查询列名只能为聚集函数或全部列名.
若不需使用ANY_VALUE,
相当于GROUP BY子句未包含列自动LIMIT 1.(Mysql独有,查找意义不明)
