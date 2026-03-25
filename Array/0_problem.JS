const solution = () => {
  return (...arg) => {
    return `Hello World`;
  };
};

console.log(solution({})());
console.log(solution("")());
console.log(solution([])());
console.log(solution("1")());
console.log(solution("1")());
