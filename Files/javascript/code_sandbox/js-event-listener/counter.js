document.addEventListener("DOMContentLoaded", function () {
  let count = 0;
  const countEl = document.getElementById("count");
  const msgEl = document.getElementById("message");
  const btnPlus = document.getElementById("btnPlus");
  const btnMinus = document.getElementById("btnMinus");
  const btnReset = document.getElementById("btnReset");
  const btnSave = document.getElementById("btnSave");
  const btnLoad = document.getElementById("btnLoad");
  btnPlus.addEventListener("click", increaseCount);
  btnMinus.addEventListener("click", decreaseCount);
  btnReset.addEventListener("click", resetCount);
  btnSave.addEventListener("click", saveCount);
  btnLoad.addEventListener("click", loadCount);
  function updateCount() {
    countEl.innerHTML = count;
  }
  function showMessage(text) {
    msgEl.innerHTML = text;
    setTimeout(function () {
      msgEl.innerHTML = "";
    }, 3000);
  }
  function increaseCount() {
    count++;
    updateCount();
  }
  function decreaseCount() {
    count--;
    updateCount();
  }
  function resetCount() {
    count = 0;
    updateCount();
  }
  function saveCount() {
    localStorage.setItem("count", count);
    showMessage("Saved!");
  }
  function loadCount() {
    let saved = localStorage.getItem("count");
    if (saved !== null) {
      count = Number(saved);
      showMessage("Loaded!");
    }
    updateCount();
  }
});
