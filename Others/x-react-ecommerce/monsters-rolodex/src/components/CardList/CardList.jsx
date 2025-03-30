import React from "react";
import "./CardList.css";

const CardList = ({ searchResult }) => {
  return (
    <section className="card-list">
      {searchResult ? null : (
        <div>
          <p style={{ color: "red", fontSize: "42px", fontWeight: "bolder" }}>
            Error Fetching Data....
          </p>
        </div>
      )}
      {!searchResult ? null : searchResult.length > 0 ? (
        searchResult.map((person) => {
          const { id, name, email } = person;
          return (
            <section className="card-container" key={id}>
              <img
                src={`https://robohash.org/${id}?set=set2&size=180x180`}
                alt={`monster ${name}`}
              ></img>
              <h2>{name}</h2>
              <p>{email}</p>
            </section>
          );
        })
      ) : (
        <div>
          <p>No Users Available</p>
        </div>
      )}
    </section>
  );
};
export default CardList;
