package com.kodilla.good.patterns.challenges.Food2Door;

public class Food2DoorAplication {
    public static void main(String[] args) {

        Product product1 = new Product("Chia seeds", 1234);
        Product product2 = new Product("Chickpeas flour", 5678);
        Product product3 = new Product("Black maca", 1289);

        ProductOrder productOrder1 = new ProductOrder(product1,1.2);
        ProductOrder productOrder2 = new ProductOrder(product2,3.0);
        ProductOrder productOrder3 = new ProductOrder(product3,0.5);

        OrderProcessor processor = new OrderProcessor();

        processor.processOrder(new HealthyShop(), productOrder1);
        processor.processOrder(new GlutenFreeShop(), productOrder2);
        processor.processOrder(new ExtraFoodShop(), productOrder3);
    }
}
