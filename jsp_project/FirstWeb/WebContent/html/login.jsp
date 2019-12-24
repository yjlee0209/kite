<%@page import="member.LoginInfo"%>
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
		String uid = request.getParameter("uid");
		String pw = request.getParameter("pw");
	
		// JDBC 0> uid 로 select -> 결과가 존재하면 pw 비교
		
		String mid = "asdf@asdf.net";
		String mpw = "1234";
				
		if( uid != null && pw != null && uid.equals(mid) && pw.equals(mpw)){
			// 아이디와 비밀번호 모두 일치 -> 로그인 처리
			// 로그인 처리 : 회원의 정보를 객체로 만들고, 세션에 속정으로 저장
		
			LoginInfo info = new LoginInfo("홍길동", "hongkd@qwerty.com", "남자", 2000);
			session.setAttribute("loginInfo", info);
			
			response.sendRedirect("myPage1.jsp");
		} else {
	%>
		
		<script>
		
			alert('아이디 또는 비밀번호가 틀립니다.');
			location.href = 'login.html';
		
		</script>
		
	<%  } %>
	
	<a> 로그인 하기 </a>
	


</body>
</html>