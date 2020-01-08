create table num_tset(
  -- type是整数型，存储实际空间是4bytes
  -- 大小是由数据类型决定的
  -- int(3)表示默认显示3位
  -- unsigned表示无符号(0和整数)
  -- zerofill表示左边用0填充
  type int(3) unsigned zerofill,
  rate decimal(10,2)
);
-- 插入数据
1, 0.88      -- 正常值
2, 123.456   -- 小数部分超过定义长度
3, 2         -- 浮点数字段插入整数
1000, 3.444 -- 整数超过最大显示宽度

create table enum_test(
  name varchar(32),
  sex enum('boy','girl'),
  course set('music','dance','paint')
 );
 insert into enum_test
 values('jerry','girl','music,dance');
 -- 超过范围，报错
 insert into enum_test
 values('tom','boy','music,football');

-- 日期时间类型
select now(), sysdate(); -- 取当前时间
select curdate(), curtime(); -- 取当前日期
-- 分别取出当前时间中的年月日
select year(now()),month(now()),day(now());
-- 取出当前系统时间中日期，时间部分
select date(now()), time(now());

-- 修改某个订单的状态
update orders set status = 2
where order_id = '201801010001';
-- 修改订单的商品数量和订单金额
update orders
   set products_num = 2,
      amt = 400
 where order_id = '201801010002';

-- 删除记录
delete from orders
where order_id = '201801010002';

-- 查询比较符
select * from orders where amt < 200;

- and: 多个条件同时满足
- or: 满足其中一个

select * from orders
where (cust_id='c0001' or cust_id='c0003')
and status = 1;

范围比较
between...and...: 在...和...之间(包含两边)
in/not in: 在/不在某个指定的范围

select * from orders
where amt between 200 and 300;

select * from orders
where cust_id in ('c0003','c0004');

模糊查询(用的非常多)
格式:where 字段 like "通配字符"
通配符匹配
  下划线(_):匹配单个字符
  百分号(%):匹配任意字符
第一步:建立客户信息表
create table customer(
  cust_id varchar(32),
  cust_name varchar(32),
  tel_no varchar(32)
) default charset=utf8;
第二部:插入测试数据
insert into customer VALUES
('c0001','jerry','13512345678'),
('c0002','dekie','13522334455'),
('c0003','dokas','13544445555');
第三部:模糊查询
-- 查询所有名字以Ｄ开头的客户
select * from customer
where cust_name like 'D%';

select * from customer
where tel_no like '%44%55%';
注意事项:
模糊查询不精确匹配,速度较慢尽量避免%前置

判断空值:字段 is NULL
判断非空:字段 is not null
update customer
set tel_no = NULL
where cust_id = 'c0003';

select * from customer
where tel_no is null;

查询字句
order by:排序
格式: order by 字段 [asc/desc]
  asc-升序   desc-降序
select order_id,amt
from orders
order by amt desc;  -- asc或不写,升序

limit字句
作用:限制显示的笔数
limit n   只显示前面ｎ笔
limit m,n  从第ｍ开始,总共显示ｎ笔

-- 查询所有订单，显示２笔
select * from orders limit 2;
-- 查询所有订单，显示金额最大的２笔
select * from orders
order by amt desc limit 2;

-- insert into customer VALUES
-- ('c0011','dkgjg','13546645678'),
-- ('c0005','fdkhh','13525634455'),
-- ('c0006','eiytt','13578745555'),
-- ('c0007','ghijj','13512245678'),
-- ('c0008','djkdj','13335434455'),
-- ('c0009','dehgg','13656745555'),
-- ('c0010','tofjj','13587945678');

-- 利用limit分页:每页３笔数据
-- 第１页
select * from customer limit 0,3;
-- 第２页
select * from customer limit 3,3;
-- 第３页
select * from customer limit 6,3;

distinct字句
作用:去重数据
select distinct(要去重的字段)
from 表名

select distinct(cust_name)
from customer;

聚合函数
max    求最大值
MIN    求最小值
AVG    求平均值
SUM    求和
count  统计笔数

select max(amt) "最大金额",
       min(amt) "最小金额",
       avg(amt) "平均金额",
       sum(amt) "订单总金额"
from orders;

-- 统计订单的笔数
select count(*) from orders;

-- 统计电话号码以１３５开头的客户数量
-- 查customer表
select count(*) from customer where tel_no like '135%';

group BY
作用:对查询结果进行分组,通常和聚合函数搭配使用
-- 统计客户数量，按照客户名称分组
select cust_name,count(*)
from customer group by cust_name;
-- 从orders表,统计每种状态订单的总金额
select status,sum(amt)
from orders group by status;

having:对分组的结果进行过滤-- 需要和group by语句配合使用
group by 分组字段 having 过滤条件
-- 按照订单状态统计总金额
-- 查询结果中值保留总金额大于５００的统计结果
select status,sum(amt)
from orders group BY status
having sum(amt) > 500;
说明:group by 分组聚合的结果,只能用having,
    不能用where,where只能用户表中有的字段作为条件时候

表结构调整
-添加到表的最后一个字段
alter table 表名 add 字段名 类型(长度)
-添加到表的第一个字段
alter table 表名 add 字段名 类型(长度)

create table student(
  stu_no varchar(32),
  stu_name varchar(128)
);
添加字段
-- 在最后添加年龄字段
alter table student add stu_age int;
-- 将id字段添加到第一个字段
alter table student add stu_id int first;
-- 将tel_no添加到stu_name后面
alter table student add tel_no varchar(32)
after stu_name;

修改字段
修改字段类型
alter table 表名 modify 字段 类型(长度)
修改字段名称
alter table 表名
change 旧字段名 新字段名 类型(长度)
-- 修改student表stu_name字段长度为64
alter table student
modify stu_name varchar(64);
-- 将student中的id字段 改为 stu_id
alter table student
change id stu_id int;

删除字段
alter table 表名 drop 字段名
alter table student
drop stu_id;















