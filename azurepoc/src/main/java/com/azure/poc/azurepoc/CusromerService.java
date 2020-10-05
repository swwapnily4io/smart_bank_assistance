package com.azure.poc.azurepoc;

import java.util.HashMap;
import java.util.Map;


import org.springframework.http.HttpStatus;
import org.springframework.lang.NonNull;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CusromerService {

  @GetMapping("/login" )
  public Map<String, Object> login(@RequestParam @NonNull String userName, @RequestParam @NonNull String password) {
    Map<String,Object> response = new HashMap<String,Object>();
    System.out.println("Printing params "+userName + "password "+userName);
    if(null!= userName && !StringUtils.isEmpty(userName) && userName.equalsIgnoreCase("xoriant") && password.equalsIgnoreCase("xoriant123")) {
      response.put("status", HttpStatus.OK);
      response.put("loginStatus", "success");
      return response;
    }
    response.put("status", HttpStatus.NOT_FOUND);
    response.put("loginStatus", "failed");
    return response;
  }
}
