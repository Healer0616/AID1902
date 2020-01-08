




查看mysql支持的存储引擎:show engines;
查看某个表的存储引擎
show create table 表名称;
修改表的存储引擎
alter table 表名称 engine = 引擎名称;
示例:
create table t3(
  id int primary key,
  name varchar(32)
) engine = innodb;
alter table t3 engine=myisam; -- 修改
查看:show create table t3;

常用的存储引擎特点
- innodb(mysql5.5及以后的版本默认)
特点:支持事务,支持行级锁,支持外键,共享表空间
文件构成:
*.frm:表的结构,索引
*.idb:表的数据

实验:查看表的存储文件
说明:通过下面的指令可以查看数据存储目录
show global variables like '%datadir%';
如果权限不够sudo -i进入root用户,
进入上面的目录查看
cd /var/lib/mysql/eshop
ls orders.*(查看orders表的存储文件)

什么时候选用innodb:
  更新(增删改)操作密集的表:
  要求支持数据事务,外键:
  自动灾备和恢复:
  要求支持自动增长(auto_increment)字段:
- myisam
特点:支持表级锁定:不支持事务,外键,行锁定功能
独占表空间:该类存储引擎容易损坏,所以灾备,恢复性能不佳
文件构成:
*.frm:表结构
*.myd:数据
*,myi:表索引
适用场合:
  查询请求较多:
  数据一致性要求较低:
  没有外键约束要求:
- memory
特点:表结构存与磁盘,数据存在内存中
     服务器重启或断电后,表中的数据丢失
文件:*.frm  表结构
使用场合:数据量小:数据需要快速访问:
        数据丢失不会造成损失:

第一步:修改t3的存储引擎为memory
 alter table t3 engine=memory;
第二步:查看文件
 sudo -i
 cd /var/lib/mysql/eshop
 ls t3.*
第三步:插入一条数据,查询(可以看到数据)
 insert into t3 values(1,'Jerry');
第四步:重启服务,在查询(数据消失)
 /etc/init.d/mysql restart














































































































