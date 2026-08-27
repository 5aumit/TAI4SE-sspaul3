package co.com.ceiba.estacionamiento.ceibaestacionamiento.servicios;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import co.com.ceiba.estacionamiento.ceibaestacionamiento.dominio.builder.ParqueaderoBuild;
import co.com.ceiba.estacionamiento.ceibaestacionamiento.dominio.constantes.Constantes;
import co.com.ceiba.estacionamiento.ceibaestacionamiento.dominio.modelo.Vehiculo;
import co.com.ceiba.estacionamiento.ceibaestacionamiento.entidad.ParqueaderoEntity;
import co.com.ceiba.estacionamiento.ceibaestacionamiento.repositorio.ParqueaderoRepositorio;

@Service
public class EntradaVehiculoService {
	
	@Autowired
	ParqueaderoRepositorio parqueaderoRepositorio;
	
	public void ingresarVehiculo (Vehiculo vehiculo) {
		ParqueaderoEntity parqueaderoEntidad =  ParqueaderoBuild.convertirHaciaEntidad(vehiculo);
		parqueaderoEntidad.setEstadoActivo(Constantes.ESTADO_ACTIVO);
		parqueaderoRepositorio.save(parqueaderoEntidad);
	}
	
	public int cantidadCuposUsados(String tipoVehiculo,boolean estadoActivo) {
		return parqueaderoRepositorio.countByTipovehiculoAndEstadoactivo(tipoVehiculo, estadoActivo);
		
	}
	
	public boolean vehiculoYaExiste(String placa,String tipoVehiculo,boolean estadoActivo) {
		return parqueaderoRepositorio.countByTipovehiculoAndPlacaAndEstadoactivo(tipoVehiculo, placa, estadoActivo) >=1;
		
	}

}
