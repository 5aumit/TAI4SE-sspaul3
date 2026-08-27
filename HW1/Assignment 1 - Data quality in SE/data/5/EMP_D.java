import java.util.*;

import EMP_C.EMP_C;

public class EMP_D {
	
	public static void main(String[] args) {
		int id;
		String fn, ln;
		String addr1, addr2, city, state, country, phone;
		int sal;
		int count;
		
		Scanner scan = new Scanner(System.in);
		
		count = EMP_C.getctr();
		
		System.out.println("Enter the details for the employee");
		count++;
		EMP_C.setctr(count);
		id = 1000 + count;
		System.out.println("Enter employee first name:");
		fn = scan.nextLine();
		System.out.println("Enter employee last name:");
		ln = scan.nextLine();
		System.out.println("Enter employee street address:");
		addr1 = scan.nextLine();
		System.out.println("Enter employee apartment/building No.:");
		addr2 = scan.nextLine();
		System.out.println("Enter employee city:");
		city = scan.nextLine();
		System.out.println("Enter employee state:");
		state = scan.nextLine();
		System.out.println("Enter employee country:");
		country = scan.nextLine();
		System.out.println("Enter employee phone:");
		phone = scan.nextLine();
		System.out.println("Enter employee salary:");
		sal = scan.nextInt();
		EMP_C emp1 = new EMP_C(id, fn, ln, addr1, addr2, city, state, country, sal, phone);
		emp1.disp();
		scan.close();
	}
}