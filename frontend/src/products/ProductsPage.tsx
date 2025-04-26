import { useState, useEffect } from "react";
import { Product } from "./Product";
import ProductList from "./ProductList";
import ProductForm from "./ProductForm";

function ProductsPage() {
  const [data, setData] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [status, setStatus] = useState<string>("list");
  const url = "http://localhost:8000/inventory/products";
  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(
          `HTTP error! status: ${response.status} message: ${response.text}`,
        );
      }
      const json: Product[] = await response.json();
      setData(json);
    } catch (err: any) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };
  function handleCreate(product: Product) {
    setStatus("list");
    setData((data) => {
      return [...data, product];
    });
  }
  function handleUpdate(product: Product) {
    setStatus("list");
    setData((data) => {
      return data.map((item) => (item.id === product.id ? product : item));
    });
  }
  function handleDelete(product: Product) {
    setStatus("list");
    setData((data) => {
      return data.filter((item) => item.id !== product.id);
    });
  }
  useEffect(() => {
    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error?.message}</div>;
  }

  if (data) {
    return (
      <>
        {status === "list" ? (
          <>
            <h2>Products</h2>
            <button aria-label="add product" onClick={() => setStatus("form")}>
              <p className="fa-solid fa-plus"></p> Product
            </button>
          </>
        ) : (
          <>
            <h2>Create Product</h2>
            <button onClick={() => setStatus("list")}>
              <p className="fa-solid fa-times"></p> Cancel
            </button>
            <ProductForm
              onCreate={handleCreate}
              onUpdate={handleUpdate}
              prevProduct={null}
            />
          </>
        )}
        <ProductList products={data} onDelete={handleDelete} />
      </>
    );
  }
  return null;
}

export default ProductsPage;
