package com.javarush.test.level20.lesson04.task04;

import java.io.*;

/* Как сериализовать static?
Сделайте так, чтобы сериализация класса ClassWithStatic была возможной
*/
public class Solution {

    public static Object object;

    public static void main(String[] args) throws Exception{

        ClassWithStatic classWithStatic = new ClassWithStatic();

        ObjectOutputStream oout = new ObjectOutputStream(new FileOutputStream("d:/3.txt"));
        oout.writeObject(classWithStatic);
        oout.flush();
        oout.close();

        ObjectInputStream oin = new ObjectInputStream(new FileInputStream("d:/3.txt"));
        object = oin.readObject();

        ClassWithStatic classWithStatic1 = (ClassWithStatic) object;

        System.out.println(classWithStatic1);
    }

    public static class ClassWithStatic implements Serializable {
        public static String staticString = "it's test static string";
        public int i;
        public int j;
    }
}
