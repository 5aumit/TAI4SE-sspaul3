package cn.liu.controller;

import cn.liu.dto.GuruDTO;
import cn.liu.service.GuruService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Component
@RequestMapping("Guru")
public class GuruController {
    @Autowired
    private GuruService guruService ;


    @ResponseBody
    @RequestMapping("getData")
    private List<Map<String , Object>> getGuruFate(){
       List<Map<String , Object>> list = new ArrayList<>();
       String[] add = {"day1","day2","day3","day4","day5","day6","day7"};

        for (int i = 0; i < 7; i++) {
            HashMap<String, Object> map = new HashMap<>();
            Integer selectDTO = guruService.getSelectDTO(i);
            map.put("name" , add[i]) ;
            map.put("value" , selectDTO);
            list.add(map);

        }

        return  list ;
    }


    @ResponseBody
    @RequestMapping("getMonth")
    public List<Map<String , Object>> getMonth(){
        List<Map<String , Object>> list  = new ArrayList<>() ;
        List<GuruDTO> selectMonth = guruService.getSelectMonth();
        String[] month = {"一月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"};
        for (int i = 1; i <= 12; i++) {
            HashMap<String, Object> map = new HashMap<>();
            map.put("name",month[i-1]);
            System.out.println(month[i-1]);
            for (GuruDTO guruDTO : selectMonth) {
                if(guruDTO.getMonth()==i){
                    System.out.println(""+guruDTO);
                    map.put("value",guruDTO.getCount());
                }else{
                    map.put("value",0);
                }
            }
            list.add(map);

        }


        return list ;
    }

}
