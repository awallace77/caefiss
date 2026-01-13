export const getCurrentLocale = () => {
  let lang;
  if (navigator.languages && navigator.languages.length) {
    lang = navigator.languages[0];
  } else {
    lang = navigator.language;
  }
  return lang && lang.includes("fr") ? "fr" : "en";
};
