package com.example.demo.service.impl;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;

import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.entity.XxmpfBpmIndEmiDetalle;
import com.example.demo.entity.XxmpfBpmIndEmision;
import com.example.demo.pdf.NFAPdf;
import com.example.demo.service.NFAService;

@Service("nfaServiceImpl")
public class NFAServiceImpl implements NFAService{
	
	private static final Logger logger = LogManager.getLogger(NFAServiceImpl.class);
	
	@Autowired
	private EmisionServiceImpl emisionService;

	@PersistenceContext
    private EntityManager entityManager;
	
	@Override
	public List<String> distincSectorByFechaFin(String dateStart, String dateFinish) {
		logger.info("Method:distincSectorByFechaFin");
		List<String> resultList= entityManager.
			      createQuery("SELECT DISTINCT(emision.sector)  "
			      		     + "FROM XxmpfBpmIndEmision emision, XxmpfBpmIndEmiDetalle detalle"
			      		     + " WHERE emision.idEmision = detalle.idEmisionFK  AND"
			      		     + " detalle.area = 'Emisión' AND"
			      		     + " emision.fechaFin > TO_DATE('"+dateStart+"', 'DD/MM/YY') AND"
			      		     		+ " emision.fechaFin < TO_DATE('"+dateFinish+"', 'DD/MM/YY')" ).getResultList();		    
			  return resultList;
		//return emisionService.findDistincSectorByFechaFin(dateStart, dateFinish);
	}

	@Override
	public List<XxmpfBpmIndEmision> allEmisionByFechaFin(String dateStart, String dateFinish) {  
		logger.info("Method:allEmisionByFechaFin");
		/*List<Object[]> results = entityManager.createQuery("SELECT emision.idEmision, detalle.area, detalle.motivo  FROM XxmpfBpmIndEmision emision, XxmpfBpmIndEmiDetalle detalle WHERE emision.idEmision = detalle.idEmisionFK  AND detalle.area = 'EMISION' AND emision.fechaFin > TO_DATE('"+dateStart+"', 'DD/MM/YY') AND emision.fechaFin < TO_DATE('"+dateFinish+"', 'DD/MM/YY')").getResultList();

		for (Object[] result : results) {
			System.out.println(result[0] + " " + result[1] + " - " + result[2]);
		}*/
		TypedQuery<XxmpfBpmIndEmision> query = entityManager.
			      createQuery("SELECT emision  "
			      		+ "FROM XxmpfBpmIndEmision emision, XxmpfBpmIndEmiDetalle detalle "
			      		+ "WHERE emision.idEmision = detalle.idEmisionFK  AND"
			      		+ " detalle.area = 'Emisión' AND"
			      		+ " emision.fechaFin > TO_DATE('"+dateStart+"', 'DD/MM/YY') AND emision.fechaFin < TO_DATE('"+dateFinish+"', 'DD/MM/YY')", XxmpfBpmIndEmision.class);
			    List<XxmpfBpmIndEmision> resultList = query.getResultList();
			    return resultList;
	//	return emisionService.findAllEmisionByFechaFin(dateStart, dateFinish);
	}
	
	@Override
	public List<Object[]> allEmisionAndDetalleByFechaFin(String dateStart, String dateFinish) {
		logger.info("Method:allEmisionAndDetalleByFechaFin");
		List<Object[]> results = entityManager.
				createQuery("SELECT emision.folio, emision.sector, emision.tipoSolicitud, emision.divisional, emision.regional, "
						          + "emision.oficinaComercial, emision.agente, emision.estatus, emision.motivo, "
						          + "detalle.usuarioAnalista ,detalle.usuarioEmisor, detalle.usuarioSuscriptor, emision.fechaFin"
						+ " FROM XxmpfBpmIndEmision emision, XxmpfBpmIndEmiDetalle detalle"
						+ " WHERE emision.idEmision = detalle.idEmisionFK  AND"
						      + " detalle.area = 'Emisión' AND "
						      + "emision.fechaFin > TO_DATE('"+dateStart+"', 'DD/MM/YY') AND "
						      + "emision.fechaFin < TO_DATE('"+dateFinish+"', 'DD/MM/YY')").getResultList();
		return results;
	}

	@Override
	public Integer countBySector(List<XxmpfBpmIndEmision> listEmision, String sector) {
		logger.info("Method:countBySector");
		// TODO Auto-generated method stub
		return emisionService.countBySector(listEmision, sector);
	}

	@Override
	public List<String> distinctStatusByFechaFinAndSector(String dateStart, String dateFinish, String sector) {
		// TODO Auto-generated method stub
		logger.info("Method:distinctStatusByFechaFinAndSector");
		return emisionService.distinctStatusByFechfinAndaSector(dateStart, dateFinish, sector);
	}

	@Override
	public Integer countBySectorAndStatus(List<XxmpfBpmIndEmision> listEmision, String sector, String status) {
		logger.info("Method:countBySectorAndStatus");
		return emisionService.countBySectorAndStatus(listEmision, sector, status);
	}

}
