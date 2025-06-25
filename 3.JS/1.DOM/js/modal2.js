const open = document.getElementById("open");

open.onclick = () => {
  showModal();
};

function showModal() {
  const modalWrapper = document.createElement("div");
  modalWrapper.className = "modal-wrapper";
  //하나하나 만들기 귀찮아서 모달창 안에 html 넣기
  modalWrapper.innerHTML = `
    <div class="modal">
        <div class="modal-title">모달 타이틀</div>
        <p>모달 본문 내용</p>
        <div class="close-wrapper">
          <button id="close">닫기</button>
        </div>
      </div>`;
  document.body.appendChild(modalWrapper);

  //닫기 버튼 이벤트 추가
  document.getElementById("close").onclick = () => {
    modalWrapper.remove();
  };
}

//   const close = document.getElementById("close");
//   close.onclick = () => {
//  modalWrapper.remove();
//   }
