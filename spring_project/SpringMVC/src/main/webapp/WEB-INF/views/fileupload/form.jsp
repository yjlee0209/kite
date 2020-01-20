<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

	<h1>파일업로드</h1>
	<h2>@RequestParam 이용한 파일처리</h2>
	<hr>
	<form action="submit1" method="post" enctype="multipart/form-data">    <!-- method="post" enctype="multipart/form-data" 필수!!  -->
		학번 : <input type="text" name="sno"> <br>
		리포트 파일 : <input type="file" name="report"> <br>
		<input type="submit" value="전송">
	</form>

	<h2>MultipartHttpServletRequest 이용한 파일처리</h2>
	<hr>
	<form action="submit2" method="post" enctype="multipart/form-data">
		학번 : <input type="text" name="sno"> <br>
		리포트 파일 : <input type="file" name="report"> <br>
		<input type="submit" value="전송">
	</form>

	<h2>커맨드 객체를 이용한 파일처리</h2>
	<hr>
	<form action="submit3" method="post" enctype="multipart/form-data"> 
		학번 : <input type="text" name="sno"> <br>
		리포트 파일 : <input type="file" name="report"> <br>
		<input type="submit" value="전송">
	</form>





</body>
</html>