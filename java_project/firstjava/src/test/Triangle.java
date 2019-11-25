package test;

public class Triangle {

	// 밑변과 높이 정보
	float width;     // 밑변
	float height;    // 높이
	
	// 밑변과 높이 정보를 변경시킬 수 있는 메서드
	void changeData(float width, float height) {
		this.width = width;
		this.height = height;
		
	}
	
	// 삼각형의 넓이를 계산하여 반환하는 메서드
	// 밑변 * 높이 / 2
	float area() {
//		float result = 0.0f;			
//		result = width*height/2;
		return width*height/2;  // result;
	}
	
	public static void main(String[] args) {
		
		Triangle t = new Triangle();
		
		System.out.println("높이 : " + t.height + "\t밑변 : " + t.width);
		
		t.changeData(3, 5);
		
		// 데이터 수정
		System.out.println("=========데이터 설정=========");
		System.out.println("높이 : " + t.height + "\t밑변 : " + t.width);
		System.out.println("\n\"삼각형의 넓이\" : " + t.area());
		
		
	}
	
}
