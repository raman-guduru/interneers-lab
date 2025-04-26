const prodTitle = document.getElementById("prod-title");
const prodDesc = document.getElementById("prod-desc");
const prodPrice = document.getElementById("prod-price");
const prodQuantity = document.getElementById("prod-quantity");
const prodBrand = document.getElementById("prod-brand");

const apiUrl =
  "http://localhost:8000/inventory/products/67fb66234494994bca7311b2";

fetch(apiUrl)
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then((data) => {
    console.log("API Data:", data);
    prodTitle.textContent = data.name;
    prodDesc.textContent = data.description;
    prodPrice.textContent = `Price ${data.price}`;
    prodQuantity.textContent = `Quantity ${data.quantity}`;
    prodBrand.textContent = `Brand: ${data.brand}`;
  })
  .catch((error) => {
    console.error("Error fetching product data:", error);
  });
