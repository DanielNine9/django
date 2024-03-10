import React from "react";
import { Link } from "react-router-dom";

const ProductItem = (product) => {
  const discountedPrice =
    product.price - (product.price * product.discount) / 100;
  return (
    <Link
      to="/view-details"
      className="flex flex-col items-center gap-2 w-300px px-4 relative"
    >
      <div className="w-full h-[190px]">
        <img
          src={product.image}
          alt={product.name}
          className="max-w-full h-full bg-contain"
        />
      </div>
      <h2 className="font-bold text-center">{product.name}</h2>
      <div className="flex gap-4">
        {/* <p className="text-red-500 font-bold">${discountedPrice.toFixed(2)}</p>
        <del>${product.price.toFixed(2)}</del> */}
      </div>
      <div className="absolute top-0 right-0 bg-red-500 px-3 py-2 rounded-sm text-white text-[10px] mr-5">
        -{product.discount}%
      </div>
    </Link>
  );
};

export default ProductItem;
