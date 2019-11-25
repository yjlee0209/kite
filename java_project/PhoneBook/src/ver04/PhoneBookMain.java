package ver04;

public class PhoneBookMain {

	public static void main(String[] args) {

		//PhoneBookManager manager = new PhoneBookManager();
		PhoneBookManager manager = PhoneBookManager.getInstance();
		
		while (true) {
			System.out.println("========================");
			System.out.println("메뉴를 입력해주세요.");
			System.out.println("1. 대학 친구");
			System.out.println("2. 회사 친구");
			System.out.println("3. 친구 검색");
			System.out.println("4. 친구 삭제");
			System.out.println("5. 전체 목록");
			System.out.println("6. 종료");
			System.out.println("========================");

			int select = manager.sc.nextInt();
			manager.sc.nextLine();

			switch (select) {
			case 1:
				manager.insertInfor(select);
				break;
			case 2:
				manager.insertInfor(select);
				break;
			case 3:
				manager.searchInfor();
				break;
			case 4:
				manager.deleteInfor();
				break;
			case 5:
				manager.showAll();
				break;
			case 6:
				System.out.println("종료합니다.");
				break;
			}
		}

	}

}
