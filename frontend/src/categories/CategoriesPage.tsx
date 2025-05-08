import { useState, useEffect } from "react";
import { Category } from "../products/Category";
import CategoryForm from "../products/CategoryForm";
import { Product } from "../products/Product";
import ProductDetail from "../products/ProductDetail";
import { Link } from "react-router-dom";

function CategoriesPage() {
  const [data, setData] = useState<Category[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [sidebar, setSidebar] = useState<string>("list");
  const [status, setStatus] = useState<string>("list");
  const [products, setProducts] = useState<Product[]>([]);
  const [allProducts, setAllProducts] = useState<Product[]>([]);
  const [selectedProd, setSelectedProd] = useState("");
  const [categoryDisplayed, setCategoryDisplayed] = useState<Category | null>(
    null,
  );
  const url = "http://localhost:8000/inventory/categories";
  const url1 = "http://localhost:8000/inventory/products";
  const fetchData = async () => {
    setLoading(true);
    // await new Promise((resolve) => setTimeout(resolve, 5000));
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(
          `HTTP error! sidebar: ${response.status} message: ${response.text}`,
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
  const fetchProducts = async (category: Category | null) => {
    if (!category) return;
    setLoading(true);
    // await new Promise((resolve) => setTimeout(resolve, 5000));
    try {
      const response = await fetch(url + "/" + category?.id + "/products");
      if (!response.ok) {
        throw new Error(
          `HTTP error! sidebar: ${response.status} message: ${response.text}`,
        );
      }
      const json: Product[] = await response.json();
      setProducts(json);
    } catch (err: any) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };
  function handleCreate(category: Category) {
    setSidebar("list");
    setData((data) => {
      return [...data, category];
    });
  }
  function handleUpdate(category: Category) {
    setStatus("list");
    setCategoryDisplayed(category);
    setData((data) => {
      return data.map((item) => (item.id === category.id ? category : item));
    });
  }
  async function handleDelete(category: Category) {
    setSidebar("list");
    await fetch(url + "/" + category.id, { method: "DELETE" });
    setData((data) => {
      return data.filter((item) => item.id !== category.id);
    });
  }
  async function handleRemove(product: Product) {
    await fetch(url + "/" + categoryDisplayed?.id + "/" + product.id, {
      method: "DELETE",
    });
    setProducts((data) => {
      return data.filter((item) => item.id !== product.id);
    });
  }
  function handleChange(event: any) {
    setSelectedProd(event.target.value);
  }
  async function fetchAllProducts() {
    setLoading(true);
    // await new Promise((resolve) => setTimeout(resolve, 5000));
    try {
      const response = await fetch(url1);
      if (!response.ok) {
        throw new Error(
          `HTTP error! status: ${response.status} message: ${response.text}`,
        );
      }
      const json: Product[] = await response.json();
      setAllProducts(json);
    } catch (err: any) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }
  async function handleAdd() {
    if (selectedProd === "") return;
    await fetch(
      url + "/" + categoryDisplayed?.id + "/products/" + selectedProd,
      {
        method: "POST",
      },
    );
    fetchProducts(categoryDisplayed);
    setStatus("list");
  }
  useEffect(() => {
    fetchData();
    fetchAllProducts();
  }, []);

  useEffect(() => {
    fetchProducts(categoryDisplayed);
  }, [categoryDisplayed]);

  if (loading) {
    return <span className="loader"></span>;
  }

  if (error) {
    return <div>Error: {error?.message}</div>;
  }

  if (data) {
    return (
      <>
        <div className="with-sidebar">
          <div className="sidebar">
            {sidebar === "list" ? (
              <div>
                <h2>Categories</h2>
                <button
                  aria-label="add category"
                  onClick={() => setSidebar("form-list")}
                >
                  <p className="fa-solid fa-plus" aria-hidden="true"></p>{" "}
                  Category
                </button>
              </div>
            ) : (
              <div>
                <h2>Add Category</h2>
                <button
                  aria-label="add category"
                  onClick={() => setSidebar("list")}
                >
                  <p className="fa-solid fa-times" aria-hidden="true"></p>{" "}
                  Cancel
                </button>
                <CategoryForm
                  onCreate={handleCreate}
                  onUpdate={handleUpdate}
                  prevCategory={null}
                />
              </div>
            )}
            {data.map((category) => (
              <>
                <div
                  key={category.id}
                  className="cat-list"
                  onClick={() => setCategoryDisplayed(category)}
                >
                  {category.id === categoryDisplayed?.id ? (
                    <h3 className="green">{category.name}</h3>
                  ) : (
                    <h4>{category.name}</h4>
                  )}
                  <span>
                    <button
                      aria-label="delete category"
                      onClick={() => {
                        handleDelete(category);
                      }}
                      className="red"
                    >
                      <p className="fa-solid fa-trash"></p>
                    </button>
                  </span>
                </div>
                <hr></hr>
              </>
            ))}
          </div>
          <div className="list">
            <h2>{categoryDisplayed?.name}</h2>
            {categoryDisplayed ? (
              status === "list" ? (
                <div>
                  <p>{categoryDisplayed?.description}</p>
                  <button onClick={() => setStatus("create")}>Edit</button>
                  <select
                    name="products"
                    value={selectedProd}
                    onChange={handleChange}
                  >
                    <option value="">select products to add</option>
                    {allProducts
                      .filter((prod) => {
                        return products.every((item) => item.id !== prod.id);
                      })
                      .map((prod) => (
                        <option key={prod.id} value={prod.id ? prod.id : ""}>
                          {prod.name}
                        </option>
                      ))}
                  </select>
                  <button onClick={handleAdd}>
                    <i className="fas fa-check"></i>
                  </button>
                </div>
              ) : (
                <>
                  <CategoryForm
                    onCreate={handleCreate}
                    onUpdate={handleUpdate}
                    prevCategory={categoryDisplayed}
                  />
                  <button onClick={() => setStatus("list")}>Cancel</button>
                </>
              )
            ) : (
              <h2>Select Category</h2>
            )}
            <div className="wrap">
              {products
                ? products.map((prod) => (
                    <div className="wrap-item">
                      <ProductDetail product={prod} />
                      <div>
                        <button
                          className="red"
                          onClick={() => handleRemove(prod)}
                        >
                          Remove from category
                        </button>
                        <Link to={"/products/" + String(prod.id)}>
                          <button>Details</button>{" "}
                        </Link>
                      </div>
                    </div>
                  ))
                : ""}
            </div>
          </div>
        </div>
      </>
    );
  }
  return null;
}

export default CategoriesPage;
