import React, { useState, useEffect, Fragment } from "react";
import { useParams } from "react-router-dom";
// import { CategoriesContext } from "../../contexts/categoriesContext";
import ProductCard from "../../components/ProductCard/ProductCard";

import { selectCategoriesMap } from "../../store/categories/categorySelector";
import { useSelector } from "react-redux";

import "./Category.scss";

const Category = () => {
  const { category } = useParams();
  // const { categoriesMap } = useContext(CategoriesContext);
  const categoriesMap = useSelector(selectCategoriesMap);
  const [products, setProducts] = useState(categoriesMap[category]);

  useEffect(() => {
    setProducts(categoriesMap[category]);
  }, [category, categoriesMap]);

  return (
    <Fragment>
      <h2 className="category-title">{category.toUpperCase()}</h2>
      <div className="category-container">
        {products &&
          products.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
      </div>
    </Fragment>
  );
};

export default Category;
