#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let counter = 0;
  const listLenght = list.length;
  for (i = 0; i < listLenght; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return (counter);
};
