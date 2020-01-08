


索引
什么是索引:提高查询效率的一种技术
原理:根据某种一列(字段)进行分段,排序,通过避免全表扫描提高查询效率
索引分类

如何创建索引
语法:index | unique | primary KEY
示例:创建index_test表,在name字段上建立普通索引
    在cert_no上建立唯一索引

create table index_test(
  id int primary key,
  cert_no varchar(32),
  name varchar(32),
  unique(cert_no),index(name)
);

查看索引:show index from index_test;
insert into index_test VALUES
(1,'0001','Jerry');
insert into index_test VALUES
(2,'0001','Jerry'); -- cert_no违反约束

删除索引
-语法:drop index 索引名称 on 表名称
-示例:
-- 删除cert_no
drop index cert_no on index_test;
-- 删除名称为name的索引
drop index name on index_test;

修改表的方式添加索引
-语法:create 索引类型 索引名称 on 表(字段)
-示例:
 -- 在index_test表cert_no字段创建唯一索引
 create unique index idx_cert_no on index_test(cert_no);

实验:索引效率测试
第一步:利用现有的orders表,插入10万笔数据执行
      insert_orders_many.py文件
第二步:在没有索引的情况下查询,条件如下:
      order_id = '2018010100000002'
      order_id = '2018010100055555'
      order_id = '2018010100099999'
第三步:给orders表添加索引
      create index idx_order_id on orders(order_id);
      在执行第二步的查询,查看执行时间
备注:如果执行文件报错,检测连接参数核对字段的名称,顺序,类型
pymysql导入出错,因为缺少了pymysql模块,更换到教学机上执行

索引使用注意事项
-总体原则
 在合适的字段上,建立合适的索引
 索引不能太多,过多的索引会降低增删改查效率
-适合使用索引的情况
 在经常进行查询,排序,分组的字段上建立索引
 数据分布比较均匀,连续的字段,适合建立索引
 查询操作较多的表,适合建立索引
-不适合建立索引的情况
 数据量太少的表不适合建立索引
 增删改操作较多的表,不适合建立较多的索引
 某个字段取值范围很少,不适合建立索引
 某个字段很少用作查询,排序,分组,不适合建立索引
 二进制字段不适合建立索引

索引失效的sql语句
索引失效:表中有索引,但是查询时候没有使用
-没有使用索引字段作为条件
-条件判断中使用了<>符号
-条件判断语句中使用了null值判断
-模糊查询%前置 会导致放弃索引
-对字段做运算 会导致放弃索引

事务的特性(ACID特性)
1.原子性(Atomicity):一个事务是不可分割的整体,
  要么全部执行,要么全都不执行
2.一致性(Consistency):事务执行完成后,数据库
  从一个一致性状态变成下一个一致性状态
3.隔离性(Isolation):不同的事务不会相互影响
4.持久性(Durability):一旦事务提交,对数据库的
  修改会被持久保存到磁盘中

示例:
第一步:创建一个测试账户表
create table acct1(
  acct_no varchar(32),
  acct_name varchar(32),
  balance decimal(16,2)
);
insert into acct1 VALUES
('0001','Jerry',1000),
('0002','Tom',2000);



权限操作
授予权限
-语法:
 grant 权限列表 on 库名.表名
 to '用户名'@'客户端地址'
 [identified by '密码']
 [with grant option];
-说明
 权限列表:表示授予哪些权限
   all privileges:所有权限
   select:只授予查询权限
   select,insert:授予查询,插入权限
 库名.表名:




-- 第一步:创建Ｔｏｍ用户并授权
grant select,delete,insert,update on eshop.*
to 'Jerry'@'%'
identified by '123456';
-- select * from mysql.db where user='Tom'\G;
-- 第二步:刷新权限生效
flush privileges;
-- 第三步：使用Ｔｏｍ用户登录　执行一下操作
进入mysql库,失败
进入eshop库,成功
在eshop中执行查询,成功
在eshop中执行增删改,失败


grant select,delete,insert,update on eshop.*
to 'Jerry'@'localhost'
identified by '123456';

吊销权限
-语法:
 revoke 权限列表 on 库名.表名
 from '用户名'@'客户端地址';
-示例:吊销Ｊｅｒｒｙ用户ｅｓｈｏｐ库下的所有表的删除权限
 revoke delete on eshop.*
 from 'Jerry'@'localhost';
-- 刷新权限后,重新用ｊｅｒｒｙ登入验证




























