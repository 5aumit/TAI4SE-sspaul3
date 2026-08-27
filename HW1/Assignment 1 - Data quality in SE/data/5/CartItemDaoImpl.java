package com.DaoImpl;

import com.Dao.CartItemDao;
import com.Dao.CartService;
import com.model.Cart;
import com.model.CartItem;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Repository
@Transactional
public class CartItemDaoImpl implements CartItemDao{

    @Autowired
    private SessionFactory sessionFactory;
    
    @Autowired
    private CartService cartService;

    public void addCartItem(CartItem cartItem) {
        Session session = sessionFactory.getCurrentSession();
        session.saveOrUpdate(cartItem);
        session.flush();
    }

    public void removeCartItem (CartItem cartItem) {
        Session session = sessionFactory.getCurrentSession();
        
        System.out.println("...............CartID="+cartItem.getCartItemId());
        if(cartItem.getQuantity()>1)
        {
        	double totalprice=cartItem.getTotalPrice();
        	double unitprice = (totalprice/cartItem.getQuantity());
        	double newtotalprice=unitprice*(cartItem.getQuantity()-1);
        	cartItem.setQuantity(cartItem.getQuantity()-1);
        	cartItem.setTotalPrice(newtotalprice);
        	session.saveOrUpdate(cartItem);
        	session.flush();
        	
        	Cart crt=cartService.getCartById(cartItem.getCart().getCartId());
        	double grandtot=crt.getGrandTotal();
        	crt.setGrandTotal(grandtot-unitprice);
        	session.saveOrUpdate(crt);
        	session.flush();

        }
        else if(cartItem.getQuantity()==1)
        {
        	session.delete(cartItem);
        	session.flush();
        	
        	Cart crt=cartService.getCartById(cartItem.getCart().getCartId());
        	crt.setGrandTotal(0.0);
        	session.saveOrUpdate(crt);
        	session.flush();
        }
        
    }

    public void removeAllCartItems(Cart cart) {
        List<CartItem> cartItems = cart.getCartItems();

        for (CartItem item : cartItems) {
            removeCartItem(item);
        }
    }

    public CartItem getCartItemByProductId (int productId) {
        Session session = sessionFactory.getCurrentSession();
        Query query = session.createQuery("from CartItem where productId = ?");
        query.setInteger(0, productId);
        session.flush();

        return (CartItem) query.uniqueResult();
    }
}

