-- 2019.11.25

-- CROSS JOIN : 테이블을 단순히 붙여준다.
-- JOIN -> 테이블을 집합으로 보고 집합의 곱 연산의 결과이다. -> N x M (결과 행이다)
select * 
from emp, dept;


-- EQUI JOIN
select *
from emp, dept
where emp.deptno=dept.deptno;


-- 이름이 'SCOTT' 인 사원의 소속부서의 이름을 이름과 함께 출력하자.
select ename, dname               -- emp.ename dept.dname
from emp, dept 
where emp.deptno=dept.deptno
and ename='SCOTT';

select ename, dname
from emp e, dept d              -- 별칭 사용
where e.deptno=d.deptno
and ename='SCOTT';

-- NON-EQUI JOIN
select e.sal, s.losal, s.hisal, e.ename, s.grade
from emp e, salgrade s
where sal between s.losal and s.hisal
order by s.grade;

-- SELF JOIN
select mgr
from emp
where ename='SMITH';

select ename
from emp
where empno='7902';

select e1.ename, e2.ename, d.dname
from emp e1, emp e2, dept d
where e1.mgr=e2.empno and e1.deptno=d.deptno
order by e1.mgr;

-- OUTER JOIN
select e.ename, m.ename
from emp e, emp m
where e.mgr=m.empno(+);

-- ANSI JOIN
-- CROSS JOIN
select * from emp, dept;
select * from emp cross join dept;  -- mysql, ms-sql, oracle

-- INNER JOIN
select * from emp e, dept d where e.deptno=d.deptno;
select * from emp e inner join dept d on e.deptno=d.deptno;
select * from emp inner join dept on emp.deptno=dept.deptno;

-- USING
select * from emp inner join dept using(deptno);

-- NATURAL
select * from emp natural join dept;

-- left|right|full OUTER JOIN
select * from emp e, emp m where e.mgr=m.empno(+);
select * from emp e inner join emp m on e.mgr=m.empno;   --null값으로 king 출력 안됨
select * from emp e left outer join emp m on e.mgr=m.empno;
select * from emp m right outer join emp e on e.mgr=m.empno;


-- 부속질의 : 쿼리 안에 쿼리 작성
-- select (부속질의) from (부속질의) where 컬럼 조건식 (부속질의)

-- emp 테이블에서 평균 급여보다 급여를 더 많이 받는 사원의 리스트를 출력
-- sal > 평균급여 <- 부속질의
select avg(sal) from emp;   -- 2073.2142
select ename, sal from emp where sal>2073.2142;

select * from emp where sal > ( select avg(sal) from emp );

-- 다중행 조건
-- 3000 이상 받는 사원이 소속된 부서(10번, 20번)와 동일한 부서에서 근무하는 사원출력
-- 3000 이상 받는 사원이 소속된 부서 : 부속질의
-- 동일한 부서에서 근무하는 사원출력
select ename, deptno
from emp
where deptno in ( select distinct deptno from emp where sal>=3000 );

-- 30번 소속 사원들 중에서 급여를 가장 많이 받는 사원보다 더 많은 급여를 받는 사원의 이름, 급여를 출력
-- 30번 소속 사원들 중에서 급여를 가장 많이 받는 사원 : 조건
select ename, sal from emp where deptno=30;
select ename, sal from emp where sal > all ( select sal from emp where deptno=30 );
select ename, sal from emp where sal > ( select max(sal) from emp where deptno=30 );

-- 부서번호가 30번인 사원들의 급여 중 가장 작은 값(950)보다 많은 급여를 받는 사원의 이름, 급여를 출력
-- 부서번호가 30번인 사원들의 급여 중 가장 작은 값(950)보다 : 부속질의
select ename, sal from emp where deptno=30;
select ename, sal from emp where sal > any ( select sal from emp where deptno=30 );
select ename, sal from emp where sal > ( select min(sal) from emp where deptno=30 );

-- ROWNUM
select ename, rownum from emp;


-- 스칼라 부속질의 : select 뒤에 위치하는 부속질의
-- 마당서점의 고객별 판매액을 보이시오(결과는 고객이름과 고객별 판매액을 출력).
select custid from orders order by custid;
select o.custid, (select name from customer c where c.custid=o.custid) name, sum(o.saleprice), trunc(avg(o.saleprice)), count(*)
from orders o 
group by o.custid;

-- 주문 정보를 출력해보자(주문번호, 고객 이름, 주문 금액)
select orderid, (select name from customer where orders.custid=customer.custid), saleprice from orders;
-- join
select o.orderid, c.name, o.saleprice from orders o, customer c where o.custid=c.custid;


-- 인라인 뷰 : from 절 뒤에 오는 부속질의 가상의 테이블로 사용
-- 고객 이름별 구매 금액의 합
select c.name, sum(o.saleprice)
from (select custid, name from customer where custid<=2)c, orders o
where c.custid=o.custid
group by c.name;

select * from (select custid, name from customer where custid<=2)c order by name;


-- ROWNUM
select ename, rownum from emp;
select ename, rownum from emp order by ename;
select ename, rownum from (select * from emp order by ename);




-- DDL

-- CREATE TABLE : 테이블 생성
-- 사원번호, 사원이름, 급여 3개의 칼럼으로 구성된 EMP01 테이블을 생성
create table emp01(
    empno number(4),     --사원 번호
    ename varchar2(20),  --사원 이름
    sal number(7, 2)     --급여   
);

drop table emp01;

desc emp01;

