import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white">
      <div className="container mx-auto py-12 grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="col-span-2">
          <h3 className="text-2xl font-semibold mb-4">My Shoe Store</h3>
          <div className="flex space-x-6">
            <a href="#" className="hover:text-gray-300 transition duration-300">Home</a>
            <a href="#" className="hover:text-gray-300 transition duration-300">Shop</a>
            <a href="#" className="hover:text-gray-300 transition duration-300">Contact</a>
          </div>
        </div>
        <div>
          <h3 className="text-2xl font-semibold mb-4">Follow Us</h3>
          <div className="flex space-x-4">
            <a href="#" className="text-gray-300 hover:text-white transition duration-300">
              <i className="fab fa-facebook-square"></i>
            </a>
            <a href="#" className="text-gray-300 hover:text-white transition duration-300">
              <i className="fab fa-twitter"></i>
            </a>
            <a href="#" className="text-gray-300 hover:text-white transition duration-300">
              <i className="fab fa-instagram"></i>
            </a>
          </div>
        </div>
        <div>
          <h3 className="text-2xl font-semibold mb-4">Newsletter</h3>
          <p className="text-sm mb-4">Subscribe to our newsletter for the latest updates and promotions.</p>
          <div className="flex">
            <input
              type="email"
              placeholder="Your email"
              className="py-2 px-3 border rounded-l focus:outline-none focus:border-gray-500"
            />
            <button className="bg-blue-500 text-white py-2 px-4 rounded-r hover:bg-blue-600 transition duration-300">
              Subscribe
            </button>
          </div>
        </div>
      </div>
      <div className="bg-gray-800 py-4">
        <div className="container mx-auto text-sm text-gray-500">
          <p>&copy; 2023 Your Shoe Store. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
