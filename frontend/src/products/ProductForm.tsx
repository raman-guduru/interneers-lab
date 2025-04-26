import { Product } from "./Product";
import { SyntheticEvent, useState } from "react";

export interface Props {
  onUpdate: (product: Product) => void;
  onCreate: (product: Product) => void;
  prevProduct: Product | null;
}

function ProductForm({ onUpdate, onCreate, prevProduct }: Props) {
  const url = "http://localhost:8000/inventory/products";
  const [error, setError] = useState<string>("");
  const [product, setProduct] = useState<Product>(
    prevProduct ? prevProduct : new Product(),
  );
  async function handleChange(event: any) {
    let { type, name, value } = event.target;
    if (type === "number") {
      value = Number(value);
    }
    const change = {
      [name]: value,
    };
    setProduct((product) => {
      const updatedProduct = new Product({ ...product, ...change });
      return updatedProduct;
    });
  }
  async function handleSubmit(event: SyntheticEvent) {
    // console.log(product);
    if (prevProduct == null) {
      try {
        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify(product),
          headers: { "Content-Type": "application/json" },
        });
        if (!response.ok) {
          const res = await response.json();
          setError(res);
          throw new Error();
        }
        const res = new Product(await response.json());
        onCreate(res);
      } catch (err: any) {
        // setError(err.message);
      }
    } else {
      try {
        console.log(product);
        const response = await fetch(url + "/" + product.id, {
          method: "PATCH",
          body: JSON.stringify(product),
          headers: { "Content-Type": "application/json" },
        });
        if (!response.ok) {
          const res = await response.json();
          setError(res);
          throw new Error();
        }
        const res = new Product(await response.json());
        onUpdate(res);
      } catch (err: any) {
        // setError(err.message);
      }
    }
  }
  return (
    <div className="detail-container">
      <label htmlFor="name">Name</label>
      <input
        type="text"
        name="name"
        placeholder="name of the product"
        value={product?.name}
        onChange={handleChange}
      />
      <hr />
      <label htmlFor="brand">Brand</label>
      <input
        type="text"
        name="brand"
        placeholder="Product Brand"
        value={product?.brand}
        onChange={handleChange}
      />
      <hr />
      <label htmlFor="description">Description</label>
      <input
        type="text"
        name="description"
        placeholder="describe the product"
        value={product?.description ? product?.description : ""}
        onChange={handleChange}
      ></input>
      <hr />
      <label htmlFor="quantity">Quantity</label>
      <input
        type="number"
        name="quantity"
        placeholder="123"
        value={product?.quantity ? product?.quantity : ""}
        onChange={handleChange}
      />
      <hr />
      <label htmlFor="price">Price</label>
      <input
        type="number"
        step="any"
        name="price"
        placeholder="12.34"
        value={product?.price ? product?.price : ""}
        onChange={handleChange}
      />
      <hr />
      <button onClick={handleSubmit}>SAVE</button>
      {error ? (
        <pre className="error">{JSON.stringify(error, undefined, 2)}</pre>
      ) : (
        ""
      )}
    </div>
  );
}

export default ProductForm;
