package ver05;

import java.util.ArrayList;
import java.util.Scanner;

// 기능 클래스
public class PhoneBookManager2 {

	// 객체 100개를 저장 : PhoneInfor 타입의 배열 생성, size : 100
	// 객체 생성 -> 배열에 객체 저장
	// -> 대학친구 객체, 회사친구 객체 : 메뉴 구성
	// 배열에서 검색 -> 검색 결과 출력
	// 배열에서 검색 -> 객체 삭제
	// 배열에서 전체 리스트 출력

	// 배열 생성 -> ArryList<PhoneInfor>
//	PhoneInfor[] pBook;
	ArrayList<PhoneInfor> pBook;
	

	// 추가한 데이터의 개수
	//int cnt;

	Scanner sc;

	// 싱글톤 패턴 : 인스턴스를 단 하나만 생성해서 사용하도록 처리
	// 1. 다른 객체에서 인스턴스 생성을 막는다 -> 생성자에 private 적용
	// 2. 인스턴스 자신이 인스턴스를 생성
	// 3. 외부에서 생성된 참조변수를 호출할수 있는 메서드를 생성

	public static PhoneBookManager2 getInstance() {
		if (m == null) {
			return new PhoneBookManager2();
		} else {
			return m;
		}
	}

	private static PhoneBookManager2 m = new PhoneBookManager2();

	private PhoneBookManager2() {
		pBook = new ArrayList<PhoneInfor>();
		sc = new Scanner(System.in);
	}

	// 입력 -> 대학 or 회사
	// 대학친구 입력 -> 1 , 회사친구 입력 -> 2
	// 검색 -> 3 , 삭제 -> 4

	void insertInfor(int select) {

		if (!(select == Menu.INSERT_UNIV || select == Menu.INSERT_COM)) {
			System.out.println("1 또는 2를 입력해주세요!");
			return;
		}

		// 기본정보 입력 받고
		System.out.println("이름을 입력해주세요.");
		String name = sc.nextLine();
		System.out.println("전번을 입력해주세요.");
		String phoneNumber = sc.nextLine();
		System.out.println("이멜을 입력해주세요.");
		String email = sc.nextLine();

		// 1또는 2에 따리 입력 받는다 -> 인스턴스 생성 -> 배열에 저장

		// 배열에 저장될 참조변수
		PhoneInfor pi = null;

		if (select == Menu.INSERT_UNIV) {
			System.out.println("주소를 입력해주세요.");
			String address = sc.nextLine();
			System.out.println("전공을 입력해주세요.");
			String major = sc.nextLine();
			System.out.println("학년을 입력해주세요.");
			String year = sc.nextLine();

			pi = new PhoneUnivInfor(name, phoneNumber, email, address, major, year);

		} else {
			System.out.println("회사를 입력해주세요.");
			String company = sc.nextLine();

			pi = new PhoneCompanyInfor(name, phoneNumber, email, company);

		}

		//pBook[cnt++] = pi;
		pBook.add(pi);
		
	}

	// 이름을 기준으로 배열에서 index 찾아 반환
	int searchIndex(String name) {
		int index = -1; // 찾지 못했을 때 반환값은 -1로 정의

		// List를 통해 이름 검색 : 반복문 이용
		// pBook[i] -> pBook.get(index)
		for (int i = 0; i < pBook.size() ; i++) {
			if (pBook.get(i).name.equals(name)) {
				index = i;
				break;
			}
		}
		return index;
	}

	// 이름을 통해 검색한 결과의 정보를 출력
	void searchInfor() {

		System.out.println("검색하실 이름을 입력해주세요.");
		String name = sc.nextLine();

		// index 검색
		int index = searchIndex(name);

		if (index < 0) {
			System.out.println("찾으시는 이름이 없습니다.");
		} else {
			pBook.get(index).showInfor();
		}

	}

	// 이름을 통해 검색한 결과의 정보를 삭제
	void deleteInfor() {

		System.out.println("삭제하실 이름을 입력해주세요.");
		String name = sc.nextLine();

		int index = searchIndex(name);

		try {

			pBook.remove(index);
			
//			for (int i = index; i < cnt - 1; i++) {
//				pBook[i] = pBook[i + 1];
//			}
//			// 전체 개수에서 -1
//			cnt--;
			System.out.println("삭제되었습니다.");
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("삭제하실 이름이 없습니다.");
		}

	}

	// 배열에 저장된 전체 데이터를 출력
	void showAll() {

		System.out.println("친구 리스트");
		System.out.println("_______________________");
		for (int i = 0; i < pBook.size(); i++) {
			pBook.get(i).showBasicInfor();
			System.out.println("-----------------------");
		}

	}

}