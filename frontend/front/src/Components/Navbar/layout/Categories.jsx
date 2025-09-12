import { CATEGORIES } from "../../../constants/categories";

const Categories = ({ activeCategory, onClick }) => (
  <div className="flex overflow-x-auto scrollbar-hide max-w-full mx-auto px-4 sm:px-6 lg:px-8 mt-2">
    <div className="flex space-x-4 py-2 whitespace-nowrap">
      {CATEGORIES.map((category) => (
        <button
          key={category}
          onClick={() => onClick(category)}
          className={`px-4 py-2 rounded-md text-sm font-medium transition-all duration-500 ${
            activeCategory === category
              ? "bg-white text-purple-600 font-bold"
              : "text-white hover:bg-purple-600"
          }`}
        >
          {category}
        </button>
      ))}
    </div>
  </div>
);

export default Categories;
