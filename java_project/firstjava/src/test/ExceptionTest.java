package test;

public class ExceptionTest {

	public static void main(String[] args) {
		
		int number = 100;
		int result = 0;
		
		for(int i=0 ; i<10 ; i++) {
			try {
				result = number / (int)(Math.random()*10);
				System.out.println(result);
			} catch(ArithmeticException ae) {
				//System.out.println("0으로 나누기는 할수 없습니다.");
				
				//System.out.println(ae.getMessage());
			
				i--;
			} catch(ArrayIndexOutOfBoundsException aie) {
				
			} catch(Exception e) {
				
			}
			
		}

	}

}
