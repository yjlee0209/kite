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

	<%
		request.setAttribute("name", "홍길동");
	%>

	요청 URI : ${pageContext.request.requestURI} <br>
	request name 속성 값 : ${requestScope.name} <br>
	request 객체 생략 name 속성 값 : ${name} <br>
	session loginInfo 객체 : ${sessionScope.loginInfo} <br>
	session 객체 생략 loginInfo 객체 : ${loginInfo} <br>
	session loginInfo 객체 id : ${sessionScope.loginInfo.id}<br>
	session 객체 생략 loginInfo 객체 id : ${loginInfo.id)}<br>
	code 파라미터 : ${param.code}





</body>
</html>








