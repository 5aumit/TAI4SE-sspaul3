package com.matias.bookings.domain;

public class Room {

    private Integer Id;
    private String title;
    private Integer peopleAmount;

    public Room(Integer id, String title, Integer peopleAmount) {
        Id = id;
        this.title = title;
        this.peopleAmount = peopleAmount;
    }

    public Integer getId() {
        return Id;
    }

    public void setId(Integer id) {
        Id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Integer getPeopleAmount() {
        return peopleAmount;
    }

    public void setPeopleAmount(Integer peopleAmount) {
        this.peopleAmount = peopleAmount;
    }
}
