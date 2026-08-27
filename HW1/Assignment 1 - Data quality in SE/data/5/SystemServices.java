package com.peaceworld.wikisms.controller.ws_rs.common;

import javax.ejb.Stateless;
import javax.servlet.http.HttpServletRequest;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.Context;

import com.peaceworld.wikisms.controller.Utility;

@Stateless
@Path("/system")
public class SystemServices {
	
	@Path("/postconnection")
	@POST
	public String checkConnectionPost(@Context HttpServletRequest httpResuest)
	{
		String result="successful";
		Utility.invalidateSession(httpResuest);
		return result;
	}
	
	@Path("/getconnection")
	@GET
	public String checkConnectionGet(@Context HttpServletRequest httpResuest)
	{
		String result="successful";
		Utility.invalidateSession(httpResuest);
		return result;
	}
	
}

