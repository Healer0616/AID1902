-- homework_day2.sql
-- MySQL第二天作业

1. 创建数据库bank, 并指定为utf8编码格式

2. 创建账户表(acct, utf8编码格式), 包含如下字段
	acct_no   	账号，字符串类型，长度32字符
	acct_name 	户名，字符串类型，长度128字符
	cust_no   	客户编号，字符串类型，长度32字符
	acct_type	账户类型, 整数型(1-存款账户 2-贷款账户)
	reg_date	开户日期, 日期类型
	status		账户状态(1-正常 2-注销 3-挂失 4-冻结)
	balance   	数字类型，最长16位，2位小数

3. 至少插入五笔数据(要求数据尽量看上去真实)

4. 编写如下SQL语句
1)查找某个客户账户信息(以客户编号做条件)
2)查找余额大于等于5000的账户信息
3)查找余额大于等于5000的贷款账户信息
4)查找账户名称以'D'开头的所有账户信息
5)查找所有账户信息，并按照金额倒序排列
6)统计每种状态的账户笔数
7)查询账户余额的最大值、最小值、平均值、总金额
8)查询账户余额最大的前3笔订单


-- 1. 创建数据库bank, 并指定为utf8编码格式
create table bank(
  acct_no varchar(32),
  acct_name varchar(128),
  cust_no varchar(32),
  acct_type enum('1','2'),       -- (1-存款账户 2-贷款账户)
  reg_date date,
  status enum('1','2','3','4'),	         -- 账户状态(1-正常 2-注销 3-挂失 4-冻结)
  balance decimal(16,2)
) default charset=utf8;

-- 3. 至少插入五笔数据(要求数据尽量看上去真实)
INSERT INTO bank VALUES
  ('201801010001','zs','C0001',1,curdate(),1,10000.00),
  ('201801010002','ls','C0002',1,curdate(),1,20000.00),
  ('201801010003','ww','C0003',2,curdate(),1,30000.00),
  ('201801010004','zl','C0004',1,curdate(),1,40000.00),
  ('201801010005','qz','C0005',2,curdate(),1,50000.00),
  ('201801010006','kk','C0006',1,curdate(),3,60000.00),
  ('201801010007','jj','C0007',1,curdate(),4,70000.00);

-- 1)查找某个客户账户信息(以客户编号做条件
select * from bank
where cust_no = 'C0005';

-- 2)查找余额大于等于5000的账户信息
select * from bank
where balance >= 5000;

-- 3)查找余额大于等于5000的贷款账户信息
select * from bank
where balance >= 5000 and acct_type = 2;

-- 4)查找账户名称以'q'开头的所有账户信息
select * from bank
where acct_name like 'q%';

-- 5)查找所有账户信息，并按照金额倒序排列
select balance from bank
order by balance desc;

-- 6)统计每种状态的账户笔数
select status,count(*)
from bank group by status;

-- 7)查询账户余额的最大值、最小值、平均值、总金额
select max(balance),
       min(balance),
       avg(balance),
       sum(balance)
from bank;

-- 8)查询账户余额最大的前3笔订单
SELECT * FROM bank
ORDER BY balance DESC limit 3;












