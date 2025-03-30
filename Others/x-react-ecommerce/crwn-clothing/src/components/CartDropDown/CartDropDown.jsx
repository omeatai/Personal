import React from "react";
import { useNavigate } from "react-router-dom";

import Button from "../Button/Button";
import CartItem from "../CartItem/CartItem";
import {
  CartDropdownContainer,
  EmptyMessage,
  CartItems,
} from "./CartDropDownStyle";

// import { CartContext } from "../../contexts/cartContext";
import { useSelector } from "react-redux";
import { selectCartItems } from "../../store/cart/cartSelector";

const CartDropDown = () => {
  // const { cartItems } = useContext(CartContext);
  const cartItems = useSelector(selectCartItems);
  const navigate = useNavigate();

  const GoToCheckoutHandler = () => {
    navigate("/checkout");
  };

  return (
    <CartDropdownContainer>
      <CartItems>
        {cartItems.length > 0 ? (
          cartItems.map((item) => <CartItem key={item.id} cartItem={item} />)
        ) : (
          <EmptyMessage>Your Cart is Empty!</EmptyMessage>
        )}
      </CartItems>
      <Button onClick={GoToCheckoutHandler}>GO TO CHECKOUT</Button>
    </CartDropdownContainer>
  );
};

export default CartDropDown;
