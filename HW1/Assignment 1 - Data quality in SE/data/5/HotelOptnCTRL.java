package com.sprHotelMbts.projectT3.hotelOptn;

import java.util.HashMap;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HotelOptnCTRL {

	@Autowired
	private IHotelOptnSVC hotelOptnSvc;
	
	String viewPage;
	
	@RequestMapping("adHotelOptn")
	public String adHotelOptn(@Param("hotelOptn") String hotelOptn, @Param("hotelNo") String hotelNo, Model model) throws Exception
	{
		model.addAttribute("hotelNo", hotelNo);
		model.addAttribute("hotelOptn", hotelOptn);
		return "AdhotelOptn";
	}
	
	
	@RequestMapping("hotelOptnSltMulit")
	public String sltMulti(Model model, String hotelNo)
	{
		hotelOptnSvc.sltAll(model, hotelNo);
		return viewPage;
	}
	
	@RequestMapping("hotelOptnInsert")
	public String insert(@Param("hotelNo") String hotelNo, @ModelAttribute("hotelOptnNo") String hotelOptnNo, Model model, HttpServletRequest request)
	{
		HotelOptnDTO hotelOptnDto = new HotelOptnDTO();
		String[] arrayParam = request.getParameterValues("check");

		hotelOptnDto.setHotelNo(hotelNo);
		
		for (int i = 0; i < arrayParam.length; i++) 
		{
			hotelOptnDto.setHotelOptnNo(arrayParam[i]);
			hotelOptnSvc.insert(model, hotelOptnDto);
		}

		return "closePage";
		
	}

	@RequestMapping("hotelOptnDelete")
	@ResponseBody
	public String delete(Model model,@Param("hotelNo") String hotelNo, @Param("hotelOptnNo")String hotelOptnNo)
	{
		Map<String, Object> map = new HashMap<String, Object>();
		
		hotelOptnSvc.delete(model, hotelNo, hotelOptnNo);
		
		String msg = "정상 삭제되었습니다.";
		
		map.put("RESULT", msg);
		
		return msg;
		
	}
}