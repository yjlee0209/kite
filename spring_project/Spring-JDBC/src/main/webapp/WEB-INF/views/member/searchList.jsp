<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<h1> 회원 검색 </h1>
	<hr>
	검색 
	<form action="">
		<select name="stype">
			<option value="email"> Email </option>
			<option value="name"> Name </option>
			<option value="both"> Email + Name </option>		
		</select>
		<input type="text" name="keyword" placeholder="단어를 입력해주세요!">
		<input type="submit" value="검색">
	</form>
	<hr>
	<c:forEach items="${list}" var="member">
		<h3>${member}</h3>
	</c:forEach>


</body>
</html>