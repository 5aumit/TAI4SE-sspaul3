package com.aaa.controller;

import com.aaa.entity.ProviderInfo;
import com.aaa.service.ProviderInfoService;
import com.aaa.util.ResultMap;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
@RequestMapping("/provider")
public class ProviderController {
    @Resource
    public ProviderInfoService providerInfoService;

    @RequestMapping("/getProviderInfoList")
    @ResponseBody
    public Object getProviderInfoList(@RequestParam(value="page",required = false)Integer page,
                                      @RequestParam(value="limit",required = false)Integer limit,
                                      @RequestParam(value="proName",required = false)String proName)
    {
        Map<String,Object> map=new HashMap<>();
        map.put("start",(page-1)*limit);
        map.put("limit",limit);
        map.put("proName",proName);
        List<Map> mapList=providerInfoService.getProviderInfoList(map);
        int count=providerInfoService.getProviderCount(map);
        return new ResultMap<List<Map>>("",mapList,0,count);
    }

    @RequestMapping("/toAddProvider")
    public String toAddProviderInfo(){
        return "provider/addprovider";
    }

    @RequestMapping("/addprovider")
    @ResponseBody
    public Object saveAddProviderInfo(ProviderInfo providerInfo){
        boolean flag=providerInfoService.addProviderInfo(providerInfo);
        if (flag){
            return "true";
        }
        return "false";
    }

    //加载商品详细信息页面
    @RequestMapping(value = "/showProviderInfo/{proId}")
    public String showProviderInfo(Model model,@PathVariable("proId") int proId){
        ProviderInfo provider=providerInfoService.getProviderInfoById(proId);
        model.addAttribute("provider",provider);
        return "provider/showprovider";
    }

    @RequestMapping("/deleteProvider")
    @ResponseBody
    public Object deleteProviderInfo(int proId){
        boolean flag=providerInfoService.deleteProciderInfo(proId);
        if (flag){
            return "true";
        }
        return "false";
    }

    @RequestMapping("/toModifyProvider/{proId}")
    public String toModifyProviderInfo(Model model,@PathVariable int proId){
        ProviderInfo provider=providerInfoService.getProviderInfoById(proId);
        model.addAttribute("provider",provider);
        return "provider/modifyprovider";
    }


    @RequestMapping("/modifyProvider")
    @ResponseBody
    public Object modifyProviderInfo(ProviderInfo providerInfo){
        boolean flag=providerInfoService.modifyProviderInfo(providerInfo);
        if (flag){
            return "true";
        }
        return "false";
    }

}