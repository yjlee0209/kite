-- 11월 26일

-- check, default 제약 조건
drop table emp07;
create table emp07(
    empno number(4) constraint emp07_empno_pk primary key,
    ename varchar2(20) constraint emp07_ename_nn not null,
    sal number(7,2) constraint emp07_sal_chk check (sal between 500 and 5000),    -- sal >= 500 and sal <= 5000
    regdate date default sysdate
);

create table emp07(
    empno number(4),
    ename varchar2(20) not null,
    sal number(7,2),
    regdate date default sysdate,
    deptno number(2),
    constraint emp07_empno_pk primary key (empno),
    constraint emp07_sal_chk check (sal between 500 and 5000),
    constraint emp07_deptno_fk foreign key (deptno) references dept(deptno)
);


desc emp07;
-- 데이터 입력
/* insert into 테이블 이름 (컬럼....) values (data, .....) */
insert into emp07 (empno, ename, sal) values (null, null, 300);
insert into emp07 (empno, ename, sal) values (1000, null, 300);
insert into emp07 (empno, ename, sal) values (1000, 'son', 5001);
insert into emp07 (empno, ename, sal) values (1000, 'son', 3000);
select * from emp07;


-- 데이터 입력
/* insert into 테이블 이름 (행단위 입력에서 입력하고자 하는 컬럼들을 기술) values (기술된 컬럼에 입력할 데이터들을 입력) */
--입력할 컬럼의 개수와 입력할 데이터의 개수가 같아야 한다. 타입도 같아야 한다.

create table dept01
as
select * from dept where 1=0; 
desc dept01;
select * from dept01;

insert into dept01 (deptno, dname, loc) values (10, 'dev', 'seoul');
insert into dept01 values (20, 'design', 'jeju');



-- 데이터의 변경
/* UPDATE 테이블 이름 SET 변경 컬럼=새로운 DATA,... WHERE 조건식 (행선택)*/
drop table emp01;
create table emp01 as select * from emp;
select * from emp01;

update emp01 set deptno=20 where ename='SCOTT';


-- 급여가 3000 이상인 사원만 급여를 10% 인상
update emp01
set sal=sal * 1.1
where sal >= 3000;

-- 1987년에 입사한 사원의 입사일을 오늘 날짜로 변경
update emp01
set hiredate=sysdate
where substr(hiredate, 1, 2)=87;    -- hiredate >= '87/01/01' and hiredate <= '87/12/31'

-- SCOTT사원의 부서번호를 10번으로 변경, 직급을 MANAGER로 변경, 입사일을 오늘 날짜로 변경, 급여를 50%, 커미션을 4000오로 변경하자.
update emp01
set deptno=10, job='MANAGER', hiredate=sysdate, sal=50, comm=4000
where ename='SCOTT';

-- 20번 부서의 지역명을 40번 부서의 지역명으로 변경
drop table dept01;
create table dept01 as select * from dept;

select loc from dept01 where deptno=40;
select loc from dept01 where deptno=20;

update dept01
set loc=(select loc from dept01 where deptno=40)
where deptno=20;


-- 20번 부서의 부서이름과 지역을 40번 부서의 이름과 지역명으로 변경
update dept01
set dname=(select dname from dept01 where deptno=40), loc=(select loc from dept01 where deptno=40)
where deptno=20;
update dept01
set (dname, loc)=(select dname, loc from dept01 where deptno=40)
where deptno=20;

select * from dept01;

-- 데이터의 삭제
/* DELETE FROM 테이블 이름 WHERE 행 선택조건 : 행단위 삭제 */
delete from dept01 where deptno=10;
delete from dept01;

rollback;


-- VIEW : 기본 테이블을 기반으로 하는 가상테이블 (select의 결과를 테이블로 사용 )
select empno, ename, deptno from emp where deptno=30;
select * from emp_view30;
create or replace view emp_view30
as
select empno, ename, deptno from emp where deptno=30;
drop view emp_view30;


-- 인라인 뷰
-- 입사일이 빠른 5명을 순서대로 출력
select rownum, ename, hiredate from emp order by hiredate;

create or replace view emp_view_hire
as 
select ename, hiredate from emp order by hiredate;

select rownum , ename, hiredate from emp_view_hire where rownum<=5;

select rownum, ename, hiredate  from (
    select * from emp order by hiredate)
where rownum<6;           -- 단편적으로 사용할 경우 뷰를 만들필요는 없다


-- SEQUENCE : 자동 숫자 재생기
-- CURRVAL : 헌재 시퀀스의 값을 반환
-- NEXTVAL : 새로운 번호를 생성해서 반환
create sequence dept_deptno_seq
start with 10
increment by 10;

drop sequence dept_deptno_seq;

select dept_deptno_seq.nextval from dual;

create table dept03
as
select * from dept where 1=0;
drop table dept03;

select * from dept03;

insert into dept03 values(dept_deptno_seq.nextval, 'dev', 'seoul');
insert into dept03 values(dept_deptno_seq.nextval, 'dev');

rollback;


-- 인덱스 : 검색을 빠르게 지원
create index idx_emp_ename
on emp(ename);


