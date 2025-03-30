import React from "react";
import Button, { BUTTON_TYPE_CLASSES } from "../Button/Button";
import "./ProductCard.scss";

// import { CartContext } from "../../contexts/cartContext";
import { useDispatch, useSelector } from "react-redux";
import { addItemToCart } from "../../store/cart/cartAction";
import { selectCartItems } from "../../store/cart/cartSelector";

const ProductCard = ({ product }) => {
  const { name, price, imageUrl } = product;
  // const { addItemToCart } = useContext(CartContext);
  const dispatch = useDispatch();
  const cartItems = useSelector(selectCartItems);
  const addProductToCart = () => dispatch(addItemToCart(cartItems, product));

  return (
    <div className="product-card-container">
      <img src={imageUrl} alt={`${name}`} />
      <div className="footer">
        <span className="name">{name}</span>
        <span className="price">{price}</span>
      </div>
      <Button
        buttonType={BUTTON_TYPE_CLASSES.inverted}
        onClick={addProductToCart}
      >
        Add to Cart
      </Button>
    </div>
  );
};

export default ProductCard;
