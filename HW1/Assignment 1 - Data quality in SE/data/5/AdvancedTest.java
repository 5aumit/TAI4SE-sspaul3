package junittest;
import static org.junit.Assert.*;

import org.junit.After;
import org.junit.BeforeClass;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;

public class AdvancedTest {
	private static Calculator calculator=new Calculator();
	
	@Before
	public void clearCalculator(){
		calculator.clear();
	}
	@Test
	public void method1(){
		calculator.mi(2);
		assertEquals(4, calculator.getResult());
	}
	@Test
	public void method2(){
		calculator.mi(0);
		assertEquals(0,calculator.getResult());
	}
	@Test
	public void method3(){
		calculator.mi(-3);
		assertEquals(9, calculator.getResult());
	}
}
//import static org.junit.Assert.assertEquals;
//import org.junit.Test;
//import org.junit.runner.RunWith;
//import org.junit.runners.Parameterized;
//import org.junit.runners.Parameterized.Parameter;
//import org.junit.runners.parameterized.*;
//import java.util.Arrays;
//import java.util.Collection;
//
//@RunWith(Parameterized.class)
//public class AdvancedTest{
//	
//	private static Calculator calculator=new Calculator();
//	private int param;
//	private int result;
//	
//	@Parameters
//	public static Collection data(){
//		return Arrays.asList(new Object{
//			{2,4},
//			{0,0},
//			{-3,9},
//		});
//	}
	
	