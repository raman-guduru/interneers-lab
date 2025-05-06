import { Product } from "./Product";

export interface Props {
  product: Product;
}

function ProductDetail({ product }: Props) {
  return (
    <>
      {/* <h2>{product.name || "N/A"}</h2> */}
      <div className="detail-container">
        <div className="row">
          <span>Name</span>
          <p>{product.name}</p>
        </div>
        <hr />
        <div className="row">
          <span>Brand</span>
          <p>{product.brand}</p>
        </div>
        <hr />
        <div>
          <span>Description</span>
          <p>{product.description ? product.description : "N/A"}</p>
        </div>
        <hr />
        <div className="row">
          <span>Price</span>
          <p>{product.price ? product.price : "N/A"}</p>
        </div>
        <hr />
        <div className="row">
          <span>Quantity</span>
          <p>{product.quantity ? product.quantity : "N/A"}</p>
        </div>
      </div>
    </>
  );
}

export default ProductDetail;
