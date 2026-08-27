package com.ancaiyun.serviceImpl;

import com.ancaiyun.entity.Member;
import com.ancaiyun.entity.MemberExtraData;
import com.ancaiyun.mapper.MemberExtraDataMapper;
import com.ancaiyun.mapper.MemberMapper;
import com.ancaiyun.service.MemberExtraDataService;
import com.ancaiyun.utils.Constants;
import com.ancaiyun.utils.Result;
import org.apache.commons.lang.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.interceptor.TransactionAspectSupport;

@Transactional
@Service
public class MemberExtraDataServiceImpl implements MemberExtraDataService{
    @Autowired
    private MemberExtraDataMapper memberExtraDataMapper;
    @Autowired
    private MemberMapper memberMapper;
    @Override
    public Result updateMemberExtraDataStatus(String id, String extraDataStatus) {
        Result result = new Result();
        String code = Constants.FAIL;
        String msg = "初始化";
        try {
            if(StringUtils.isBlank(id)){
                code = "-3";
                msg = "请选择要审核的资料";
            }else if(StringUtils.isBlank(extraDataStatus)){
                code = "-4";
                msg = "请选择通过状态";
            }else if(!"1".equals(extraDataStatus) && !"2".equals(extraDataStatus)){
                code = "-5";
                msg = "审核状态只能是1或2";
            }else{
                MemberExtraData memberExtraData_db = memberExtraDataMapper.selectByPrimaryKey(id);
                if(memberExtraData_db == null){
                    code = "-6";
                    msg = "审核的资料不存在";
                }else{
                    Member member_db = memberMapper.selectByExtraDataId(id);
                    if(member_db == null){
                        code = "-7";
                        msg = "不存在任何会员有此资料";
                    }else{
                        member_db.setExtraDataStatus(extraDataStatus);
                        memberMapper.updateExtraDataStatusByPrimaryKey(member_db);
                        code = "-7";
                        msg = "操作成功";
                    }
                }
            }
        } catch (Exception e) {
            code = Constants.ERROR;
            msg = "后台繁忙";
            TransactionAspectSupport.currentTransactionStatus().setRollbackOnly();
            e.printStackTrace();
        }
        result.setCode(code);
        result.setMsg(msg);
        return result;
    }

    @Override
    public Result updateMemberExtraData(MemberExtraData memberExtraData) {
        Result result = new Result();
        String code = Constants.FAIL;
        String msg = "初始化";
        try {
            if(StringUtils.isBlank(memberExtraData.getId())){
                code = "-3";
                msg = "请选择要修改的资料";
            }else{
                MemberExtraData memberExtraData_db = memberExtraDataMapper.selectByPrimaryKey(memberExtraData.getId());
                if(memberExtraData_db == null){
                    code = "-4";
                    msg = "修改资料不存在";
                }else{
                    memberExtraDataMapper.updateByPrimaryKeySelective(memberExtraData);
                    code = "-5";
                    msg = "操作成功";
                }
            }
        } catch (Exception e) {
            code = Constants.ERROR;
            msg = "后台繁忙";
            TransactionAspectSupport.currentTransactionStatus().setRollbackOnly();
            e.printStackTrace();
        }
        result.setCode(code);
        result.setMsg(msg);
        return result;
    }
}
