package ver05;

public class PhoneBookMain {

	public static void main(String[] args) {

		//PhoneBookManager manager = new PhoneBookManager();
		//PhoneBookManager manager = PhoneBookManager.getInstance();
		//PhoneBookManager2 manager = PhoneBookManager2.getInstance();
		PhoneBookManager3 manager = PhoneBookManager3.getInstance();
		
		while (true) {
			System.out.println("========================");
			System.out.println("메뉴를 입력해주세요.");
			System.out.println(Menu.INSERT_UNIV + ". 대학 친구");
			System.out.println(Menu.INSERT_COM + ". 회사 친구");
			System.out.println(Menu.SEARCH + ". 친구 검색");
			System.out.println(Menu.DELETE + ". 친구 삭제");
			System.out.println(Menu.LIST + ". 전체 목록");
			System.out.println(Menu.EXIT + ". 종료");
			System.out.println("========================");

			int select = manager.sc.nextInt();
			manager.sc.nextLine();

			switch (select) {
			case Menu.INSERT_UNIV:
				manager.insertInfor(select);
				break;
			case Menu.INSERT_COM:
				manager.insertInfor(select);
				break;
			case Menu.SEARCH:
				manager.searchInfor();
				break;
			case Menu.DELETE:
				manager.deleteInfor();
				break;
			case Menu.LIST:
				manager.showAll();
				break;
			case Menu.EXIT:
				System.out.println("종료합니다.");
				return;
			}
		}

	}

}
