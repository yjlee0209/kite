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

	<c:if test="${resultCnt==1}">
		<h1> 회원 가입이 되었습니다. </h1>
	</c:if>
	
	<c:if test="${resultCnt==0 or resultCnt == -1}">
		<h1> 회원 가입중에 오류가 발생했습니다. </h1>
		<a href="regForm"> 회원가입하기. </a>    <!-- /op/member/reg -> /op/member/regForm -->
	</c:if>
	

	


</body>
</html>