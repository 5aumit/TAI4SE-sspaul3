package com.company.prashantrathod;

public class BankAccount {

    private int accountNumber;
    private double balance;
    private String name;
    private String email;
    private int phoneNumber;

    public void setAccountNumber(int accountNumber){
        this.accountNumber = accountNumber;
    }

    public void setBalance(double balance){
        this.balance = balance;
    }

    public void setPhoneNumber(int phoneNumber){
        this.phoneNumber = phoneNumber;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public int getAccountNumber(){
        return this.accountNumber;
    }

    public double getBalance(){
        return this.balance;
    }

    public int getPhoneNumber(){
        return this.phoneNumber;
    }

    public String getName(){
        return this.name;
    }

    public String getEmail(){
        return this.email;
    }

    public double depositFunds(double deposit, double balance){
        System.out.println("Current Balance: " + balance);
        balance = deposit + balance;
        setBalance(balance);
        System.out.println("Current Balance: " + balance);
        return balance;
    }

    public double withdrawFunds(double withdrawAmount, double balance){
        if (balance >= withdrawAmount){
            //System.out.println("Current Balance: " + balance);
            balance = balance - withdrawAmount;
            setBalance(balance);
            //System.out.println("Current Balance: " + balance);
            return balance;
        } else {
            //System.out.println("Current Balance: " + balance);
            System.out.println("Insufficienct Funds");
            return -1;
        }

    }


}
