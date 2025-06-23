function number_inc() {
  let number = document.getElementById("result");
  let number_String = number.textContent;
  //div 요소 안에 있는 글을 가져오는 3가지방법
  // innerText - 글자만 가져온다.(디자인 속성을 적용받음)
  // innerHtml - 글자와 그 태그까지 함께 가져온다.
  // textContet - 순수 글자만 가져온다
  console.log(number);
  let number_string_to_number = Number(number_String);
  let result = number_string_to_number + 1;
  number.textContent = result;
}
function number_dec() {
  // let number = document.getElementById("result");
  //let number_String = number.textContent;
  //console.log(number);
  //let number_string_to_number = Number(number_String);
  //let result = number_string_to_number - 1;
  //number.textContent = result;
  let result = document.getElementById("result");
  result.textContent = Number(result.textContent) - 1;
}
