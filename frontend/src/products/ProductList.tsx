import { Link } from "react-router-dom";
import { Product } from "./Product";

export interface Props {
  products: Product[];
  onDelete: (product: Product) => void;
}

function ProductList({ products, onDelete }: Props) {
  const url = "http://localhost:8000/inventory/products";
  async function handleDelete(product: Product) {
    await fetch(url + "/" + product.id, { method: "DELETE" });
    onDelete(product);
  }
  return (
    <div className="list">
      {products.map((product) => (
        <div key={product.id} className="list-item">
          <Link to={`./${product.id}`}>
            <div className="prod-list-container">
              <h4>{product.name}</h4>
              <p># {product.quantity || "N/A"}</p>
            </div>
          </Link>
          <span>
            <button
              aria-label="delete product"
              onClick={() => handleDelete(product)}
            >
              <p className="fa-solid fa-trash"></p>
            </button>
          </span>
        </div>
      ))}
    </div>
  );
}

export default ProductList;
