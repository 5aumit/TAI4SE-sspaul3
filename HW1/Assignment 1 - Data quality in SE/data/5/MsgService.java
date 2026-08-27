package msg;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.List;

import VO.DoctorVO;
import VO.MessageVO;
import msg.IMsgDao;
import msg.MsgDao;

public class MsgService extends UnicastRemoteObject implements IMsgService{
	private IMsgDao msgDao;
	
	public MsgService() throws RemoteException {
		msgDao = MsgDao.getInstance();
	}
	
	@Override
	public List<MessageVO> getAllMsg(int doctor_num) throws RemoteException {
		return msgDao.getAllMsg(doctor_num);
	}

	@Override
	public List<DoctorVO> getAllDoctor()throws RemoteException {
		return msgDao.getAllDoctor();
	}

	@Override
	public DoctorVO searchDoctor(int doctor_num)throws RemoteException {
		return msgDao.searchDoctor(doctor_num);
	}

	@Override
	public String searchDoctorName(int doctor_num)throws RemoteException {
		return msgDao.searchDoctorName(doctor_num);
	}

	@Override
	public int insertMsg(MessageVO msgVo) throws RemoteException {
		return msgDao.insertMsg(msgVo);
	}

	@Override
	public List<MessageVO> getAllReMsg(int doctor_num) throws RemoteException {
		return msgDao.getAllReMsg(doctor_num);
	}

}
