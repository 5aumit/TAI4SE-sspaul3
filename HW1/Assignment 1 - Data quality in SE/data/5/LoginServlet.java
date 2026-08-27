package bankingproject.ui;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.log4j.Logger;

import bankingproject.dao.DaoException;
import bankingproject.dao.admin.AdminDao;
import bankingproject.dao.admin.AdminDaoImpl;
import bankingproject.dao.employee.EmployeeDao;
import bankingproject.dao.employee.EmployeeDaoImpl;
import bankingproject.domain.staff.Admin;
import bankingproject.domain.staff.Employee;

/**
 * Servlet implementation class LoginServlet
 */
public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	private final static Logger logger = Logger.getLogger(LoginServlet.class);
	
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginServlet() {
        super();
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String login = request.getParameter("login");
		String password = request.getParameter("password");
		
		logger.info("Log in with login " + login);
		
		EmployeeDao employeeDao = new EmployeeDaoImpl();
		
		try {
			logger.trace("Get employee with login " + login);
			Employee employee = employeeDao.getEmployee(login);
			
			if (employee == null) {
				AdminDao adminDao = new AdminDaoImpl();
				
				Admin admin = adminDao.getAdmin(login);
				
				if (admin == null) {
					request.setAttribute("message", "Login " + login + " does not exist");
					
					request.getRequestDispatcher("index.jsp").forward(request, response);
				}
				else if (!admin.getPassword().equals(password)) {
					request.setAttribute("message", "Password is incorrect");
					
					request.getRequestDispatcher("index.jsp").forward(request, response);
				}
				else {
					Cookie cookie = new Cookie("adminLogin", login);
					response.addCookie(cookie);
					response.sendRedirect("admin/mainPage.jsp");
				}
			}
			else if (!employee.getPassword().equals(password)) {
				request.setAttribute("message", "Password is incorrect");
				
				request.getRequestDispatcher("index.jsp").forward(request, response);
			}
			else {
				Cookie cookie = new Cookie("employeeLogin", login);
				response.addCookie(cookie);
				response.sendRedirect("employee/mainPage.jsp");
			}
		} catch (DaoException e) {
			// Go to error page
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}
	
}
