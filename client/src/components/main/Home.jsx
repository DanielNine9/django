import React, { useState, useEffect } from "react";
import Banner from "./Banner";
import ProductItem from "../product/ProductItem";
import { get_products_request } from "../../api";

const Home = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const get_products = async () => {
      const res = await get_products_request();
      if (res.status >= 400) return;
      console.log(res)
      setProducts(res?.data?.data);
    };

    get_products();
  }, []);

  return (
    <div className="">
      <div className="container mx-auto mt-8">
        <div className="text-center text-[16px] flex flex-col items-center">
          <h2 className="text-xl font-thin mb-2">Sản phẩm nổi bật</h2>
          <div className="border border-gray-400 w-1/12"></div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8  py-12">
          {products?.length
            ? products?.map((product) => (
                <ProductItem key={product.id} {...product} />
              ))
            : "Currently, there are no products"}
        </div>
      </div>
    </div>
  );
};

export default Home;
