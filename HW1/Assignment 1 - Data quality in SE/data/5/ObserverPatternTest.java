package com.observerpatternjavacode;

import java.util.ArrayList;
import java.util.List;

public class ObserverPatternTest {

    public static void main(String[] args) {
        //Create a subject
        Subject demoSubject = new SubjectDemo();
        List<Observer> observers = new ArrayList<>(4);
        //Create observers
        for (int i = 1; i <= 5; i++) {
            observers.add(new ObserverDemo("User-" + i));
        }

        for (Observer observer : observers) {
            demoSubject.register(observer);
            observer.setSubject(demoSubject);
        }
        observers.get(0).update();
        demoSubject.postMessage("Hello!! Welcome to my Application");
    }
}