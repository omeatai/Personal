import React, { useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import CategoriesPreview from "../CategoriesPreview/CategoriesPreview";
import Category from "../Category/Category";
import "./Shop.scss";

import { getCategoriesAndDocuments } from "../../utils/firebase/firebase";
import { setCategories } from "../../store/categories/categoryAction";
import { useDispatch } from "react-redux";

const Shop = () => {
  const dispatch = useDispatch();

  //Get Categories collection with documents
  useEffect(() => {
    const getCategoriesMap = async () => {
      // const categoryMap = await getCategoriesAndDocuments();
      const categoriesArray = await getCategoriesAndDocuments();
      console.log(categoriesArray);
      dispatch(setCategories(categoriesArray));
    };
    getCategoriesMap();
  }, [dispatch]);

  return (
    <Routes>
      <Route index element={<CategoriesPreview />} />
      <Route path=":category" element={<Category />} />
    </Routes>
  );
};

export default Shop;
