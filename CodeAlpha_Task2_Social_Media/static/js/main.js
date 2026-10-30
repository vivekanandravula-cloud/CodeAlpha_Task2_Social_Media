document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("textarea").forEach((field) => {
    field.addEventListener("input", () => {
      field.setCustomValidity(field.value.trim() ? "" : "Please enter some text.");
    });
  });
});
