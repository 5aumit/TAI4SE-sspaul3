package net.risesoft.approve.service.impl;

import java.util.ArrayList;
import java.util.List;

import javax.annotation.PostConstruct;
import javax.annotation.Resource;
import javax.sql.DataSource;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import net.risesoft.approve.service.BdexDocTypeInfoService;

@Service(value="bdocTypeService")
public class BdexDocTypeInfoServiceImpl implements BdexDocTypeInfoService{

	@Resource(name = "routerDataSource")
	private DataSource routerDataSource;

	private JdbcTemplate jdbcTemplate;

	@PostConstruct
	private void afterIoc() {
		jdbcTemplate = new JdbcTemplate(this.routerDataSource);
	}

	
	/*
	 * 查询证照信息列表
	 * 
	 */
	@Override
	public List findById(String id) {
		List<Object> params = new ArrayList<Object>();
		String sql = "select * from T_BDEX_DOCTYPEINFO where doctypeguid = ?";
		params.add(id);
		return jdbcTemplate.queryForList(sql,params.toArray());
	}

	/*
	 * 删除证照信息
	 * 
	 */
	@Override
	public int deleteDocType(String guid) {
		List<Object> params = new ArrayList<Object>();
		String sql = "delete from T_BDEX_DOCTYPEINFO where guid=?";
		params.add(guid);
		return jdbcTemplate.update(sql,params.toArray());
	}


	/*
	 * 新建证照信息
	 * 
	 */
	@Override
	public int insert(String guid, String doctypeguid, String infocode,
			String infomemo, String glguid) {
		List<Object> params = new ArrayList<Object>();
		String sql = "insert into T_BDEX_DOCTYPEINFO values(?,?,?,?,null,?)";
		params.add(guid);
		params.add(doctypeguid);
		params.add(infocode);
		params.add(infomemo);
		params.add(glguid);
		return jdbcTemplate.update(sql,params.toArray());
	}
	
	
	/*
	 * 修改证照信息
	 * 
	 */
	@Override
	public int update(String guid,String infocode,String infomemo,String glguid) {
		List<Object> params = new ArrayList<Object>();
		String sql = "update T_BDEX_DOCTYPEINFO set infocode=?,infomemo=?,glguid=? where guid=?";
		params.add(infocode);
		params.add(infomemo);
		params.add(glguid);
		params.add(guid);
		return jdbcTemplate.update(sql,params.toArray());
	}

}
