package com.guang.bishe.domain;

public class Product {
    private Long productId;

    private String productNo;

    private String productName;

    private Long productSellerId;

    private Double productPrice;

    private Integer productStock;

    private String productTaste;

    private String productIsSell;

    private String productDescription;

    private String productPicture;

    private Integer productHassSelled;

    public Long getProductId() {
        return productId;
    }

    public void setProductId(Long productId) {
        this.productId = productId;
    }

    public String getProductNo() {
        return productNo;
    }

    public void setProductNo(String productNo) {
        this.productNo = productNo == null ? null : productNo.trim();
    }

    public String getProductName() {
        return productName;
    }

    public void setProductName(String productName) {
        this.productName = productName == null ? null : productName.trim();
    }

    public Long getProductSellerId() {
        return productSellerId;
    }

    public void setProductSellerId(Long productSellerId) {
        this.productSellerId = productSellerId;
    }

    public Double getProductPrice() {
        return productPrice;
    }

    public void setProductPrice(Double productPrice) {
        this.productPrice = productPrice;
    }

    public Integer getProductStock() {
        return productStock;
    }

    public void setProductStock(Integer productStock) {
        this.productStock = productStock;
    }

    public String getProductTaste() {
        return productTaste;
    }

    public void setProductTaste(String productTaste) {
        this.productTaste = productTaste == null ? null : productTaste.trim();
    }

    public String getProductIsSell() {
        return productIsSell;
    }

    public void setProductIsSell(String productIsSell) {
        this.productIsSell = productIsSell == null ? null : productIsSell.trim();
    }

    public String getProductDescription() {
        return productDescription;
    }

    public void setProductDescription(String productDescription) {
        this.productDescription = productDescription == null ? null : productDescription.trim();
    }

    public String getProductPicture() {
        return productPicture;
    }

    public void setProductPicture(String productPicture) {
        this.productPicture = productPicture == null ? null : productPicture.trim();
    }

    public Integer getProductHassSelled() {
        return productHassSelled;
    }

    public void setProductHassSelled(Integer productHassSelled) {
        this.productHassSelled = productHassSelled;
    }
}