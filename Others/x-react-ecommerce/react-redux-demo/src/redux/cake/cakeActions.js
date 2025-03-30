import { BUY_CAKE } from "./cakeTypes";

//Action creator (function that returns an action)
export const buyCake = (number = 1) => {
  return {
    type: BUY_CAKE,
    payload: number,
  };
};
