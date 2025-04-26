import { useState, useEffect } from "react";
import { Product } from "./Product";
import ProductDetail from "./ProductDetail";
import ProductForm from "./ProductForm";
import { Params, useParams } from "react-router-dom";

function ProductPage() {
  const params = useParams();
  const [data, setData] = useState<Product>();
  const [status, setStatus] = useState("detail");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const url = "http://localhost:8000/inventory/products/";
  const fetchData = async (params: Params) => {
    setLoading(true);
    try {
      const response = await fetch(url + params.id);
      if (!response.ok) {
        throw new Error(
          `HTTP error! status: ${response.status} ${response.text}`,
        );
      }
      const json: Product = await response.json();
      setData(json);
    } catch (err: any) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };
  useEffect(() => {
    fetchData(params);
  }, [params]);
  async function handleChange(product: Product) {
    setData(product);
    setStatus("detail");
  }
  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (data) {
    if (status === "detail") {
      return (
        <>
          <ProductDetail product={data} />
          <button onClick={() => setStatus("form")}>
            <p className="fa-solid fa-edit fa-lg"></p>
          </button>
        </>
      );
    } else if (status === "form") {
      return (
        <>
          <h2>Edit Product</h2>
          <button onClick={() => setStatus("detail")}>Cancel</button>
          <ProductForm
            onUpdate={handleChange}
            onCreate={handleChange}
            prevProduct={data}
          />
        </>
      );
    }
  }

  return null;
}

export default ProductPage;
