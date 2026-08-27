package DaoImplements;

import java.time.LocalDate;
import java.util.List;

import javax.persistence.EntityManager;

import com.flover_shop.entity.Flower;
import com.flover_shop.entity.Orders;
import com.flover_shop.entity.User;
import com.flower_shop.dao.OrderDao;

public class OrderDaoImpl implements OrderDao{

	private final EntityManager maneger;
	
	
	
	
	
	public OrderDaoImpl(EntityManager maneger) {
		super();
		this.maneger = maneger;
	}

	public void save(Orders orders, User user, Flower flower) {
		maneger.getTransaction().begin();
		maneger.persist(orders);

		orders.setUser(user);
		orders.getFlowers().add(flower);
		maneger.merge(orders);
		maneger.getTransaction().commit();
	}

	public List<Orders> findAll() {

		maneger.getTransaction().begin();
		
		List<Orders> orders = maneger.createQuery(" from Orders").getResultList();
		maneger.getTransaction().commit();
		
		return orders;
	}

	public Orders findOne(LocalDate date) {

		maneger.getTransaction().begin();
		 Orders orders = null;
		 try{
			 orders = (Orders) maneger.createQuery("select o from Orders o where o.name =:value").setParameter("value", date).getSingleResult();
		 }
		 catch(Exception e){
			 System.out.println(e.getMessage());
		 }
		 maneger.getTransaction().commit();
		return orders;
	}

	public void remove(LocalDate date) {
		maneger.getTransaction().begin();
		Orders orders = findOne(date);
		maneger.remove(orders);
		
		maneger.getTransaction().commit();
		
	}

	public void update(Orders orders) {
		maneger.getTransaction().begin();
		maneger.merge(orders);
		maneger.getTransaction().commit();
		
	}

	public void addUserToOrders(User user, Orders orders) {
		maneger.getTransaction().begin();
		
		orders.setUser(user);
		
		maneger.getTransaction().commit();
		
	}

	public void addFloderToOrders(Flower flower, Orders orders) {
		maneger.getTransaction().begin();
		
		orders.getFlowers().add(flower);
		maneger.merge(orders);
		
		maneger.getTransaction().commit();
		
		
		
	}

}
