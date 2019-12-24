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

	
	<!-- 
		MemberInfo member = (MemberInfo)request.getAttribute("member");
	
		MemberInfo member = new MamberInfo();
		request.setAttribure("member", member);
	-->
	
	<jsp:useBean id="member" class="member.MemberInfo" scope="request"/>
	<jsp:setProperty property="*" name="member" />
	
	<%= member %>
	
	<%-- <%
		member.setUname("son");
	%>


	<%= member.getByear() %> : <%= member.getUname() %> --%>

	<jsp:useBean id="loginInfo" class="member.LoginInfo" scope="session" />
	
	<%
		loginInfo.setId("asdf@asdf.com;");
	%>
	
	<%= loginInfo %>



</body>
</html>














