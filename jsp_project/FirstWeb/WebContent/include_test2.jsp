<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page trimDirectiveWhitespaces="true" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
	div {
		text-align: center;
		border: 1px solid #777;
	}
	div.left, div right {
		float : left;
		width : 49%;
	}
	div.footer {
		clear : 
	}

</style>
</head>
<body>

	<%@ include file="include/top.jsp" %>
	<%@ include file="include/left.jsp" %>
	<%@ include file="include/right.jsp" %>
	
	<jsp:include page="include/footer.jsp">
		<jsp:param value="2" name="menu_code"/>
		<jsp:param value="qwerty123@naver.com" name="email"/>
		<jsp:param value="010-1234-5678" name="tel"/>
	</jsp:include>
	
	
</body>
</html>