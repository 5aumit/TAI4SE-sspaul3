package org.Iteracion1.dao;

import org.hibernate.HibernateException;
import javax.persistence.Query;

import domain.Propietario;
import domain.Vehiculo;

public class PropietarioDao extends GeneralDao<Propietario> {
	public PropietarioDao() {
		super();
	}	
	
	public Propietario findByMatricula(String Matricula) throws HibernateException {
		Propietario propietario = null;
        try {
            startOperation();
            Query query=session.createQuery("from Vehiculo where matricula=?");
            query.setParameter(0, Matricula);
            Vehiculo vehicle=(Vehiculo) query.getSingleResult();
            propietario=vehicle.getPropietario();
            transaction.commit();
        } catch (HibernateException e) {
            throw e;
        } finally {
            HibernateFactory.close(session);
        }
        return propietario;
	}
}
