package cn.hexing.ami.web.action.main.arcMgt;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.apache.log4j.Logger;

import cn.hexing.ami.service.main.arcMgt.DataImpManagerInf;
import cn.hexing.ami.util.ActionResult;
import cn.hexing.ami.util.Constants;
import cn.hexing.ami.util.StringUtil;
import cn.hexing.ami.web.action.BaseAction;

public class DataImpAction extends BaseAction{
	
	private DataImpManagerInf dataImpManager;
	private static Logger logger = Logger.getLogger(DataImpAction.class.getName());
	
	private File MeterUpload;
	private File custUpload;
	private String importResult;
	//提示信息类型
	private String msgType;
	public DataImpManagerInf getDataImpManager() {
		return dataImpManager;
	}

	public void setDataImpManager(DataImpManagerInf dataImpManager) {
		this.dataImpManager = dataImpManager;
	}
	//导入文件
	public String uploadArchives(){
		ActionResult result = new ActionResult();
		String lang = getLang();
		try {
			Map<String, String> param=new HashMap<String, String>();
			String czyid=(String) session.getAttribute(Constants.CURR_STAFFID);
			String dwdm=(String) session.getAttribute(Constants.UNIT_CODE);
			String byqid=(String) session.getAttribute(Constants.FIRST_TRANS_ID);
			param.put("CURR_STAFFID", czyid);
			param.put("UNIT_CODE", dwdm);
			param.put("first_trans_id", byqid);
			
			//gprs
			if (MeterUpload!=null) {
				FileInputStream fis = new FileInputStream(MeterUpload);
				param.put("bjlxbz", "02");
				result = dataImpManager.parseExcel(fis, param,Constants.DA_BJ_GPRS,lang);
				//删除临时文件
				MeterUpload.delete();
			}
			
			//用户
			if (custUpload!=null) {
				FileInputStream fis = new FileInputStream(custUpload);
				result = dataImpManager.parseExcel(fis, param,Constants.DA_YH,lang);
				//删除临时文件
				custUpload.delete();
			}
		
		} catch (Exception e) {
			logger.error(getText("basicModule.dagl.dadr.import.failure")+StringUtil.getExceptionDetailInfo(e));
			result.setSuccess(false);
			result.setMsg("basicModule.dagl.dadr.importFail",getLang());
		}finally{
			
		}
		//输出信息
		response.setContentType("text/html;charset=UTF-8"); 
		try {
			response.getWriter().print("{success:'" + StringUtil.getString(result.isSuccess())
					+ "',msgType:'"+ StringUtil.getString(result.getDataObject()) +"', errMsg:'"
					+ StringUtil.getString(result.getMsg()) + "'}");
		} catch (IOException e) {
			logger.error(StringUtil.getExceptionDetailInfo(e));
		} 
		return null;
	}

	public File getMeterUpload() {
		return MeterUpload;
	}

	public void setMeterUpload(File meterUpload) {
		MeterUpload = meterUpload;
	}

	public File getCustUpload() {
		return custUpload;
	}

	public void setCustUpload(File custUpload) {
		this.custUpload = custUpload;
	}

	public String getImportResult() {
		return importResult;
	}

	public void setImportResult(String importResult) {
		this.importResult = importResult;
	}

	public String getMsgType() {
		return msgType;
	}

	public void setMsgType(String msgType) {
		this.msgType = msgType;
	}
}
