<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page trimDirectiveWhitespaces="true"%>

<!DOCTYPE html>
<html>
<head>
	<title>날씨를 알아보자!!</title>
	
	<style>
        div.box {
            border : 5px solid #DDD;
            padding : 10px;
            margin : 5px;
            line-height: 160%;
            width: 300px;
            float: left;
        }
    </style>
    <meta charset="UTF-8">
	<script src="https://code.jquery.com/jquery-1.12.1.min.js"></script>
	
</head>
<body>

	<div>
		<input type="text" id="city"></input>	
	</div>
	<div>
		<input type="text" id="county"></input>	
	</div>
	<div>
		<input type="text" id="village"></input>	
    </div>
	<div>
        <button id="search"> 검색  </button>
	</div>
			
    <div id="weatherForecast"></div>
    
    <script type="text/javascript">
    	$(document).ready(function(){
    		
    		$("#search").click(function(){
    			
    			var city = $("#city").val();
    			var county = $("#county").val();
    			var village = $("#village").val();
    			var key = 'l7xx9cff6a0f1f314d908904d1e97b8d86db';
    			
    			$.ajax({
    				
    				url: 'http://apis.openapi.sk.com/weather/current/minutely',
    				dataType: 'json',
    				type: 'GET',
    				data: {
    					version: '2',
        				city: city,
        				county: county,
        				village: village,
        				appkey: key
    				},
    			
    				success: function(data){
	    				
    					var wthr = '';
    						    				
	    				$.each(data.weather.minutely, function(index, val) {

                            wthr += '<p><b>' + '관측 장소 : ' +val.station.name + ' <p> ' 
                            				 + '관측 시간 : ' +val.timeObservation + ' <p> ' 
                            				 + '현재 기온 : ' +val.temperature.tc + '&deg;C ' 
                            				 + '(최고 : ' + val.temperature.tmax + '&deg;C / 최저 : '+  val.temperature.tmin + '&deg;C) <p> ' 
                            				 + '대기 상태 : ' + val.sky.name + ' <p> '
                            				 + '풍속 : ' + val.wind.wspd + ' m/s <p> '
                            				 + '강수량 : '+ val.rain.sinceOntime + ' mm <p> '
                            				 + '습도 : '+ val.humidity + ' % <p> '
                            				 + '기압 : '+ val.pressure.surface + ' Ps <p> '

                        });
	    				$("#weatherForecast").html(wthr);
	    				
    				}    	
    			});
    		});
    	});
    
   
    	
    </script>

</body>
</html>