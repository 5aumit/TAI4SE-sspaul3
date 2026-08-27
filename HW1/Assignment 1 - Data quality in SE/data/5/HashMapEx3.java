package Ch11;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class HashMapEx3 {

	static HashMap phoneBook = new HashMap();

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		addPhoneNo("친구", "이자바", "010-1111-1111");
		addPhoneNo("친구", "이자바", "010-1111-1234");
		printList();
	}

	static void addPhoneNo(String groupName, String name, String tel) {
		addGroup(groupName);
		HashMap group = (HashMap) phoneBook.get(groupName);
		group.put(tel, name); // 이름은 중복될 수 있으니 전화번호를 key로 지정
	}

	// HashMap<Key, Value>
	static void addGroup(String groupName) {
		if (!phoneBook.containsKey(groupName)) { // 그룹이름이 새로 등록될 때만 아래 코드를 실행
			phoneBook.put(groupName, new HashMap()); // 그룹이름을 키, 새로운 해쉬맵을 값으로 활용
		}
	}

	static void printList() {
		// 프린트 리스트
		Set set = phoneBook.entrySet();
		Iterator it = set.iterator();

		while (it.hasNext()) {
			Map.Entry e = (Map.Entry) it.next();
			Set tmpSet = ((HashMap) e.getValue()).entrySet();
			Iterator tmpIt = tmpSet.iterator();
			System.out.println("*" + e.getKey() + "[" + tmpSet.size() + "]");
			while (tmpIt.hasNext()) {
				Map.Entry tmpE = (Map.Entry) tmpIt.next();
				System.out.println("이름  : " + tmpE.getValue() + ", 폰번호 : " + tmpE.getKey());
			}
		}
	}
}
