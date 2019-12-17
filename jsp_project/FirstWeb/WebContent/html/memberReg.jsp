<!docytpe>
    <html>

    <head>
        <title>회원가입</title>
        <meta charset="UTF-8">
        <script
        	src="https://code.jquery.com/jquery-1.12.4.min.js"
        	integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ="
        	crossorigin="anonymous"></script>
        <link rel="stylesheet" href="default.css">
        
        <style>
        
            select.byear {
                width: 200px;
                height: 30px;
                
                font-size: 1.3em;
            }
            
        </style>
    </head>

    <body>

        <h1 class="title">회원가입</h1>
        <hr>

        <form action="memberReg.jsp" method="get">
            <table class="inputBox">
                <tr>
                    <td>아이디(이메일)</td>
                    <td><input type="text" name="uid"></td>
                </tr>
                <tr>
                    <td>비밀번호</td>
                    <td><input type="password" name="pw"></td>
                </tr>
                <tr>
                    <td>이름</td>
                    <td><input type="text" name="uname"></td>
                </tr>
                <tr>
                    <td>성별</td>
                    <td>남 <input type="radio" name="gender" value="m">
                       	여 <input type="radio" name="gender"value="w"></td>
                </tr>
                <tr>
                    <td>태어난 년도</td>
                    <td>
                        <select id="byear" class="byear" name="byear">
                        <%
                        	for(int i=2019 ; i>=1950 ; i--){                       
                        %>
                        	<option value='<% i%>'><% i%></option>	
                        <%
                        	};
                        %>
                            
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>사진</td>
                    <td><input type="file" name="pfile"></td>
                </tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="회원가입"></td>
                </tr>
            </table>
        </form>
        
        <script>
        
        	$(document).ready(function() {
				
        		var selectOptions = ' ';
        		
        		for(var i=2019; i>1950 ; i--){
        			selectOptions += '<option value="'+i+'">'+i+'</option>\n';
        		}
        		
        		$('#byear').html(selectOptions);
        		
        		
			});
        
        </script>
        
        
        
        
    </body>

    </html>
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    