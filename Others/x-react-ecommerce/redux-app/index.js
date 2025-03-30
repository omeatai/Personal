// import redux from 'redux';
// import { legacy_createStore as createStore } from 'redux';
// import { combineReducers } from "redux";
// import logger from 'redux-logger'

const redux = require("redux");
const reduxLogger = require("redux-logger");

const createStore = redux.legacy_createStore;
const combineReducers = redux.combineReducers;
const applyMiddleware = redux.applyMiddleware;
const logger = reduxLogger.createLogger();

//action type
const BUY_CAKE = "BUY_CAKE";
const BUY_ICECREAM = "BUY_ICECREAM";

//action function (action creator)
function buyCake() {
  return {
    type: BUY_CAKE,
    info: "Buy Cake redux action",
  };
}

function buyIceCream() {
  return {
    type: BUY_ICECREAM,
    info: "Buy Ice Cream redux action",
  };
}

//intial state
// const initialState = {
//   numOfCakes: 10,
//   numOfIceCreams: 20,
// };

//intial state for cakes
const initialCakeState = {
  numOfCakes: 10,
};

//intial state for ice cream
const initialIceCreamState = {
  numOfIceCreams: 20,
};

//reducer function
// const reducer = (state = initialState, action) => {
//   switch (action.type) {
//     case BUY_CAKE:
//       return {
//         ...state,
//         numOfCakes: state.numOfCakes - 1,
//       };

//     case BUY_ICECREAM:
//       return {
//         ...state,
//         numOfIceCreams: state.numOfIceCreams - 1,
//       };

//     default:
//       return state;
//   }
// };

//cake reducer function
const cakeReducer = (state = initialCakeState, action) => {
  switch (action.type) {
    case BUY_CAKE:
      return {
        ...state,
        numOfCakes: state.numOfCakes - 1,
      };

    default:
      return state;
  }
};

//iceCream reducer function
const iceCreamReducer = (state = initialIceCreamState, action) => {
  switch (action.type) {
    case BUY_ICECREAM:
      return {
        ...state,
        numOfIceCreams: state.numOfIceCreams - 1,
      };

    default:
      return state;
  }
};

//combine reducers as root reducer
const rootReducer = combineReducers({
  cake: cakeReducer,
  iceCream: iceCreamReducer,
});

//create store
const store = createStore(rootReducer, applyMiddleware(logger));
console.log("Initial state", store.getState());

//listener service
const unsubscribe = store.subscribe(
  () => {}
  //   console.log("Updated state", store.getState()
);

//perform action
store.dispatch(buyCake());
store.dispatch(buyCake());
store.dispatch(buyCake());
store.dispatch(buyIceCream());
store.dispatch(buyIceCream());

//close service
unsubscribe();
