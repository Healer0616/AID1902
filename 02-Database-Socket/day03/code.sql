


高级查询
1子查询
一个查询语句中嵌套语句中嵌套另一个查询
-- 查询金额超过平均值的订单
select * from orders where amt >
(select avg(amt) from orders);
-- 查询所有名字以Ｄ开头的客户下的订单
select * from orders where cust_id IN
(select distinct cust_id
  from customer
  where cust_name like 'D%');
说明:
-括号中的部分称为子查询
-子查询可以返回一个值也可以多个值
 根据外层查询的要求来决定
-先执行子查询,将子查询的结果,作为外层查询的条件,再执行外层查询
#使用子查询的情况:一个语句无法查出来或者不方便查询
-- 订单中先找到所有客户编号
-- 再从客户表中去掉这一部分客户
select * from customer
where cust_id not in (
  select distinct cust_id from orders
);

2联合查询
1.什么是联合查询:也叫连接查询,将多个表中的数据进行连接,得到一个查询结果集
2.什么情况下使用:当从一个表无法查询到所有想要的数据时,使用联合查询
  前提:联合的表之间一定要有逻辑上的关联性
  SELECT a.order_id, a.amt,
         b.cust_name, b.tel_no
  from orders a,customer b  -- 别名
  where a.cust_id = b.cust_id;
3.笛卡尔积(联合查询的理论依据)
-什么是笛卡尔积:两个集合的乘积,产生一个新的集合
表示两个集合所有的可能的组合情况
-笛卡尔积和关系:笛卡尔积中 去掉没有意义或不存在的组合
就是关系(规范的二维表)

连接查询
-内连接(inner join):没有关联到的数据不显示
示例:查询订单编号 金额 客户名称 客户电话
-- 方式 --:where进行条件关联
select a.order_id,a.amt,
       b.cust_name,b.tel_no
from orders a, customer b
where a.cust_id = b.cust_id;

-- 方式二 --:利用inner join 关键字
select a.order_id, a.amt,
       b.cust_name, b.tel_no
from orders a inner join customer b
on a.cust_id = b.cust_id;

-外连接(outer join):没有关联到的数据也要显示到结果集
左连接:以左边为基准,右表的数据进行关联
      左表数据全部显示,右表中的字段
      如果没有关联到,则显示null
      left join 实现
select a.order_id, a.amt,
       b.cust_name, b.tel_no
from orders a left join customer b
on a.cust_id = b.cust_id;

右连接:以右边为基准,左表的数据进行关联
      右表数据全部显示,左表中的字段
      如果没有关联到,则显示null
      right join 实现
select a.order_id, a.amt,
       b.cust_name, b.tel_no
from orders a right join customer b
on a.cust_id = b.cust_id;

1.创建一个订单明细表(orders_detaill),包含的字段有:
  订单编号  order_id    字符串  32字符
  商品编号  product_id  字符串  32字符
  商品金额  amt         浮点数  2小数

create table orders_detaill(
  order_id varchar(32),
  product_id varchar(32),
  amt decimal(16,2)
) default charset=utf8;

2.在商品明细表中插入3笔数据(注意逻辑关联性)
INSERT INTO orders_detaill VALUES
  ('201801010001','p0001',80),
  ('201801010001','p0002',20),
  ('201801010003','p0003',200.00);

3.做三个表的联合查询,查询结果为:
订单编号 下单日期 客户名称 商品编号 商品金额
select a.order_id, a.order_date,
       b.cust_name,
       c.product_id, c.amt
from orders a, customer b, orders_detaill c
where a.cust_id = b.cust_id
and a.order_id = c.order_id;

约束(constraint)
1.什么是约束:数据必须遵循的规则
2.目的:保证数据一致性 完整性
  从数据库层面对数据进行"安检"
3.分类
非空约束
-定义:not null 要求字段的值不能为空
-语法:
字段名称 类型(长度) not null

唯一约束
-定义:unique 字段的值不能重复
-语法:
字段名称 类型(长度) unique

主键(primary key,简写pk):非空,唯一
-定义:主键在表中唯一标识 区分一个实体非空,唯一
-语法:
字段名称 类型(长度) primary key
示例:
create table t1(
  stu_no varchar(32) primary key, -- 主键
  stu_name varchar(32) not null,  -- 非空
  id_card_no varchar(32) unique   -- 唯一
);
-- 正常数据
insert into t1 values
('001','Jerry','513822199001011111');
-- 插入stu_name为空值数据,报错
insert into t1 values
('002',null,'513822199001011112');
-- 插入id_card_no为重复数据,报错
insert into t1 values
('003','Tom','513822199001011111');
-- 插入stu_no主键空值,报错
insert into t1 values
(null,'Lisa','513822199001011113');

默认值(default constraint)
-定义:指定某个字段的默认值,如果新插入一笔数据
没有对该字段赋值,系统会自动填入一个默认值
-语法:
字段名称 类型(长度) default 值

自动增长(auto_increment)
-定义:当字段被设置为自动增长时,插入时不需要赋值
系统在原最大值的基础上自动加1(要求:要求这个字段必须是pk
或设置了unique约束)
-语法:
字段名称 类型(长度) auto_increment
示例:
create table t2(
  id int primary key auto_increment,
  name varchar(32),
  status int default 0
);
insert into t2 VALUES(null,'Jerry',1);
insert into t2 VALUES(null,'Tom',2);
insert into t2(id,name) VALUES(null,'Hennry');

外键约束(foreign key,简称FK)
-什么是外键:一种约束,建立外键的前提是:
某个字段在当前表中不是PK,但在另外表
(也称为"外表")是主键
-作用:保证被参照的实体一定存在(参照的完整性)
-字段被设置外键约束后,影响有:当插入一个在外表中不存在的实体是,报错
当删除外表中已经被参照的实体,报错
-创建外键语法:
字段名称 类型(长度),
-- 所有字段定义完成后
constraint 外键名称 foreign key(当前表字段)
references 外表(字段名)
-示例:
创建course(课程信息表,主键course_id)
创建teacher(教师信息表,包含course_id,
    在course_id字段创建外键)
create table course(
  course_id varchar(32) primary key,
  name varchar(32)
);
create table teacher(
  id int auto_increment primary key,
  name varchar(32),
  course_id varchar(32),
  constraint fk_course foreign key(course_id)
  references course(course_id)
);
-- 在course表中插入一笔课程数据
-- (一个课程实体)
insert into course VALUES
('0001','python编程基础');
-- 再在tearcher表中插入一笔数据
-- 参照0001课程实体
insert into teacher VALUES
(1,'Jerry','0001'); --ok
-- 删除0001课程,报错
delete from course where xourse_id = '0001';
-- 在teacher表插入course_id为0003的信息
-- 报错,参照0003课程实体不存在
insert into teacher VALUES
(2,'Jerry','0003');

-外键使用的条件
 表的存储引擎必须为innoDB
 外键字段在另外表中必须是主键
 当前表,外表中字段类型必须一致

create table t6(
  id int,
  name varchar(32),
  status int,
  course_id varchar(4),
  tel_no varchar(32)
);
alter table t6 add primary key(id);
alter table t6 modify id int auto_increment;
alter table t6 modify status int default 0;
alter table t6 modify tel_no varchar(32) unique;
alter table t6 add constraint fk_course_id
foreign key(course_id)
references course(course_id);

数据导入导出
1.导出
show variables like 'secure_file%';
结果:/var/lib/mysql-files/
导出只能导出到该目录
导入只能从该目录导入
2.语法:
select 查询语句
into outfile '文件路径'
fields terminated by '字段分隔符'
lines terminated by '行分隔符'
3.示例:导出orders表中所有数据
select * from orders
into outfile '/var/lib/mysql-files/orders.csv'
fields terminated by ','
lines terminated by '\n';

-- 查看导出的文件:(Linux shell下执行)
sudo cat /var/lib/mysql-files/orders.csv
导入
语法:
load data infile '备份文件路径'
into table 表名称
fields terminated by ','
lines terminated by '\n';
示例:
-- 先删除orders表中数据,再执行导入
load data infile '/var/lib/mysql-files/orders.csv'
into table orders
fields terminated by ','
lines terminated by '\n';
-- 导入完成后,查询,确认

表的复制 重命名
1.表的复制
-- 将orders数据 表结构全部复制到orders_new表
create table orders_new
select * from orders;
-- 将orders表结构复制到orders_new表
create table orders_new
select * from orders where 1=0;
备注:该方式不会将键的属性复制到新表中

2.表的重命名
-- 将orders表重命名为orders_bak
alter table orders rename to orders_bak;





