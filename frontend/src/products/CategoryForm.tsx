import { Category } from "./Category";
import { SyntheticEvent, useState } from "react";

export interface Props {
  onUpdate: (category: Category) => void;
  onCreate: (category: Category) => void;
  prevCategory: Category | null;
}

function CategoryForm({ onUpdate, onCreate, prevCategory }: Props) {
  const url = "http://localhost:8000/inventory/categories";
  const [error, setError] = useState<string>("");
  const [product, setProduct] = useState<Category>(
    prevCategory ? prevCategory : new Category(),
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
      const updatedProduct = new Category({ ...product, ...change });
      return updatedProduct;
    });
  }
  async function handleSubmit(event: SyntheticEvent) {
    // console.log(product);
    if (prevCategory == null) {
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
        const res = new Category(await response.json());
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
        const res = new Category(await response.json());
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
        value={product?.name ? product?.name : ""}
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
      />
      <button onClick={handleSubmit}>SAVE</button>
      {error ? (
        <pre className="error">{JSON.stringify(error, undefined, 2)}</pre>
      ) : (
        ""
      )}
    </div>
  );
}

export default CategoryForm;
