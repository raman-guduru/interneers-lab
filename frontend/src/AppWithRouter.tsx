import { Routes, Route, Outlet, Link } from "react-router-dom";
import ProductsPage from "./products/ProductsPage";
import ProductPage from "products/ProductPage";
import "./AppWithRouter.scss";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="products" element={<ProductsPage />} />
        <Route path="products/:id" element={<ProductPage />} />
        <Route path="*" element={<NoMatch />} />
      </Route>
    </Routes>
  );
}

function Layout() {
  return (
    <>
      <nav>
        <div>
          <Link to="/" className="link" id="main-link">
            INVENTORY
          </Link>
        </div>
        <div>
          <Link to="/products" className="link">
            Products
          </Link>
        </div>
      </nav>
      <main>
        <Outlet />
      </main>
    </>
  );
}

function Home() {
  return (
    <div>
      <h2>Home</h2>
      <Link to="/products" className="link">
        <button>Products</button>
      </Link>
    </div>
  );
}

function NoMatch() {
  return (
    <div>
      <h2>Nothing to see here!</h2>
      <p>
        <Link to="/">Go to the home page</Link>
      </p>
    </div>
  );
}
