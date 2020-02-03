<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ page trimDirectiveWhitespaces="true"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

   <meta charset="utf-8">
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
   
</head>
<body>

    <input id="city"></input>
    <button id='getWeatherForecast'>Get weather</button>

    <div id="showMetheForecast"></div>

    <script type="text/javascript">
        $(document).ready(function() {

            $("#getWeatherForecast").click(function() {

                var city = $("#city").val();
                var key = 'a3f6e2ae7bb5f17e77bb6ee99f6c4a0a';

                $.ajax({

                    url: 'http://api.openweathermap.org/data/2.5/weather',
                    dataType: 'json',
                    type: 'GET',
                    data: {
                        q: city,
                        appid: key,
                        units: 'metric'
                    },

                    success: function(data) {
                        var wf = '';

                        $.each(data.weather, function(index, val) {

                            wf += '<p><b>' + data.name + "</b><img src=http://openweathermap.org/img/wn/" + val.icon + ".png></p>" + data.main.temp + '&deg;C ' + ' | ' + val.main + ", " + val.description

                        });

                        $("#showMetheForecast").html(wf);

                    }

                });

            });

        });
    </script>


</body>
</html>