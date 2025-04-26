import { useEffect, useState } from "react";
import { Product } from "./Product";
import { Category } from "./Category";

export interface Props {
  product: Product;
}

function Categories({ product }: Props) {
  const [data, setData] = useState<Category[]>([]);
  const [cats, setCats] = useState<Category[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const url = "http://localhost:8000/inventory/products/";
  const url1 = "http://localhost:8000/inventory/categories";
  const [status, setStatus] = useState("default");
  const [selectedCat, setSelectedCat] = useState("");

  function handleChange(event: any) {
    setSelectedCat(event.target.value);
  }

  async function handleDelete(cat: Category) {
    await fetch(url1 + "/" + cat.id + "/products/" + product.id, {
      method: "DELETE",
    });
    setData((cats) => cats.filter((item) => item.id !== cat.id));
  }

  async function handleAdd() {
    if (selectedCat === "") return;
    await fetch(url1 + "/" + selectedCat + "/products/" + product.id, {
      method: "POST",
    });
    fetchData(product);
    setStatus("default");
  }

  const fetchCat = async () => {
    setLoading(true);
    try {
      const response = await fetch(url1);
      if (!response.ok) {
        throw new Error(
          `HTTP error! status: ${response.status} ${response.text}`,
        );
      }
      const json: Category[] = await response.json();
      setCats(json);
    } catch (err: any) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  const fetchData = async (prod: Product) => {
    setLoading(true);
    try {
      const response = await fetch(url + prod.id + "/categories");
      if (!response.ok) {
        throw new Error(
          `HTTP error! status: ${response.status} ${response.text}`,
        );
      }
      const json: Category[] = await response.json();
      setData(json);
    } catch (err: any) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData(product);
    fetchCat();
  }, [product]);

  if (loading) {
    return <span className="loader"></span>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (data)
    return (
      <>
        <div className="type-list">
          <h4>Categories: </h4>
          {data.map((cat) => {
            return (
              <div
                key={cat.id}
                className="type"
                onClick={() => handleDelete(cat)}
              >
                {"-  " + cat.name}
              </div>
            );
          })}
          {status === "default" ? (
            <button onClick={() => setStatus("add-cat")}>
              <i className="fas fa-plus"></i>
            </button>
          ) : (
            <>
              <br></br>
              <select
                name="categories"
                value={selectedCat}
                onChange={handleChange}
              >
                <option value="">select category to add</option>
                {cats.map((cat) => (
                  <option key={cat.id} value={cat.id}>
                    {cat.name}
                  </option>
                ))}
              </select>
              <div>
                <button onClick={handleAdd}>
                  <i className="fas fa-check"></i>
                </button>
                <button onClick={() => setStatus("default")}>
                  <i className="fas fa-times"></i>
                </button>
              </div>
            </>
          )}
        </div>
      </>
    );

  return null;
}

export default Categories;
