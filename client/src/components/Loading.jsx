import React from 'react';

const Loading = () => {
  return (
    <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-900 bg-opacity-50 z-50">
<div className="w-12 h-12 border-4 border-gray-300 rounded-full border-t-blue-500 animate-spin"></div>
    {/* <img src="https://cdn.pixabay.com/animation/2022/07/29/03/42/03-42-11-849_512.gif" alt="" /> */}
    </div>
  );
};

export default Loading;
