import { BUY_ICECREAM } from "./iceCreamTypes";

//Action creator (function that returns an action)
export const buyIceCream = () => {
  return {
    type: BUY_ICECREAM,
  };
};
