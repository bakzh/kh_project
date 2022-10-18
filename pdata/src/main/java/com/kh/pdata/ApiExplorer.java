package com.kh.pdata;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;

import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.io.BufferedReader;
import java.io.IOException;

public class ApiExplorer {
    private static final String serviceKey = "CdMg3a1Lo4r6sk%2BsrR2b18n%2BYLOpJUtsp16%2FEJomsiXcTof9t6wsYWB58y5nB9WGmlIDuaEj5xlzRnmnC29vnw%3D%3D";
    public static void main(String[] args) throws IOException {
        StringBuilder urlBuilder = new StringBuilder("http://www.kspo.or.kr/openapi/service/sportsNewFacilInfoService/getNewFacilInfoList"); /*URL*/
        urlBuilder.append("?" + URLEncoder.encode("serviceKey","UTF-8") + "=" + serviceKey); /*Service Key*/
        urlBuilder.append("&" + URLEncoder.encode("pageNo","UTF-8") + "=" + URLEncoder.encode("1", "UTF-8")); /*페이지번호*/
        urlBuilder.append("&" + URLEncoder.encode("numOfRows","UTF-8") + "=" + URLEncoder.encode("10", "UTF-8")); /*한 페이지 결과 수*/
        urlBuilder.append("&" + URLEncoder.encode("faciNm","UTF-8") + "=" + URLEncoder.encode("헬스", "UTF-8")); /*체육시설명*/
        urlBuilder.append("&" + URLEncoder.encode("fcobNm","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*업종명*/
        urlBuilder.append("&" + URLEncoder.encode("ftypeNm","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*시설유형명*/
        urlBuilder.append("&" + URLEncoder.encode("faciRoadAddr1","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*시설유형명*/
        urlBuilder.append("&" + URLEncoder.encode("faciAddr1","UTF-8") + "=" + URLEncoder.encode("", "UTF-8")); /*지번주소*/
        URL url = new URL(urlBuilder.toString());
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Accept", "application/xml");
        System.out.println("Response code: " + conn.getResponseCode());
        BufferedReader rd;
        if(conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
            rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        } else {
            rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
        }
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = rd.readLine()) != null) {
            sb.append(line);
        }
        rd.close();
        conn.disconnect();
        System.out.println(sb.toString());

        String xmlStr = sb.toString();
        //xml to json
        XmlMapper xmlMapper =  new XmlMapper();
        JsonNode node = xmlMapper.readTree(xmlStr);
        ObjectMapper jsonMapper = new ObjectMapper();
        String json = jsonMapper.writeValueAsString(node);
        System.out.println(json);

        //xml to java Object
        Response res = xmlMapper.readValue(xmlStr,Response.class);
        System.out.println(res);
        for(Response.Body.Item item : res.getBody().getItems()){
            if (item.getFaciStat() == "폐업") {
                System.out.println("시설명 : " + item.getFaciNm() + " | " + "운영상태 : " + item.getFaciStat());
            }else {
                System.out.println("시설명 : " + item.getFaciNm() + " | " + "운영상태 : " + item.getFaciStat());
            }
        }

        //json to java Object
        Response2 res2 = xmlMapper.readValue(json,Response2.class);
        System.out.println(res2);
        for(Response2.Body.Item item : res2.getBody().getItems()){
            if (item.getFaciStat() == "폐업") {
                System.out.println("시설명 : " + item.getFaciNm() + " | " + "운영상태 : " + item.getFaciStat());
            }else {
                System.out.println("시설명 : " + item.getFaciNm() + " | " + "운영상태 : " + item.getFaciStat());
            }
        }
    }
}