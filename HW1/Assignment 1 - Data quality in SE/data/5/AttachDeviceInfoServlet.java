package controller;
import entity.AttachDeviceInfo;
import entity.DeviceInfo;
import service.AttachDeviceInfoService;
import service.DeviceInfoService;
import tools.ReflectTools;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class AttachDeviceInfoServlet extends HttpServlet{
    AttachDeviceInfoService attachDeviceInfoService=new AttachDeviceInfoService();
    DeviceInfoService deviceInfoService = new DeviceInfoService();
    public void doGet(HttpServletRequest request,HttpServletResponse response)
    {
        try{
            String method=request.getParameter("method");
            if("add".equals(method)) {
                add(request,response);
            }else if("delete".equals(method)) {
                delete(request,response);
            }else if("update".equals(method)) {
                update(request,response);
            }else if ("updateTo".equals(method)) {
                updateTo(request, response);
            }else if ("get".equals(method)){
                get(request, response);
            }
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    public void doPost(HttpServletRequest request,HttpServletResponse response)
    {
        doGet(request,response);
    }
    private void add(HttpServletRequest request,HttpServletResponse response) throws Exception
    {
        AttachDeviceInfo attachDeviceInfo=ReflectTools.ReflectTo(request,AttachDeviceInfo.class);
        DeviceInfo deviceInfo = deviceInfoService.getDeviceInfo(attachDeviceInfo.getAttachDeviceID());
        deviceInfo.setDeviceState(3);
        deviceInfoService.update(deviceInfo);
        attachDeviceInfoService.insert(attachDeviceInfo);
        response.sendRedirect("/attachdeviceinfo.jsp");
    }
    private void delete(HttpServletRequest request,HttpServletResponse response)
    {
        try{
            String attachDeviceId=request.getParameter("attachDeviceId");
            String deviceId=request.getParameter("DeviceId");
            DeviceInfo deviceInfo = deviceInfoService.getDeviceInfo(attachDeviceId);
            deviceInfo.setDeviceState(1);
            deviceInfoService.update(deviceInfo);
            boolean flag=attachDeviceInfoService.delete(attachDeviceId,deviceId);
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    private void update(HttpServletRequest request,HttpServletResponse response)
    {
        try{
            AttachDeviceInfo attachDeviceInfo=ReflectTools.ReflectTo(request,AttachDeviceInfo.class);
            boolean flag=attachDeviceInfoService.update(attachDeviceInfo);
        }catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    private void updateTo(HttpServletRequest request,HttpServletResponse response) {
        try {
            request.getRequestDispatcher("/updateAttachDevice.jsp").forward(request, response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    private void get(HttpServletRequest request,HttpServletResponse response) {
        try {
            request.getRequestDispatcher("/attachdeviceinfo.jsp").forward(request, response);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
