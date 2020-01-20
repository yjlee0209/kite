create table project.MEMBER (
	ID int auto_increment primary key,
	EMAIL varchar(255),
	PASSWORD varchar(100),
	NAME varchar(100),
	REGDATE datetime,
	unique key (EMAIL)    
);
-- sysdate
INSERT INTO `project`.`member`
(`EMAIL`, `PASSWORD`, `NAME`, `REGDATE`)
VALUES
('test2@test2', '2222', 'tester2', now());
