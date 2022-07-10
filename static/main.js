function openbar() {
  document.getElementById("sidenav").style.width = "25%";
}

function closebar() {
  document.getElementById("sidenav").style.width = "0";
}

function hideorshowtable(ele) {
    if (ele.checked == true){
        ele.nextElementSibling.style.display = "none";
    } else {
        ele.nextElementSibling.style.display = "table";
    }
}

function hideorshow(ele) {
    if (ele.checked == true){
        ele.nextElementSibling.style.display = "none";
    } else {
        ele.nextElementSibling.style.display = "block";
    }
}
