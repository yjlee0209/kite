<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page trimDirectiveWhitespaces="true" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<!--CDN 방식으로 jQuery 라이브러리를 로드-->
<script
	src="https://code.jquery.com/jquery-1.12.4.min.js"
    integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="
    crossorigin="anonymous"></script>
<style>
	* {
		margin : 0;
		padding : 0;
	}
</style>
</head>
<body>

	<c:set var="msg" value="users-123" />
	<h1>msg : ${msg}</h1>

	<c:if test="${msg eq'users-123'}">
		<h1>반갑습니다 ${msg}님!</h1>
	</c:if>


	<c:if test="${msg ne'users-12'}">
		<h1>로그인해주세요!</h1>
	</c:if>



</body>
</html>