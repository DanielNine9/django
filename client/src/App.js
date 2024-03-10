import "./App.css";
import { BrowserRouter, Outlet, Route, Routes } from "react-router-dom";
import Home from "./components/main/Home";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import Header from "./components/header/Header";
import Footer from "./components/footer/Footer";
import Banner from "./components/main/Banner";
import Cart from "./components/cart/Cart";
import ViewDetails from "./components/main/ViewDetails";
import Filter from "./components/main/Filter";
import VerificationForm from "./components/VerificationForm";
import ResetPassword from "./components/auth/ResetPassword";

const Layout = ({ children }) => (
  <div className="App">
    <Header />
    <Banner />
    {children}
    <Footer />
  </div>
);

const LayoutNotBanner = ({ children }) => (
  <div className="App">
    <header>
      <Header />
    </header>
    {children}
    <Footer />
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          element={
            <Layout>
              <Outlet />
            </Layout>
          }
        >
          <Route path="/" element={<Home />} />
        </Route>
        {/* <Route path="/product-sold" element={<ProductSold />} />
        <Route path="/user-management" element={<UserManagement />} />
        <Route path="/my-sellers" element={<MySeller />} />
        <Route path="/create-product" element={<CreateProduct />} />

        <Route path="/forbidden" element={<ForbiddenPage />} />
        <Route path="/wrong" element={<Something />} /> */}

        {/* layout not banner */}
        <Route
          element={
            <LayoutNotBanner>
              <Outlet />
            </LayoutNotBanner>
          }
        >
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/view-details" element={<ViewDetails />} />
          <Route path="/filter/:header" element={<Filter />} />
          <Route path="/verify" element={<VerificationForm />} />
          <Route path="/reset" element={<ResetPassword />} />

        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
