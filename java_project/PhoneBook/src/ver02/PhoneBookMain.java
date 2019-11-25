package ver02;

import java.util.Scanner;

import ver01.PhoneInfor;

public class PhoneBookMain {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		while(true) {
		
			System.out.println("----------------------------");
			System.out.println("이름을 입력해주세요.");
			String name = sc.nextLine();
			System.out.println("전화 번호를 입력해주세요.");
			String pNum = sc.nextLine();
			System.out.println("생일을 입력해주세요.");
			String bDay = sc.nextLine();
			
	
			//new PhoneInfor(name, phoneNumber, birthday)
			//new PhoneInfor(name, phoneNumber)
			//System.out.println("이름 : " + name + " 전번 : " + pNum + " 생일 : " + bDay);		
			//System.out.println("문자열의 개수 : " + bDay.trim().length());   // " " 공백(스페이스)도 문자열에 포함 , trim: 문자를 제외한 좌우의 여백을 지워준다.
			
			// 사용자가 입력한 생일 데이터 비교 : 공백 여부
			if(bDay != null && bDay.trim().length()>0) {
				new PhoneInfor(name, pNum, bDay).showInfo();
			} else {
				new PhoneInfor(name, pNum).showInfo();
			}
			
		}
			
		
	}

}
