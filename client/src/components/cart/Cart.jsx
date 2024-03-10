import React from "react";
import Navigation from "../main/Navigation";

const Cart = () => {
  return (
    <>
      {/* component */}
      {/* Create By Joker Banny */}
      <style
        dangerouslySetInnerHTML={{
          __html:
            '\n    @layer utilities {\n    input[type="number"]::-webkit-inner-spin-button,\n    input[type="number"]::-webkit-outer-spin-button {\n      -webkit-appearance: none;\n      margin: 0;\n    }\n  }\n',
        }}
      />
      <div className="h-screen bg-gray-100 pt-20">
        <h1 className="mb-10 text-center text-2xl font-bold">Cart Items</h1>
        <div className="mx-auto max-w-5xl justify-center px-6 md:flex md:space-x-6 xl:px-0">
          <div className="rounded-lg md:w-2/3">
            <div className="justify-between mb-6 rounded-lg bg-white p-6 shadow-md sm:flex sm:justify-start">
              <img
                src="https://images.unsplash.com/photo-1515955656352-a1fa3ffcd111?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
                alt="product-image"
                className="w-full rounded-lg sm:w-40"
              />
              <div className="sm:ml-4 sm:flex sm:w-full sm:justify-between">
                <div className="mt-5 sm:mt-0">
                  <h2 className="text-lg font-bold text-gray-900">
                    Nike Air Max 2019
                  </h2>
                  <p className="mt-1 text-xs text-gray-700">36EU - 4US</p>
                </div>
                <div className="mt-4 flex justify-between sm:space-y-6 sm:mt-0 sm:block sm:space-x-6">
                  <div className="flex items-center border-gray-100">
                    <span className="cursor-pointer rounded-l bg-gray-100 py-1 px-3.5 duration-100 hover:bg-blue-500 hover:text-blue-50">
                      {" "}
                      -{" "}
                    </span>
                    <input
                      className="h-8 w-8 border bg-white text-center text-xs outline-none"
                      type="number"
                      defaultValue={2}
                      min={1}
                    />
                    <span className="cursor-pointer rounded-r bg-gray-100 py-1 px-3 duration-100 hover:bg-blue-500 hover:text-blue-50">
                      {" "}
                      +{" "}
                    </span>
                  </div>
                  <div className="flex items-center space-x-4">
                    <p className="text-sm">259.000 ₭</p>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      strokeWidth="1.5"
                      stroke="currentColor"
                      className="h-5 w-5 cursor-pointer duration-150 hover:text-red-500"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M6 18L18 6M6 6l12 12"
                      />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
            <div className="justify-between mb-6 rounded-lg bg-white p-6 shadow-md sm:flex sm:justify-start">
              <img
                src="https://images.unsplash.com/photo-1587563871167-1ee9c731aefb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1131&q=80"
                alt="product-image"
                className="w-full rounded-lg sm:w-40"
              />
              <div className="sm:ml-4 sm:flex sm:w-full sm:justify-between">
                <div className="mt-5 sm:mt-0">
                  <h2 className="text-lg font-bold text-gray-900">
                    Nike Air Max 2019
                  </h2>
                  <p className="mt-1 text-xs text-gray-700">36EU - 4US</p>
                </div>
                <div className="mt-4 flex justify-between im sm:space-y-6 sm:mt-0 sm:block sm:space-x-6">
                  <div className="flex items-center border-gray-100">
                    <span className="cursor-pointer rounded-l bg-gray-100 py-1 px-3.5 duration-100 hover:bg-blue-500 hover:text-blue-50">
                      {" "}
                      -{" "}
                    </span>
                    <input
                      className="h-8 w-8 border bg-white text-center text-xs outline-none"
                      type="number"
                      defaultValue={2}
                      min={1}
                    />
                    <span className="cursor-pointer rounded-r bg-gray-100 py-1 px-3 duration-100 hover:bg-blue-500 hover:text-blue-50">
                      {" "}
                      +{" "}
                    </span>
                  </div>
                  <div className="flex items-center space-x-4">
                    <p className="text-sm">259.000 ₭</p>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      strokeWidth="1.5"
                      stroke="currentColor"
                      className="h-5 w-5 cursor-pointer duration-150 hover:text-red-500"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        d="M6 18L18 6M6 6l12 12"
                      />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
          {/* Sub total */}
          <div className="mt-6 h-full rounded-lg border bg-white p-6 shadow-md md:mt-0 md:w-1/3">
            <div className="mb-2 flex justify-between">
              <p className="text-gray-700">Subtotal</p>
              <p className="text-gray-700">$129.99</p>
            </div>
            <div className="flex justify-between">
              <p className="text-gray-700">Shipping</p>
              <p className="text-gray-700">$4.99</p>
            </div>
            <hr className="my-4" />
            <div className="flex justify-between">
              <p className="text-lg font-bold">Total</p>
              <div className="">
                <p className="mb-1 text-lg font-bold">$134.98 USD</p>
                <p className="text-sm text-gray-700">including VAT</p>
              </div>
            </div>
            <button className="mt-6 w-full rounded-md bg-blue-500 py-1.5 font-medium text-blue-50 hover:bg-blue-600">
              Check out
            </button>
          </div>
        </div>
      </div>
    </>

    // <div className="min-h-[200px]">
    //   <Navigation title="Giỏ hàng" />
    //   <>
    //     {/* Hello world */}
    //     <div className="container mx-auto mt-10">
    //       <div className="flex shadow-md my-10">
    //         <div className="w-3/4 bg-white px-10 py-10">
    //           <div className="flex justify-between border-b pb-8">
    //             <h1 className="font-semibold text-2xl">Shopping Cart</h1>
    //             <h2 className="font-semibold text-2xl">3 Items</h2>
    //           </div>
    //           <div className="flex mt-10 mb-5">
    //             <h3 className="font-semibold text-gray-600 text-xs uppercase w-2/5">
    //               Product Details
    //             </h3>
    //             <h3 className="font-semibold text-center text-gray-600 text-xs uppercase w-1/5 text-center">
    //               Quantity
    //             </h3>
    //             <h3 className="font-semibold text-center text-gray-600 text-xs uppercase w-1/5 text-center">
    //               Price
    //             </h3>
    //             <h3 className="font-semibold text-center text-gray-600 text-xs uppercase w-1/5 text-center">
    //               Total
    //             </h3>
    //           </div>
    //           <div className="flex items-center hover:bg-gray-100 -mx-8 px-6 py-5">
    //             <div className="flex w-2/5">
    //               {" "}
    //               {/* product */}
    //               <div className="w-20">
    //                 <img
    //                   className="h-24"
    //                   src="https://drive.google.com/uc?id=18KkAVkGFvaGNqPy2DIvTqmUH_nk39o3z"
    //                   alt=""
    //                 />
    //               </div>
    //               <div className="flex flex-col justify-between ml-4 flex-grow">
    //                 <span className="font-bold text-sm">Iphone 6S</span>
    //                 <span className="text-red-500 text-xs">Apple</span>
    //                 <a
    //                   href="#"
    //                   className="font-semibold hover:text-red-500 text-gray-500 text-xs"
    //                 >
    //                   Remove
    //                 </a>
    //               </div>
    //             </div>
    //             <div className="flex justify-center w-1/5">
    //               <svg
    //                 className="fill-current text-gray-600 w-3"
    //                 viewBox="0 0 448 512"
    //               >
    //                 <path d="M416 208H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h384c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z" />
    //               </svg>
    //               <input
    //                 className="mx-2 border text-center w-8"
    //                 type="text"
    //                 defaultValue={1}
    //               />
    //               <svg
    //                 className="fill-current text-gray-600 w-3"
    //                 viewBox="0 0 448 512"
    //               >
    //                 <path d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z" />
    //               </svg>
    //             </div>
    //             <span className="text-center w-1/5 font-semibold text-sm">
    //               $400.00
    //             </span>
    //             <span className="text-center w-1/5 font-semibold text-sm">
    //               $400.00
    //             </span>
    //           </div>
    //           <div className="flex items-center hover:bg-gray-100 -mx-8 px-6 py-5">
    //             <div className="flex w-2/5">
    //               {" "}
    //               {/* product */}
    //               <div className="w-20">
    //                 <img
    //                   className="h-24"
    //                   src="https://drive.google.com/uc?id=10ht6a9IR3K2i1j0rHofp9-Oubl1Chraw"
    //                   alt=""
    //                 />
    //               </div>
    //               <div className="flex flex-col justify-between ml-4 flex-grow">
    //                 <span className="font-bold text-sm">
    //                   Xiaomi Mi 20000mAh
    //                 </span>
    //                 <span className="text-red-500 text-xs">Xiaomi</span>
    //                 <a
    //                   href="#"
    //                   className="font-semibold hover:text-red-500 text-gray-500 text-xs"
    //                 >
    //                   Remove
    //                 </a>
    //               </div>
    //             </div>
    //             <div className="flex justify-center w-1/5">
    //               <svg
    //                 className="fill-current text-gray-600 w-3"
    //                 viewBox="0 0 448 512"
    //               >
    //                 <path d="M416 208H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h384c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z" />
    //               </svg>
    //               <input
    //                 className="mx-2 border text-center w-8"
    //                 type="text"
    //                 defaultValue={1}
    //               />
    //               <svg
    //                 className="fill-current text-gray-600 w-3"
    //                 viewBox="0 0 448 512"
    //               >
    //                 <path d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z" />
    //               </svg>
    //             </div>
    //             <span className="text-center w-1/5 font-semibold text-sm">
    //               $40.00
    //             </span>
    //             <span className="text-center w-1/5 font-semibold text-sm">
    //               $40.00
    //             </span>
    //           </div>
    //           <div className="flex items-center hover:bg-gray-100 -mx-8 px-6 py-5">
    //             <div className="flex w-2/5">
    //               {" "}
    //               {/* product */}
    //               <div className="w-20">
    //                 <img
    //                   className="h-24"
    //                   src="https://drive.google.com/uc?id=1vXhvO9HoljNolvAXLwtw_qX3WNZ0m75v"
    //                   alt=""
    //                 />
    //               </div>
    //               <div className="flex flex-col justify-between ml-4 flex-grow">
    //                 <span className="font-bold text-sm">Airpods</span>
    //                 <span className="text-red-500 text-xs">Apple</span>
    //                 <a
    //                   href="#"
    //                   className="font-semibold hover:text-red-500 text-gray-500 text-xs"
    //                 >
    //                   Remove
    //                 </a>
    //               </div>
    //             </div>
    //             <div className="flex justify-center w-1/5">
    //               <svg
    //                 className="fill-current text-gray-600 w-3"
    //                 viewBox="0 0 448 512"
    //               >
    //                 <path d="M416 208H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h384c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z" />
    //               </svg>
    //               <input
    //                 className="mx-2 border text-center w-8"
    //                 type="text"
    //                 defaultValue={1}
    //               />
    //               <svg
    //                 className="fill-current text-gray-600 w-3"
    //                 viewBox="0 0 448 512"
    //               >
    //                 <path d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z" />
    //               </svg>
    //             </div>
    //             <span className="text-center w-1/5 font-semibold text-sm">
    //               $150.00
    //             </span>
    //             <span className="text-center w-1/5 font-semibold text-sm">
    //               $150.00
    //             </span>
    //           </div>
    //           <a
    //             href="#"
    //             className="flex font-semibold text-indigo-600 text-sm mt-10"
    //           >
    //             <svg
    //               className="fill-current mr-2 text-indigo-600 w-4"
    //               viewBox="0 0 448 512"
    //             >
    //               <path d="M134.059 296H436c6.627 0 12-5.373 12-12v-56c0-6.627-5.373-12-12-12H134.059v-46.059c0-21.382-25.851-32.09-40.971-16.971L7.029 239.029c-9.373 9.373-9.373 24.569 0 33.941l86.059 86.059c15.119 15.119 40.971 4.411 40.971-16.971V296z" />
    //             </svg>
    //             Continue Shopping
    //           </a>
    //         </div>
    //         <div id="summary" className="w-1/4 px-8 py-10">
    //           <h1 className="font-semibold text-2xl border-b pb-8">
    //             Order Summary
    //           </h1>
    //           <div className="flex justify-between mt-10 mb-5">
    //             <span className="font-semibold text-sm uppercase">Items 3</span>
    //             <span className="font-semibold text-sm">590$</span>
    //           </div>
    //           <div>
    //             <label className="font-medium inline-block mb-3 text-sm uppercase">
    //               Shipping
    //             </label>
    //             <select className="block p-2 text-gray-600 w-full text-sm">
    //               <option>Standard shipping - $10.00</option>
    //             </select>
    //           </div>
    //           <div className="py-10">
    //             <label
    //               htmlFor="promo"
    //               className="font-semibold inline-block mb-3 text-sm uppercase"
    //             >
    //               Promo Code
    //             </label>
    //             <input
    //               type="text"
    //               id="promo"
    //               placeholder="Enter your code"
    //               className="p-2 text-sm w-full"
    //             />
    //           </div>
    //           <button className="bg-red-500 hover:bg-red-600 px-5 py-2 text-sm text-white uppercase">
    //             Apply
    //           </button>
    //           <div className="border-t mt-8">
    //             <div className="flex font-semibold justify-between py-6 text-sm uppercase">
    //               <span>Total cost</span>
    //               <span>$600</span>
    //             </div>
    //             <button className="bg-indigo-500 font-semibold hover:bg-indigo-600 py-3 text-sm text-white uppercase w-full">
    //               Checkout
    //             </button>
    //           </div>
    //         </div>
    //       </div>
    //     </div>
    //   </>
    // </div>
  );
};

export default Cart;
