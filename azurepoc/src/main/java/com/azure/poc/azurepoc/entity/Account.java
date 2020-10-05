package com.azure.poc.azurepoc.entity;

import java.util.Date;

public class Account {

  private String userName;
  private long accountNo;
  private double balance;
  private Date createdOn;
  private String accountType;
  
  public Account(String userName, long accountNo, double balance, Date createdOn, String accountType) {
    super();
    this.userName = userName;
    this.accountNo = accountNo;
    this.balance = balance;
    this.createdOn = createdOn;
    this.accountType = accountType;
  }

  public String getAccountType() {
    return accountType;
  }

  public void setAccountType(String accountType) {
    this.accountType = accountType;
  }

  public String getUserName() {
    return userName;
  }

  public void setUserName(String userName) {
    this.userName = userName;
  }

  public long getAccountNo() {
    return accountNo;
  }

  public void setAccountNo(long accountNo) {
    this.accountNo = accountNo;
  }

  public double getBalance() {
    return balance;
  }

  public void setBalance(double balance) {
    this.balance = balance;
  }

  public Date getCreatedOn() {
    return createdOn;
  }

  public void setCreatedOn(Date createdOn) {
    this.createdOn = createdOn;
  }
  
  
  
}
