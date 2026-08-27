package manager;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.*;

import db.DBconnection;
import entity.RouteInfo;
import entity.TimeTable;
import entity.TravelInfo;

public class TimeTableManager extends HttpServlet {

	DBconnection con = new DBconnection();
	TimeTable time = new TimeTable();
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs = null;
	
	private static final long serialVersionUID = 1L;

	public void doPost(HttpServletRequest request,HttpServletResponse response)
	        throws IOException, ServletException {    
		
	
		//String routename = request.getParameter("routename").toString();
		RouteInfo nroute = new RouteInfo();
		ArrayList<RouteInfo> a;
		
		a = nroute.CallRouting("", "Travel");
		
		for(int i=0; i<a.size(); i++){
			   //request.setAttribute("userid"+i, a.get(i).userid);
			   //request.setAttribute("routename"+i, a.get(i).routename);
			   request.setAttribute("id"+i, a.get(i).id);
			   request.setAttribute("startTime"+i, a.get(i).startTime);
			   request.setAttribute("timecount"+i, a.get(i).timecount);
			   request.setAttribute("stat"+i, a.get(i).stat);
			   request.setAttribute("train"+i, a.get(i).train);
			   request.setAttribute("trainCount"+i, a.get(i).traincount);
			   request.setAttribute("timer"+i, a.get(i).timer);
			   request.setAttribute("ctype"+i, a.get(i).ctype);
			   request.setAttribute("dest"+i, a.get(i).dest);
			   request.setAttribute("startDate"+i, a.get(i).startDate);
			   request.setAttribute("endDate"+i, a.get(i).endDate);
			   request.setAttribute("freeCount"+i, a.get(i).freeCount);
			   request.setAttribute("dateCount"+i, a.get(i).dateCount);
			   request.setAttribute("companyName"+i, a.get(i).companyName);
			   request.setAttribute("score"+i, a.get(i).score);
			   request.setAttribute("mealCount"+i, a.get(i).mealCount);
			   request.setAttribute("sleepCount"+i, a.get(i).sleepCount);
			   request.setAttribute("type"+i, a.get(i).type);
			}

		System.out.println(a.size());
			request.setAttribute("count",a.size());
		
		ServletContext context = request.getSession().getServletContext();
		RequestDispatcher rd  = context.getRequestDispatcher("/TimeTableView.jsp");
		
		rd.forward(request, response);
	}
	
	public void doGet(HttpServletRequest request,HttpServletResponse response)
	        throws IOException, ServletException {    
	}
}
