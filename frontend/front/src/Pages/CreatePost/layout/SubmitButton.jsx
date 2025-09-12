import React from "react";

const SubmitButton = ({ label }) => {
  return (
    <div className="flex justify-end">
      <button
        type="submit"
        className="px-6 py-3 bg-purple-500 text-white rounded-lg hover:bg-purple-600 transition-all duration-200 font-semibold"
      >
        {label}
      </button>
    </div>
  );
};

export default SubmitButton;
