package day50_Tuesday;

public class ClassNote {

    /*
what we can have inside an interface :
	 public static final field (CONSTANT)
	 abstract method ( NO-BODY!!!)
	 default method (MUST HAVE BODY : usually have default implementation)
	 static method (MUST HAVE BODY : NOT INHERITED, use in static way)

public interface Edible{
	public abstract void eat();
}

Edible e1 = new Edible() ; NO OBJECT !!!!!!!

ALL OF THEM ARE optional :
 is there any interface that has nothing inside ? YES
 its known as marker interface
 Examples of marker interfaces are the Serializable , Cloneable and Remote interfaces.
 These are used to indicate some information to compilers or JVMs

Where else have we seen default  :
 switch statement
 		String season = "winter";
 		switch(season){
 			case "spring":
 				// ski
 			.....
 			default:
 				// if nothing match come here !!!
 		}

 access modifer for
 		fields , methods , constructor
 		if there is no visible access modifer like public protected private
 			it means it has default access modifier
 			IT IS INVISIBLE , WE DONT SEE THE WORD DEFAULT HERE
 interface
 		default method :
 			a method that have default keyword in method delaration
 			and has default implementation (body)
 			THIS IS THE ONLY PLACE DEFAULT METHOD CAN EXISTS !!!

  constructor
  		default cosntructor that given by compiler
  		when a class does not have any constructor
  		WE DO NOT SEE THE WORD DEFAULT HERE , Its just a way to call it

  default values for
  		array items get default values
  		int[] nums = new int[5] ;   [0,0,0,0,0]
  		double[] nums = new double[3] ;   [0.0, 0.0 , 0.0]
  		boolean[] bools = new boolean[2] ;  [false , false]
  		........

  		what about for reference type
  		String[]  names = new String[2]  [null, null]
  		fields : instance or static field also gets default values
  			for whole numbers -->> 0
			for fractional numbers -->> 0.0
			for boolean  -->> false
			for char -->> empty char
			for any non-primitive types we get null !!!

     */
}
