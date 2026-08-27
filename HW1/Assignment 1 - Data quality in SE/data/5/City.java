package com.umbrella.model.internal.entity;

import org.springframework.data.jpa.domain.AbstractPersistable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Index;
import javax.persistence.Table;

@Entity
@Table(indexes =  {
        @Index(columnList = "city")
})
public class City extends AbstractPersistable<Long> {
    @Column(unique = true)
    private String city;

    public City() {
    }

    public City(String city) {
        this.city = city;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        //if (!super.equals(o)) return false;

        City city1 = (City) o;

        if (city != null ? !city.equals(city1.city) : city1.city != null) return false;

        return true;
    }

    @Override
    public int hashCode() {
        //int result = super.hashCode();
        int result = 31 * (city != null ? city.hashCode() : 0);
        return result;
    }
}
