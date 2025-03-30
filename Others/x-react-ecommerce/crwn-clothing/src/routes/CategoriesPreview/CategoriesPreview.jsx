import React, { Fragment } from "react";
// import { CategoriesContext } from "../../contexts/categoriesContext";
import CategoryPreview from "../../components/CategoryPreview/CategoryPreview";

import "./CategoriesPreview.scss";
import { selectCategoriesMap } from "../../store/categories/categorySelector";
import { useSelector } from "react-redux";

const CategoriesPreview = () => {
  // const { categoriesMap } = useContext(CategoriesContext);
  const categoriesMap = useSelector(selectCategoriesMap);

  return (
    <Fragment>
      {Object.keys(categoriesMap).map((title) => {
        const products = categoriesMap[title];

        return (
          <CategoryPreview key={title} title={title} products={products} />
        );
      })}
    </Fragment>
  );
};

export default CategoriesPreview;
