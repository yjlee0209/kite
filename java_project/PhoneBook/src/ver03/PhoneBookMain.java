package ver03;

import java.util.Scanner;

import ver01.PhoneInfor;

public class PhoneBookMain {

	// 저장 공간 : 배열 생성
	static PhoneInfor[] pBook = new PhoneInfor[100];
	// 저장된 정보의 개수 : 저장시의 index, 배열의 반복의 조건, 저장된 정보의 개수
	static int cnt = 0;
	
	static Scanner sc = new Scanner(System.in);
	
	// 기능 : 전화번호 정보 저장, 검색, 삭제, 찾기(검색어로 배열의 index를 찾기)
	
	public static void main(String[] args) {
		
		while(true) {
			
			System.out.println("----------------------------");
			System.out.println("무엇을 하시겠습니까?");
			System.out.println("1.입력\t2.검색\n3.삭제\t4.종료");
			System.out.println("----------------------------");
			
			int menuNum = sc.nextInt();
			
			sc.nextLine();
			
			switch (menuNum) {
			case 1:
				insert();
				break;
			case 2:
				searchInfo();
				break;
			case 3:
				deleteInfo();
				break;
			case 4:
				System.out.println("프로그램을 종료합니다.");
				return;
			}
			System.out.println("----------------------------");
			
		}
	}

	public static void insert() {
			
		System.out.println("----------------------------");
		System.out.println("이름을 입력해주세요.");
		String name = sc.nextLine();
		System.out.println("전화 번호를 입력해주세요.");
		String pNum = sc.nextLine();
		System.out.println("생일을 입력해주세요.");
		String bDay = sc.nextLine();
		
		PhoneInfor pi = null;
		
		if(bDay != null && bDay.trim().length()>0) {
			pi = new PhoneInfor(name, pNum, bDay);
		} else {
			pi = new PhoneInfor(name, pNum);
		}
		
		pBook[cnt++] = pi;
		// 저장된 횟수 증가
		//cnt++;   //후위형으로 대체 가능
		
		System.out.println("정상적으로 저장되었습니다!");
		
		//System.out.println("저장된 정보의 개수는 : " + cnt);
		//pBook[cnt-1].showInfo();
		
	}
	
	public static int searchIndex(String name) {
		// index : 0 ~ N-1
		// index -> -1
		
		// 찾는 index가 없다의 의미 : -1
		int index = -1;
		
		// index 찾기 : i -> 0~cnt-1
 		for(int i=0 ; i<cnt ; i++) {
			if(pBook[i].name.equals(name)) {
				index = i;
				break;
			}
		}	
		return index;
	
	}
	
	public static void searchInfo() {
		
		System.out.println("찾고자하는 이름을 입력해주세요.");
		String name = sc.nextLine();
		
		int index = searchIndex(name);
		
		// index -> -1 : 검색 결과가 없다, 0~cnt-1
		if(index<0) {
			System.out.println("찾으시는 이름의 정보가 없습니다.");
		}else{
			pBook[index].showInfo();
		}
	}
	
	public static void deleteInfo() {
		
		System.out.println("삭제하고자하는 이름을 입력해주세요.");
		String name = sc.nextLine();
		
		int index = searchIndex(name);
		
		if(index<0) {
			System.out.println("찾으시는 이름의 정보가 없습니다.");
		}else{
			for(int i=index ; i<cnt-1 ;i++) {
				pBook[i] = pBook[i+1];
			}
			cnt--;
			System.out.println("삭제되었습니다.");
		}
		
	}

}













