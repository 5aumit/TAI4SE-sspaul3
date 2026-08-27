package cn.kgc.service.impl;

import cn.kgc.dao.houseMapper;
import cn.kgc.domain.*;
import cn.kgc.service.houseService;
import cn.kgc.domain.HouseCondition;
import cn.kgc.utils.pageUtils;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class HouseServiceImpl  implements houseService {
    @Autowired
    private houseMapper houseMapper;

    @Override
    public int addHouse(house house) {
        house.setIspass(0);
        return houseMapper.insertSelective(house);
    }

    @Override
    public List<Exhouse> findzhuyemian(Integer userid) {
        return houseMapper.findzhuyemian(userid);
    }

    @Override
    public Exhouse xiugaizhu(String id) {
        return houseMapper.xiugaizhu(id);
    }

    @Override
    public int xiugai(Exhouse exhouse) {
        return houseMapper.updateByPrimaryKeySelective(exhouse);
    }

    @Override
    public int delhouse(String id,Integer isdel) {
        Map m=new HashMap();
        m.put("id",id);
        m.put("isdel",isdel);
        return houseMapper.updateisdelbyid(m);
    }

    @Override
    public PageInfo<Exhouse> findallExhousebyispass(Integer ispass, pageUtils pageUtil) {
            PageHelper.startPage(pageUtil.getPage(),pageUtil.getRows());
            //查询所有
            List<Exhouse> list=houseMapper.findallExhousebyispass(ispass);
            return new PageInfo<Exhouse>(list);
    }

    @Override
    public int updateHousePassState(String id, Integer state) {
        house  house=new house();
        house.setId(id); //编号
        house.setIspass(state); //审核状态
        return this.houseMapper.updateByPrimaryKeySelective(house);
    }

    @Override
    public PageInfo<Exhouse> getHouseByBroswer(HouseCondition condition) {
        PageHelper.startPage(condition.getPage(),condition.getRows());
        List<Exhouse> houseByBroswer = houseMapper.getHouseByBroswer(condition);

        PageInfo<Exhouse> pageInfo=new PageInfo<>(houseByBroswer);
        return pageInfo;
    }

}
