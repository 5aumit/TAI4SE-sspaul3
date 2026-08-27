package kh.chapter9_API.WrrapperTest;

public class WrapperTest {
	// 래퍼클래스란
	// 기본 자료형들을
	// 참조자료형처럼 사용하여
	// 여러 메소드 기능을 제공하는 클래스

	public void wrapperTest() {
		// String 을 특정 자료형으로 바꾸는 방법
		// 어떠한 데이터를 형태가 완전히 다른
		// 특정 데이터로 변경하는 것을 parse라고 한다.
		// 문자열 ---> 기본자료형
		byte b = Byte.parseByte("5");
		short s = Short.parseShort("10");
		int i = Integer.parseInt("100");

		float f = Float.parseFloat("3.14");
		double d = Double.parseDouble("3.14");

		boolean t = Boolean.parseBoolean("true");

		char ch = "text".charAt(0);

		// 기본 자료형 ---> 문자열
		String str1 = String.valueOf(1);

		String str2 = String.valueOf(3.14);

		String str3 = String.valueOf(false);

		String str4 = String.valueOf('A');
	}

	public static void main(String[] args) {
		WrapperTest wt = new WrapperTest();

		wt.wrapperTest();

	}
}
