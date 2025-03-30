import React from "react";
import { useNavigate } from "react-router-dom";

import {
  BackgroundImage,
  CategoryBodyContainer,
  CategoryItemContainer,
} from "./CategoryItemStyle.js";

const CategoryItem = ({ category }) => {
  const { imageUrl, title, route } = category;
  const navigate = useNavigate();

  const onNavigateHandler = () => navigate(route);

  return (
    <CategoryItemContainer onClick={onNavigateHandler}>
      <BackgroundImage imageUrl={imageUrl} />
      <CategoryBodyContainer>
        <h2>{title}</h2>
        <p>Shop Now</p>
      </CategoryBodyContainer>
    </CategoryItemContainer>
  );
};

export default CategoryItem;
