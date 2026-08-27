import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;

import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class downloadTest extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        //通过路径得到一个输入流
        String path =     this.getServletContext().getRealPath("/WEB-INF/w.txt");
        FileInputStream fis =  new FileInputStream(path);
        //创建字节输出流
        ServletOutputStream sos  = response.getOutputStream();
        
        //得到要下载的图片文件名
        String filename = path.substring(path.lastIndexOf("\\"+ "w"));
            
        
        //告诉客户端需要下载图片（通过响应消息头）
        response.setHeader("content-disposition", "attachment;filename="+filename);
        
        //告诉客户端下载文件的类型
        response.setHeader("content-type", "txt");
        
        //执行输出操作
        int len = 1;
        byte[] b = new byte[1024];
        while((len=fis.read(b)) != -1){
            sos.write(b,0,len);
        }
        sos.close();
        fis.close();
        
    }

    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request,response);
    }

}
