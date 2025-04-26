import { Product } from "./Product";

export interface Props {
  product: Product;
}

function ProductCard({ product }: Props) {
  return (
    <div className="card">
      <h2 className="prod-title">{product.name}</h2>
      <p className="prod-brand">Brand: {product.brand}</p>
      <p className="prod-desc">{product.description}</p>
      <div className="prod-pq">
        <p className="prod-price">Price: {product.price}</p>
        <p className="prod-quantity">Quantity: {product.price}</p>
      </div>
    </div>
  );
}

export default ProductCard;
