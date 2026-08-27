package com.goshop.manager.controller;

import com.github.pagehelper.PageInfo;
import com.goshop.common.attachment.AttachmentService;
import com.goshop.common.exception.AjaxException;
import com.goshop.common.exception.PageException;
import com.goshop.common.utils.*;
import com.goshop.manager.pojo.Member;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import javax.imageio.ImageIO;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

@Controller
@RequestMapping(value =  "/pic")
public class PictureController {

    @Autowired
    AttachmentService attachmentService;

    @RequestMapping("/avatar_save")
    @ResponseBody
    public void avatarSave(Model model,
                             @RequestParam(value = "_pic") MultipartFile pic,
                             HttpServletRequest request,
                             HttpServletResponse response){
        Map<String,Object> jsonMap = new HashMap<>();
        try {
            File file= ImageUtils.save(pic, 500);
            String type = FileUtils.getFileType(pic.getOriginalFilename()).toLowerCase();
            String path=attachmentService.upload(file,type);
            jsonMap.put("status",1);
            jsonMap.put("url",path);
        } catch (Exception e) {
            e.printStackTrace();
            throw new AjaxException("保存图片错误:"+e.getMessage());
        }
        ResponseMessageUtils.textPlainResponse(response, JsonUtils.objectToJson(jsonMap));
    }

    @RequestMapping(value = "/pic_cut",method = RequestMethod.GET)
    public String index(Integer x,Integer y,Integer resize,
                        Integer ratio,String url,Model model, HttpServletRequest request) {
        File file=attachmentService.download(url);
        BufferedImage bi = null;
        try {
            bi = ImageIO.read(file);
        } catch (IOException e) {
            e.printStackTrace();
            throw new PageException("读取图片错误！");
        }
        int srcWidth = bi.getWidth(); // 源图宽度
        int srcHeight = bi.getHeight();
        model.addAttribute("width",srcWidth);
        model.addAttribute("height",srcHeight);
        model.addAttribute("x",x==null?120:x);
        model.addAttribute("y",y==null?120:y);
        model.addAttribute("resize",resize==null?1:resize);
        model.addAttribute("ratio",ratio==null?1:ratio);
        model.addAttribute("url",url);
        return "pic/pic_cut";
    }

    @RequestMapping(value = "/pic_cut",method = RequestMethod.POST)
    @ResponseBody
    public String  imageSave(
            @RequestParam("url")String url,
            @RequestParam("x1")Integer x1,
            @RequestParam("y1")Integer y1,
            @RequestParam("x2")Integer x2,
            @RequestParam("y2")Integer y2,
            @RequestParam("w")Integer width,
            @RequestParam("h")Integer height,
            @RequestParam("filename")String fileName,
            HttpServletRequest request,
            HttpServletResponse response){

        try {
            File file = attachmentService.download(url);
            String type = FileUtils.getFileType(url).toLowerCase();
            InputStream is = new FileInputStream(file);
            File tempFile = File.createTempFile("temp_images_"+ IDUtils.getUuid(),"."+type);
            ImageUtils.abscut(is, x1, y1, width, height, tempFile);
            String path=attachmentService.upload(tempFile,type);
            return path;
        }catch (Exception e){
            throw new PageException("文件保存错误！");
        }

    }
}
