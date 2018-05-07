exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accu, el) => {
    if (el === searchElement) { accu.push(el); }
    return accu;
  }, []).length;
};
