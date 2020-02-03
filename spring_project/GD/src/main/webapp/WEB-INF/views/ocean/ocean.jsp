<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
   <title>WFS Test</title>
   <script src="jquery-3.1.1.min.js" type="text/javascript"></script>
   <script src="OpenLayers.js" type="text/javascript"></script>
   <script src="http://www.khoa.go.kr/oceanmap/js/proj4js-1.1.0/lib/proj4js.js" type="text/javascript"></script>
   <script src="http://www.khoa.go.kr/oceanmap/js/proj4js-1.1.0/lib/defs/EPSG5179.js" type="text/javascript"></script>
   <script src="http://www.khoa.go.kr/oceanmap/js/gis/OtmsApi.js" type="text/javascript"></script>
   <!-- 개방海 지도 서비스 호출 -->
   <script src="http://www.khoa.go.kr/oceanmap/BASEMAP/otmsBasemapApi.do?ServiceKey=개방海에서 받은 서비스키" type="text/javascript"></script>
        
   <script type="text/javascript">
   var map;
     
   var OtmsLayer;
   var mapCenterX='956498.5710969';
   var mapCenterY='1819967.0629328';
   var numZoomLevels = 11;
   var zoomLevel = 1;
   var minZoomLevel = 0;
     
     
   // 지도의 영역을 지정
   var mapBounds = new OpenLayers.Bounds(123 , 32, 132 , 43);  
     
   // avoid pink tiles
   OpenLayers.IMAGE_RELOAD_ATTEMPTS = 3;
   OpenLayers.Util.onImageLoadErrorColor = "transparent";
 
   function init(){
       var options = {
           projection : new OpenLayers.Projection("EPSG:5179"), //지도의 좌표계
           displayProjection: new OpenLayers.Projection("EPSG:4326"),
           maxExtent : new OpenLayers.Bounds(-200000.0, -3015.4524155292, 3803015.45241553, 4000000.0),
           restrictedExtent : new OpenLayers.Bounds(37953.1466, 1126946.7253, 2152527.8074, 2873292.7040),
           center : new OpenLayers.LonLat(mapCenterX, mapCenterY),
           allOverlays: true,
           maxResolution : 1954.597389,//지도의 해상도
           numZoomLevels: numZoomLevels,
           zoom : zoomLevel,
           minZoom : minZoomLevel,
           transitionEffect : null,
           layers : [ OtmsLayer ],
           controls : [],
           // 사용자 이벤트 등록 
           eventListeners: {
               featureover: function(e) {  // feature에 마우스오버시
                   e.feature.renderIntent = "select";
                   e.feature.layer.drawFeature(e.feature);
                   console.log("featureover");
               },
               featureout: function(e) {   // feature에 마우스아웃시
                   e.feature.renderIntent = "default";
                   e.feature.layer.drawFeature(e.feature);
                   console.log("featureout");
               },
               featureclick: function(e) { // feature에 마우스클릭시
                   console.log("featureclick e.feature.id = " + e.feature.id);
               }
           }
           };
       map = new OpenLayers.Map('map', options);       // html의 'map'div 태그에 지도를 그려주도록 세팅
            
         
       // 지정된 바운드로 줌
       map.zoomToExtent( mapBounds.transform(map.displayProjection, map.projection ) );
       // 지도 센터 설정
       map.setCenter([mapCenterX,mapCenterY], minZoomLevel);
       // 지도 초기 레벨 설정
       map.zoomTo(1);
       // 지도 네비게이션 컨트롤
       map.addControl(new OpenLayers.Control.Navigation());
       // 개방海 WFS 오픈API 호출
       getWFS();
   }
     
   function getWFS() {
       var layerName = "TB_FACI_BEACH";    // 개방海 해수욕장정보 레이어 지정 
       var url = "http://www.khoa.go.kr/oceanmap/otmsWfsApi.do";
           url += "?ServiceKey=개방海에서 받은 서비스키";
           url += "&Layer=" + layerName;
         
       $.ajax({
           async:true,
           cache:false,
           type:"GET",
           url:encodeURI(url),
           data:{},
           dataType:"text", 
           success:function(response) {
               // 정상적으로 데이터를 받아오면 받은 데이터를 파싱하여 지도상에 feature배열을 그려준다.
               parseGML(response, layerName);
           },
           error:function(response) {
               // 데이터를 받아오지 못했을때 에러처리
               alert("처리오류로 인해 WFS정보를 가져오지 못했습니다.");
           }
       });
         
   }
 
   function parseGML(response, layerName) {
       // WFS GML의 값을 파싱하여 features 배열에 저장
       var features;
       var g = new OpenLayers.Format.GML();
       features = g.read(response);
         
       // features를 그려줄 랜더러 설정
       var renderer = OpenLayers.Util.getParameters(window.location.href).renderer;
       renderer = (renderer) ? [renderer] : OpenLayers.Layer.Vector.prototype.renderers;
         
       // features가 그려질 레이어 세팅
       var layer = new OpenLayers.Layer.Vector(layerName, 
               {
                   styleMap: "",
                   renderers: renderer
               });
       // 레이어에 features add
       layer.addFeatures(features);
       // 지도에 레이어 add
       map.addLayer(layer);
         
       // 지도 이벤트 등록    
       selectControl = new OpenLayers.Control.SelectFeature(layer);
       map.addControl(selectControl);
       selectControl.activate();
       layer.events.on({
           'featureselected': onFeatureSelect,
           'featureunselected': onFeatureUnselect
       });
         
       // 속성정보 팝업 X버튼 클릭시 호출
       function onPopupClose(evt) {
           var feature = this.feature;
           if (feature.layer) {
               selectControl.unselect(feature);
           } else { 
               this.destroy();
           }
       }
         
       // 마우스로 선택된 feature가 받는 이벤트-feature.data.NM , feature.data.ADDR 과 같이 컬럼을 지정
       function onFeatureSelect(evt) {
           feature = evt.feature;
           popup = new OpenLayers.Popup.FramedCloud("featurePopup",
                                    feature.geometry.getBounds().getCenterLonLat(),
                                    new OpenLayers.Size(100,100),
                                    "<h2>"+feature.data.NM + "</h2>" +
                                    feature.data.ADDR,
                                    null, true, onPopupClose);
           feature.popup = popup;
           popup.feature = feature;
           map.addPopup(popup, true);
       }
         
       // 마우스로 선택되지 않은 feature들이 받는 이벤트
       function onFeatureUnselect(evt) {
           feature = evt.feature;
           if (feature.popup) {
               popup.feature = null;
               map.removePopup(feature.popup);
               feature.popup.destroy();
               feature.popup = null;
           }
       }
   }
   </script>
</head>
  
<body onload="init()">
    <div id="map" style="height:600px;"></div>
</body>
  
</html>
