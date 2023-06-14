#!/isr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  let i = 0;
  let listLenght = list.length;
  listLenght = listLenght - 1;
  while (listLenght >= 0) {
    reverseList[i] = list[listLenght];
    --listLenght;
    i++;
  }
  return (reverseList);
};
