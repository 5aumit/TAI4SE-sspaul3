package com.oca_ocp.oca_ch6_working_methods_encapsulation;

public class Compile {
    public static void main(String[] args) {

        /*Q11 code snippet*/
        System.out.println("Q11 code snippet");

        A instance1 = new A(12,14);
        A instance2 = new A(12,14);

        System.out.println(instance1.equals(instance2)); // Option C : using equals method to access to private attributes from each
                                                         // other!

        B instance3 = new B(2,4);

        B instance4 = new B(82,45);

        instance3.a=5;

        System.out.println(instance1.instance5.b);// Option D : instance from A access to instance from B and access to
                                                  // protected attributes of B


    }

}


class A {

    private int a;
    private int b;
    public A(int a, int b) {
        this.a=a;
        this.b=b;
    }

    public int getA() {
        return a;
    }

    public int getB() {
        return b;
    }

    @Override
    public boolean equals(Object obj) {

        if(obj==this) return true;

        if (! (obj instanceof A)  ) return false;

        A a_obj = (A) obj;

        return Integer.compare(a,(a_obj).a) == 0 && Integer.compare(b,a_obj.b)==0;

    }

    protected B instance5 = new B(12,45);







}

class B {

    protected int a;
    protected int b;

    public B(int a, int b) {
        this.a = a;
        this.b = b;
    }
}