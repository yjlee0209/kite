<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page trimDirectiveWhitespaces="true"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>다음 지도</title>
</head>
<body>

    <div id="map" style="width:500px;height:400px;"></div>
    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=f4cb3f702374dcf8ec06703df17cac2b"></script>
    <script>
        var container = document.getElementById('map'); 
        var options = { 
            center: new kakao.maps.LatLng(33.450701, 126.570667),
            level: 3 
        };
        var map = new kakao.maps.Map(container, options);
    </script>


</body>
</html>