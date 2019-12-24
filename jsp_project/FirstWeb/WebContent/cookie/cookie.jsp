<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
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

	<h1>Cookie 정보</h1>

	<%
		Cookie[] cookies = request.getCookies();
	
		for(int i=0 ; i<cookies.length ; i++){
	%>	
		<%= cookies[i].getName() + " : "+ cookies[i].getValue() %> <br>		
	<% 		
		}
	
	%>



</body>
</html>