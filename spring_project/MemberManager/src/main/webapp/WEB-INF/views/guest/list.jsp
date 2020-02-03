<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt"%>
<%@ page trimDirectiveWhitespaces="true"%>

<c:if test="${loginInfo eq null}">
<script>
	alert('로그인이 필요한 서비스입니다.');
	location.href='<c:url value="/member/login"/>';
</script>

</c:if>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<meta name="description" content="">
	<meta name="author" content="">

	<title>방명록 리스트</title>

	<!-- 기본 CSS 자리 시작 -->
	
	<%@ include file="/WEB-INF/views/include/basic.jsp" %>
	
	<!-- 기본 CSS 자리 끝 -->



<script>
	
</script>
</head>
<body>


	<!-- 헤더 시작 -->
	
	<%@ include file="/WEB-INF/views/include/header.jsp" %>
	
	<!-- 헤더 끝 -->
	
	
	<!-- 메인 컨텐트 시작 -->
	
    <main role="main" class="container">
      <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded box-shadow">
        <img class="mr-3" src="https://getbootstrap.com/assets/brand/bootstrap-outline.svg" alt="" width="48" height="48">
        <div class="lh-100">
          <h6 class="mb-0 text-white lh-100">방명록</h6>
          <small>2020</small>
        </div>
      </div>

      <div class="my-3 p-3 bg-white rounded box-shadow">
        <h6 class="border-bottom border-gray pb-2 mb-0">Recent updates</h6>
       
       	<table class="table">
       		<tr>
       			<th>no</th>
       			<th>제목</th>
       			<th>작성자</th>
       			<th>작성시간</th>
       			<th>관리</th>  			
       		</tr>
			
			<!-- 리스트 시작 -->
			<c:forEach items="${listView.list}" var="article" >
				<tr>
	       			<td> ${article.idx} </td>
	       			<td> ${article.title} </td>
	       			<td> ${article.writer} </td>
	       			<td> <fmt:formatDate value="${article.regdate}" pattern="yyyy. MM. dd"/> </td>
	       			<td>
	       				<a href="edit?idx=${article.idx}" class="btn btn-primary"> 수정 </a>
	       				<a href="javascript:del(${article.idx})" class="btn btn-danger"> 삭제 </a>
	       			</td>			
       			</tr> 
			</c:forEach>
      		<!-- 리스트 끝 -->
      		      		
       	</table>
       
       <div>
       	<c:forEach begin="1" end="${listView.totalPageCount}" var="i">
	    	<a href="list?page=${i}">[${i}]</a>   	
       	</c:forEach>
       
       </div>
       
       
       
      </div>

      <div class="my-3 p-3 bg-white rounded box-shadow">
        <h6 class="border-bottom border-gray pb-2 mb-0">방명록</h6>
			
		<c:forEach items="${listView.list}" var="article" >
        <div class="media text-muted pt-3">
          <!-- <img data-src="holder.js/32x32?theme=thumb&bg=007bff&fg=007bff&size=1" alt="" class="mr-2 rounded"> -->
          <div class="media-body pb-3 mb-0 small lh-125 border-bottom border-gray">
            <div class="d-flex justify-content-between align-items-center w-100">
              <strong class="text-gray-dark">${article.title}</strong>
              <a href="#">${article.writer}</a>             
            </div>
            <span class="d-block">${article.content}</span>
          </div>
        </div>
        </c:forEach> 
                
       </div>
    </main>
    
	<!-- 메인 컨텐트 끝 -->


	<!-- 푸터 시작 -->

	<%@ include file="/WEB-INF/views/include/footer.jsp" %>

	<!-- 푸터 끝 -->
	
	<script>
	
		function del(idx){
			
			if(confirm('삭제하시겠습니까?')) {
				location.href='delete?idx='+idx;
			}
			
		}
	
	</script>
	
	
</body>
</html>