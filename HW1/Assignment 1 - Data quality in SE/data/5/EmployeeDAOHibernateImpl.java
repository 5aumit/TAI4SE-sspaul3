package com.codeinsyt.springboot.cruddemo.dao;

import java.util.List;

import javax.persistence.EntityManager;
import javax.transaction.Transactional;

import org.hibernate.Session;
import org.hibernate.query.Query;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.codeinsyt.springboot.cruddemo.entity.Employee;


@Repository
public class EmployeeDAOHibernateImpl implements EmployeeDAO {

	private EntityManager entityManager;
	
	@Autowired
	public EmployeeDAOHibernateImpl(EntityManager entityManager) {
		super();
		this.entityManager = entityManager;
	}



	@Override
	@Transactional
	public List<Employee> findAll() {
		
		//get current hibernate session
		Session currentSession = entityManager.unwrap(Session.class);
		
		//create query
		Query<Employee> theQuery = currentSession.createQuery("from Employee", Employee.class);
		
		//execute query
		List<Employee> employees = theQuery.getResultList();
		
		//currentSession.close();
		
		return employees;
	}



	@Override
	public Employee findById(long theId) {
		
		//get session 
		Session currentSession = entityManager.unwrap(Session.class);
		
		//query 
		Employee employee  = currentSession.get(Employee.class, theId);
		
		
		return employee;
	}



	@Override
	@Transactional
	public void save(Employee theEmployee) {
		Session currentSession = entityManager.unwrap(Session.class);
		currentSession.saveOrUpdate(theEmployee);
		
	}



	@Override
	@Transactional
	public void deleteById(long theId) {
		
		Session currentSession = entityManager.unwrap(Session.class);
		
		Query theQuery = currentSession.createQuery("delete from Employee where id=:empID");
		theQuery.setParameter("empID", theId);
		theQuery.executeUpdate();
		
	}

}
