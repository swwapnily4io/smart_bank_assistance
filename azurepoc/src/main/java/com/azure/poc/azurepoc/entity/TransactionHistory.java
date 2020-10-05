package com.azure.poc.azurepoc.entity;

import java.util.Date;

public class TransactionHistory {

  private Date transactionDate;
  private long refNo;
  private String transactionType;
  private String description;
  private double amount;
  public TransactionHistory(Date transactionDate, long refNo, String transactionType, String description,
          double amount) {
    super();
    this.transactionDate = transactionDate;
    this.refNo = refNo;
    this.transactionType = transactionType;
    this.description = description;
    this.amount = amount;
  }
  public Date getTransactionDate() {
    return transactionDate;
  }
  public void setTransactionDate(Date transactionDate) {
    this.transactionDate = transactionDate;
  }
  public long getRefNo() {
    return refNo;
  }
  public void setRefNo(long refNo) {
    this.refNo = refNo;
  }
  public String getTransactionType() {
    return transactionType;
  }
  public void setTransactionType(String transactionType) {
    this.transactionType = transactionType;
  }
  public String getDescription() {
    return description;
  }
  public void setDescription(String description) {
    this.description = description;
  }
  public double getAmount() {
    return amount;
  }
  public void setAmount(double amount) {
    this.amount = amount;
  }
  
  
  
}
