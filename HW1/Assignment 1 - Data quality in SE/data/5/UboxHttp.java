package com.uboxpay;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.MessageDigest;
import java.util.Map;
import java.util.TreeMap;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.uboxpay.common.UboxConfigure;


/**
 * 
 */
public class UboxHttp{
	
	/**
	 * 测试参数
	 * */
	public static String appId="3aaf09c5ad33c60b5b1c4ce4bf9e2185";
	public static String appKey="9fea2b56b76b67a7566032f0fa101838";
	
	/**
     * 生产sign（签名字符串）
     * @param map 请求的参数数组(TreeMap类型，使获取的数组符合ascii顺序)
     * @param appKey 分配给第三方的app_key
     */
    public static String sign(TreeMap<String,Object> map,String appKey) throws Exception{
        String datasSign="";
        for(String s:map.keySet()){
        datasSign+=s+"="+map.get(s);

        }
        datasSign+="_"+appKey;

        //签名算法
        MessageDigest digest = java.security.MessageDigest.getInstance("SHA-1");
        digest.update(datasSign.getBytes());
        byte messageDigest[] = digest.digest();

        StringBuffer hexString = new StringBuffer();
        // 字节数组转换为 十六进制 数
        for (int i = 0; i < messageDigest.length; i++) {
            String shaHex = Integer.toHexString(messageDigest[i] & 0xFF);
            if (shaHex.length() < 2) {
                hexString.append(0);
            }
            hexString.append(shaHex);
        }
        return hexString.toString();
    }
    
    /**
     * @param sortedMap
     * @param url
     * 请求uboxApi接口方法
     * */
    public static Map<String,Object> example(TreeMap<String,Object> sortedMap,String url) throws Exception{
        
        //请求地址
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        // http正文内，因此需要设为true, 默认情况下是false; 
        con.setDoOutput(true); 

        // 设置是否从httpUrlConnection读入，默认情况下是true; 
        con.setDoInput(true); 

        // Post 请求不能使用缓存 
        con.setUseCaches(false); 
        con.setRequestProperty("Content-type", "application/x-www-form-urlencoded"); 
        con.setRequestMethod("POST");

        //拼接url参数
        String datas = "";
        for(String s:sortedMap.keySet()){
            datas+=s+"="+sortedMap.get(s)+"&";
        }

        //拼接sign参数信息，获取sign
        String datasWithSign=datas+"sign="+sign(sortedMap,UboxConfigure.appKey);
        //发送post请求  必须
        con.setDoOutput(true);
        DataOutputStream wr = new DataOutputStream(con.getOutputStream());
        wr.write(datasWithSign.getBytes());
        wr.flush();
        wr.close();

        BufferedReader in = new BufferedReader(
        new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer response = new StringBuffer();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();
        JSONObject parseObject = JSONObject.parseObject(response.toString());
        System.out.println("parseObject"+parseObject);
        Map<String,Object> result = (Map)JSON.parse(parseObject.getString("head"));
        int object = (int) result.get("return_code");
        Map<String,Object> body = null;
        if(object==200) {
        	body = (Map)JSON.parse(parseObject.getString("body"));
        	body.put("return_code", object);
        }else {
        	body = result;
//        	body = new HashMap<>();
//        	int return_code =  (int) result.get("return_code");
//        	String return_msg = (String) result.get("return_msg");
//        	body.put("return_code", return_code);
//        	body.put("return_msg", return_msg);
		}
        //打印结果，中文为unicode编码
		return body;
    }

}
